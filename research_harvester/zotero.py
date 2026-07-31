from __future__ import annotations

import json
import re
import uuid
from datetime import datetime, timezone
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .core import (
    ResearchStore,
    canonicalize_url,
    normalize_arxiv_id,
    normalize_doi,
    normalize_space,
    normalize_title,
)


API_ROOT = "https://api.zotero.org"
ACADEMIC_SOURCES = {"arxiv", "crossref", "openalex", "semantic-scholar"}


class ZoteroError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        retry_after: int | None = None,
    ):
        super().__init__(message)
        self.status_code = status_code
        self.retry_after = retry_after


def _safe_error_body(exc: HTTPError) -> str:
    try:
        body = exc.read().decode("utf-8", errors="replace")
    except OSError:
        return ""
    return normalize_space(body)[:500]


class ZoteroClient:
    def __init__(self, user_id: str, api_key: str, timeout: int = 30):
        self.user_id = str(user_id)
        self.api_key = api_key
        self.timeout = int(timeout)
        self.prefix = f"/users/{self.user_id}"

    def _request(
        self,
        path: str,
        *,
        method: str = "GET",
        query: dict[str, Any] | None = None,
        payload: Any | None = None,
        write_token: bool = False,
    ) -> tuple[Any, dict[str, str]]:
        url = API_ROOT + path
        if query:
            url += "?" + urlencode(query)
        data = None
        headers = {
            "Accept": "application/json",
            "Zotero-API-Version": "3",
            "Zotero-API-Key": self.api_key,
            "User-Agent": "personal-research-harvester/1.1",
        }
        if payload is not None:
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            headers["Content-Type"] = "application/json"
        if write_token:
            headers["Zotero-Write-Token"] = uuid.uuid4().hex
        request = Request(url, data=data, headers=headers, method=method)
        try:
            with urlopen(request, timeout=self.timeout) as response:
                raw = response.read()
                parsed = json.loads(raw.decode("utf-8")) if raw else None
                return parsed, dict(response.headers.items())
        except HTTPError as exc:
            detail = _safe_error_body(exc)
            suffix = f": {detail}" if detail else ""
            retry_value = exc.headers.get("Retry-After") or exc.headers.get("Backoff")
            try:
                retry_after = int(retry_value) if retry_value else None
            except ValueError:
                retry_after = None
            raise ZoteroError(
                f"Zotero API returned HTTP {exc.code}{suffix}",
                status_code=exc.code,
                retry_after=retry_after,
            ) from exc
        except (URLError, TimeoutError) as exc:
            raise ZoteroError(f"Zotero API request failed: {exc}") from exc

    def verify_access(self) -> dict[str, Any]:
        payload, _ = self._request("/keys/current")
        access = (payload or {}).get("access", {}).get("user", {})
        actual_user = str((payload or {}).get("userID", ""))
        if actual_user != self.user_id:
            raise ZoteroError(
                f"The key belongs to Zotero user {actual_user}, not {self.user_id}."
            )
        if not access.get("library"):
            raise ZoteroError("The API key cannot read the personal Zotero library.")
        if not access.get("write"):
            raise ZoteroError("The API key does not have write access.")
        return payload

    def list_collections(self) -> list[dict[str, Any]]:
        payload, _ = self._request(
            self.prefix + "/collections",
            query={"limit": 100, "format": "json"},
        )
        return list(payload or [])

    def ensure_collection(self, name: str) -> str:
        wanted = normalize_space(name).casefold()
        for collection in self.list_collections():
            data = collection.get("data") or {}
            if normalize_space(data.get("name")).casefold() == wanted:
                return str(collection.get("key") or data.get("key"))
        payload, _ = self._request(
            self.prefix + "/collections",
            method="POST",
            payload=[{"name": normalize_space(name), "parentCollection": False}],
            write_token=True,
        )
        key = _created_key(payload, "0")
        if not key:
            raise ZoteroError(f"Zotero did not create collection {name!r}.")
        return key

    def list_top_items(self) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        start = 0
        while True:
            payload, headers = self._request(
                self.prefix + "/items/top",
                query={"limit": 100, "start": start, "format": "json"},
            )
            batch = list(payload or [])
            results.extend(batch)
            start += len(batch)
            total = int(headers.get("Total-Results", start) or start)
            if not batch or start >= total:
                break
        return results

    def create_items(self, items: list[dict[str, Any]]) -> dict[str, Any]:
        payload, _ = self._request(
            self.prefix + "/items",
            method="POST",
            payload=items,
            write_token=True,
        )
        return dict(payload or {})


def _created_key(payload: dict[str, Any] | None, index: str) -> str | None:
    if not payload:
        return None
    for bucket_name in ("successful", "success", "unchanged"):
        entry = (payload.get(bucket_name) or {}).get(index)
        if isinstance(entry, str):
            return entry
        if isinstance(entry, dict):
            data = entry.get("data") or {}
            key = entry.get("key") or data.get("key")
            if key:
                return str(key)
    return None


def _created_version(payload: dict[str, Any] | None, index: str) -> int | None:
    if not payload:
        return None
    entry = (payload.get("successful") or {}).get(index)
    if not isinstance(entry, dict):
        return None
    value = entry.get("version") or (entry.get("data") or {}).get("version")
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def verify_api_key(api_key: str, timeout: int = 30) -> dict[str, Any]:
    client = ZoteroClient("0", api_key, timeout)
    payload, _ = client._request("/keys/current")
    user_id = str((payload or {}).get("userID", ""))
    if not user_id:
        raise ZoteroError("Zotero did not return a user ID for this API key.")
    access = (payload or {}).get("access", {}).get("user", {})
    if not access.get("library"):
        raise ZoteroError("The API key cannot read the personal Zotero library.")
    if not access.get("write"):
        raise ZoteroError("The API key needs personal-library write access.")
    return payload


def _identity_tokens(item: dict[str, Any]) -> set[str]:
    tokens: set[str] = set()
    doi = normalize_doi(item.get("DOI") or item.get("doi"))
    if doi:
        tokens.add(f"doi:{doi}")
    extra = normalize_space(item.get("extra"))
    arxiv_id = normalize_arxiv_id(
        item.get("arxiv_id") or item.get("source_id") or item.get("url") or extra
    )
    if arxiv_id:
        tokens.add(f"arxiv:{arxiv_id}")
    url = canonicalize_url(item.get("url"))
    if url:
        tokens.add(f"url:{url}")
    title = normalize_title(item.get("title"))
    if title:
        tokens.add(f"title:{title}")
    codex_key = re.search(r"(?im)^Codex Research Key:\s*(\S+)", extra)
    if codex_key:
        tokens.add(f"codex:{codex_key.group(1)}")
    canonical_key = item.get("canonical_key")
    if canonical_key:
        tokens.add(f"codex:{canonical_key}")
    return tokens


def build_existing_index(items: Iterable[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for item in items:
        data = item.get("data") or item
        for token in _identity_tokens(data):
            index.setdefault(token, item)
    return index


def find_existing(
    row: dict[str, Any],
    index: dict[str, dict[str, Any]],
) -> dict[str, Any] | None:
    for token in _identity_tokens(row):
        if token in index:
            return index[token]
    return None


def _creator(name: str) -> dict[str, str]:
    cleaned = normalize_space(name)
    if not cleaned:
        return {}
    if "," in cleaned:
        last, first = [part.strip() for part in cleaned.split(",", 1)]
        return {"creatorType": "author", "firstName": first, "lastName": last}
    parts = cleaned.split()
    if len(parts) >= 2:
        return {
            "creatorType": "author",
            "firstName": " ".join(parts[:-1]),
            "lastName": parts[-1],
        }
    return {"creatorType": "author", "name": cleaned}


def _item_type(row: dict[str, Any]) -> str:
    source = str(row.get("source") or "")
    metadata = json.loads(row.get("metadata_json") or "{}")
    source_type = str(metadata.get("source_type") or "")
    if source in ACADEMIC_SOURCES or source_type == "paper":
        return "preprint" if source == "arxiv" else "journalArticle"
    if source.startswith("rss:") or source_type in {"blog", "industry-analysis"}:
        return "blogPost"
    return "webpage"


def to_zotero_item(row: dict[str, Any], collection_key: str) -> dict[str, Any]:
    item_type = _item_type(row)
    authors = json.loads(row.get("authors_json") or "[]")
    creators = [_creator(author) for author in authors]
    creators = [creator for creator in creators if creator]
    topics = [
        token.partition(":")[0]
        for token in str(row.get("topics") or "").split(",")
        if token
    ]
    tags = [
        {"tag": "codex-research"},
        {"tag": f"source:{row.get('source') or 'unknown'}"},
    ]
    tags.extend({"tag": f"topic:{topic}"} for topic in sorted(set(topics)))
    extra_lines = [
        f"Codex Research Key: {row['canonical_key']}",
        f"Source: {row.get('source') or 'unknown'}",
    ]
    if row.get("arxiv_id"):
        extra_lines.append(f"arXiv: {row['arxiv_id']}")
    payload: dict[str, Any] = {
        "itemType": item_type,
        "title": normalize_space(row.get("title")),
        "creators": creators,
        "abstractNote": normalize_space(row.get("abstract")),
        "date": normalize_space(row.get("published_at"))[:10],
        "url": row.get("url") or row.get("canonical_url") or "",
        "language": "",
        "extra": "\n".join(extra_lines),
        "tags": tags,
        "collections": [collection_key],
        "relations": {},
    }
    if item_type == "journalArticle":
        payload["publicationTitle"] = normalize_space(row.get("container_title"))
        payload["DOI"] = normalize_doi(row.get("doi")) or ""
    elif item_type == "preprint":
        payload["repository"] = normalize_space(row.get("container_title")) or "arXiv"
        payload["DOI"] = normalize_doi(row.get("doi")) or ""
    elif item_type == "blogPost":
        payload["blogTitle"] = normalize_space(row.get("container_title"))
    else:
        payload["websiteTitle"] = normalize_space(row.get("container_title"))
    return payload


def sync_store_to_zotero(
    store: ResearchStore,
    client: ZoteroClient,
    *,
    collection_name: str,
    target_date: str | None = None,
    limit: int = 100,
) -> dict[str, Any]:
    candidates = store.zotero_candidates(target_date, limit)
    summary: dict[str, Any] = {
        "candidates": len(candidates),
        "linked_existing": 0,
        "created": 0,
        "failed": 0,
        "collection": collection_name,
    }
    if not candidates:
        return summary

    client.verify_access()
    existing_items = client.list_top_items()
    existing_index = build_existing_index(existing_items)
    collection_key = client.ensure_collection(collection_name)
    pending: list[dict[str, Any]] = []

    for row in candidates:
        existing = find_existing(row, existing_index)
        if existing:
            data = existing.get("data") or {}
            item_key = str(existing.get("key") or data.get("key") or "")
            version = existing.get("version") or data.get("version")
            store.record_zotero_link(
                row["id"],
                client.user_id,
                "linked_existing",
                zotero_item_key=item_key or None,
                zotero_version=int(version) if version is not None else None,
                collection_key=collection_key,
            )
            summary["linked_existing"] += 1
        else:
            pending.append(row)

    for offset in range(0, len(pending), 50):
        batch_rows = pending[offset : offset + 50]
        batch_payload = [to_zotero_item(row, collection_key) for row in batch_rows]
        try:
            response = client.create_items(batch_payload)
        except ZoteroError as exc:
            for row in batch_rows:
                store.record_zotero_link(
                    row["id"],
                    client.user_id,
                    "error",
                    collection_key=collection_key,
                    error=str(exc),
                )
                summary["failed"] += 1
            if exc.status_code == 429:
                summary["rate_limited"] = True
                summary["retry_after_seconds"] = exc.retry_after
                summary["deferred"] = len(pending) - offset - len(batch_rows)
                break
            continue

        failed = response.get("failed") or {}
        for index, row in enumerate(batch_rows):
            token = str(index)
            key = _created_key(response, token)
            if key:
                store.record_zotero_link(
                    row["id"],
                    client.user_id,
                    "created",
                    zotero_item_key=key,
                    zotero_version=_created_version(response, token),
                    collection_key=collection_key,
                )
                summary["created"] += 1
                continue
            error_entry = failed.get(token) or {}
            message = normalize_space(
                error_entry.get("message")
                if isinstance(error_entry, dict)
                else str(error_entry)
            )
            store.record_zotero_link(
                row["id"],
                client.user_id,
                "error",
                collection_key=collection_key,
                error=message or "Zotero did not return an item key.",
            )
            summary["failed"] += 1

    summary["completed_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return summary
