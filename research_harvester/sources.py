from __future__ import annotations

import json
import os
import re
import time
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from .core import normalize_arxiv_id, normalize_space


ATOM = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def _strip_html(value: str | None) -> str:
    text = re.sub(r"<[^>]+>", " ", value or "")
    return normalize_space(unescape(text))


def _request(url: str, config: dict[str, Any], headers: dict[str, str] | None = None) -> bytes:
    merged = {
        "User-Agent": config.get("user_agent", "personal-research-harvester/1.0"),
        "Accept": "*/*",
    }
    if headers:
        merged.update(headers)
    request = Request(url, headers=merged)
    timeout = int(config.get("request_timeout_seconds", 30))
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urlopen(request, timeout=timeout) as response:
                return response.read()
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(1.5 * (attempt + 1))
    assert last_error is not None
    raise last_error


def _json_request(url: str, config: dict[str, Any], headers: dict[str, str] | None = None) -> Any:
    return json.loads(_request(url, config, headers).decode("utf-8"))


def _iso_date_from_parts(parts: Any) -> str | None:
    if not isinstance(parts, list) or not parts or not isinstance(parts[0], list):
        return None
    values = parts[0]
    if not values:
        return None
    year = int(values[0])
    month = int(values[1]) if len(values) > 1 else 1
    day = int(values[2]) if len(values) > 2 else 1
    return date(year, month, day).isoformat()


def _within_window(
    value: str | None,
    since: date,
    until: date | None = None,
) -> bool:
    """Reject stale records and implausible future publication dates."""
    if not value or not re.match(r"\d{4}-\d{2}-\d{2}", value):
        return True
    try:
        published = date.fromisoformat(value[:10])
    except ValueError:
        return True
    upper_bound = until or date.today() + timedelta(days=1)
    return since <= published <= upper_bound


def _abstract_from_inverted_index(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    positioned: list[tuple[int, str]] = []
    for word, positions in index.items():
        if not isinstance(positions, list):
            continue
        positioned.extend((int(position), word) for position in positions)
    positioned.sort()
    return normalize_space(" ".join(word for _, word in positioned))


def collect_arxiv(
    topic: dict[str, Any],
    config: dict[str, Any],
    since: date,
    until: date | None = None,
) -> list[dict[str, Any]]:
    upper_bound = until or date.today() + timedelta(days=1)
    dated_query = (
        f"({topic['arxiv_query']}) AND "
        f"submittedDate:[{since.strftime('%Y%m%d')}0000 TO "
        f"{upper_bound.strftime('%Y%m%d')}2359]"
    )
    params = {
        "search_query": dated_query,
        "start": 0,
        "max_results": int(config.get("max_results_per_query", 20)),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = "https://export.arxiv.org/api/query?" + urlencode(params)
    root = ET.fromstring(_request(url, config))
    results: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", ATOM):
        published = normalize_space(entry.findtext("atom:published", default="", namespaces=ATOM))
        published_date = published[:10] if published else None
        if not _within_window(published_date, since, upper_bound):
            continue
        entry_id = normalize_space(entry.findtext("atom:id", default="", namespaces=ATOM))
        arxiv_id = normalize_arxiv_id(entry_id)
        links = {
            link.attrib.get("type", link.attrib.get("rel", "")): link.attrib.get("href")
            for link in entry.findall("atom:link", ATOM)
        }
        authors = [
            normalize_space(author.findtext("atom:name", default="", namespaces=ATOM))
            for author in entry.findall("atom:author", ATOM)
        ]
        categories = [node.attrib.get("term", "") for node in entry.findall("atom:category", ATOM)]
        results.append(
            {
                "source": "arxiv",
                "source_id": arxiv_id or entry_id,
                "arxiv_id": arxiv_id,
                "doi": normalize_space(entry.findtext("arxiv:doi", default="", namespaces=ATOM)) or None,
                "title": normalize_space(entry.findtext("atom:title", default="", namespaces=ATOM)),
                "url": links.get("text/html") or entry_id,
                "abstract": normalize_space(entry.findtext("atom:summary", default="", namespaces=ATOM)),
                "authors": [author for author in authors if author],
                "published_at": published,
                "updated_at": normalize_space(entry.findtext("atom:updated", default="", namespaces=ATOM)),
                "subjects": categories,
                "container_title": "arXiv",
                "metadata": {
                    "categories": categories,
                    "pdf_url": links.get("application/pdf"),
                    "source_type": "paper",
                    "quality_tier": "A",
                },
                "topics": [topic["id"]],
            }
        )
    return results


def collect_crossref(
    topic: dict[str, Any],
    config: dict[str, Any],
    since: date,
    until: date | None = None,
) -> list[dict[str, Any]]:
    upper_bound = until or date.today() + timedelta(days=1)
    params = {
        "query": topic["search_query"],
        "filter": (
            f"from-pub-date:{since.isoformat()},"
            f"until-pub-date:{upper_bound.isoformat()}"
        ),
        "sort": "published",
        "order": "desc",
        "rows": int(config.get("max_results_per_query", 20)),
        "select": "DOI,title,author,published,published-online,published-print,URL,abstract,container-title,type,created,subject",
    }
    mailto = os.environ.get("CROSSREF_MAILTO")
    if mailto:
        params["mailto"] = mailto
    url = "https://api.crossref.org/works?" + urlencode(params)
    payload = _json_request(url, config)
    results: list[dict[str, Any]] = []
    for work in payload.get("message", {}).get("items", []):
        title = normalize_space(" ".join(work.get("title") or []))
        if not title:
            continue
        published = (
            _iso_date_from_parts((work.get("published-online") or {}).get("date-parts"))
            or _iso_date_from_parts((work.get("published-print") or {}).get("date-parts"))
            or _iso_date_from_parts((work.get("published") or {}).get("date-parts"))
        )
        if not _within_window(published, since, upper_bound):
            continue
        authors = []
        for author in work.get("author") or []:
            name = normalize_space(
                " ".join([author.get("given", ""), author.get("family", "")])
            )
            if name:
                authors.append(name)
        results.append(
            {
                "source": "crossref",
                "source_id": work.get("DOI") or work.get("URL"),
                "doi": work.get("DOI"),
                "title": title,
                "url": work.get("URL"),
                "abstract": _strip_html(work.get("abstract")),
                "authors": authors,
                "published_at": published,
                "updated_at": _iso_date_from_parts((work.get("created") or {}).get("date-parts")),
                "subjects": work.get("subject") or [],
                "container_title": normalize_space(" ".join(work.get("container-title") or [])),
                "metadata": {
                    "type": work.get("type"),
                    "source_type": "paper",
                    "quality_tier": "A",
                },
                "topics": [topic["id"]],
            }
        )
    return results


def collect_openalex(
    topic: dict[str, Any],
    config: dict[str, Any],
    since: date,
    until: date | None = None,
) -> list[dict[str, Any]]:
    upper_bound = until or date.today() + timedelta(days=1)
    params = {
        "search": topic["search_query"],
        "filter": (
            f"from_publication_date:{since.isoformat()},"
            f"to_publication_date:{upper_bound.isoformat()}"
        ),
        "sort": "publication_date:desc",
        "per-page": int(config.get("max_results_per_query", 20)),
        "select": "id,doi,display_name,publication_date,primary_location,authorships,abstract_inverted_index,type,topics,updated_date",
    }
    api_key = os.environ.get("OPENALEX_API_KEY")
    if api_key:
        params["api_key"] = api_key
    mailto = os.environ.get("CROSSREF_MAILTO")
    if mailto:
        params["mailto"] = mailto
    url = "https://api.openalex.org/works?" + urlencode(params)
    payload = _json_request(url, config)
    results: list[dict[str, Any]] = []
    for work in payload.get("results", []):
        if not _within_window(work.get("publication_date"), since, upper_bound):
            continue
        location = work.get("primary_location") or {}
        source = location.get("source") or {}
        authors = [
            normalize_space((authorship.get("author") or {}).get("display_name"))
            for authorship in work.get("authorships") or []
        ]
        topics = [
            normalize_space(topic_row.get("display_name"))
            for topic_row in work.get("topics") or []
        ]
        results.append(
            {
                "source": "openalex",
                "source_id": work.get("id"),
                "doi": work.get("doi"),
                "title": normalize_space(work.get("display_name")),
                "url": location.get("landing_page_url") or work.get("id"),
                "abstract": _abstract_from_inverted_index(work.get("abstract_inverted_index")),
                "authors": [author for author in authors if author],
                "published_at": work.get("publication_date"),
                "updated_at": work.get("updated_date"),
                "subjects": [value for value in topics if value],
                "container_title": normalize_space(source.get("display_name")),
                "metadata": {
                    "type": work.get("type"),
                    "source_type": "paper",
                    "quality_tier": "A",
                },
                "topics": [topic["id"]],
            }
        )
    return results


def _parse_feed_date(value: str | None) -> str | None:
    if not value:
        return None
    cleaned = normalize_space(value)
    try:
        return parsedate_to_datetime(cleaned).astimezone(timezone.utc).isoformat()
    except (TypeError, ValueError, OverflowError):
        pass
    try:
        return datetime.fromisoformat(cleaned.replace("Z", "+00:00")).isoformat()
    except ValueError:
        return cleaned


def _entry_link(entry: ET.Element) -> str | None:
    direct = entry.findtext("link")
    if direct:
        return normalize_space(direct)
    for link in entry.findall("{http://www.w3.org/2005/Atom}link"):
        href = link.attrib.get("href")
        if href and link.attrib.get("rel", "alternate") == "alternate":
            return href
    return None


def collect_feed(
    feed: dict[str, Any],
    config: dict[str, Any],
    since: date,
    until: date | None = None,
) -> list[dict[str, Any]]:
    root = ET.fromstring(_request(feed["url"], config))
    entries = root.findall(".//item")
    if not entries:
        entries = root.findall(".//{http://www.w3.org/2005/Atom}entry")
    results: list[dict[str, Any]] = []
    for entry in entries:
        atom = "{http://www.w3.org/2005/Atom}"
        title = normalize_space(entry.findtext("title") or entry.findtext(f"{atom}title"))
        link = _entry_link(entry)
        guid = normalize_space(entry.findtext("guid") or entry.findtext(f"{atom}id"))
        raw_date = (
            entry.findtext("pubDate")
            or entry.findtext(f"{atom}published")
            or entry.findtext(f"{atom}updated")
        )
        published = _parse_feed_date(raw_date)
        published_day = published[:10] if published and re.match(r"\d{4}-\d{2}-\d{2}", published) else None
        if not _within_window(published_day, since, until):
            continue
        description = (
            entry.findtext("description")
            or entry.findtext(f"{atom}summary")
            or entry.findtext(f"{atom}content")
        )
        results.append(
            {
                "source": f"rss:{feed['name']}",
                "source_id": guid or link,
                "title": title,
                "url": link,
                "abstract": _strip_html(description),
                "authors": [],
                "published_at": published,
                "updated_at": published,
                "container_title": feed["name"],
                "metadata": {
                    "feed_url": feed["url"],
                    "source_type": feed.get("source_type", "blog"),
                    "quality_tier": feed.get("quality_tier", "B"),
                    "trusted_topic_hints": bool(
                        feed.get("trusted_topic_hints", False)
                    ),
                },
                "topics": feed.get("topic_hints", []),
                "trusted_topic_hints": bool(
                    feed.get("trusted_topic_hints", False)
                ),
            }
        )
    return results


def collect_github_releases(
    repository: dict[str, Any],
    config: dict[str, Any],
    since: date,
    until: date | None = None,
) -> list[dict[str, Any]]:
    repo = repository["repo"]
    url = f"https://api.github.com/repos/{quote(repo, safe='/')}/releases?per_page=10"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    payload = _json_request(url, config, headers)
    results: list[dict[str, Any]] = []
    for release in payload:
        published = release.get("published_at") or release.get("created_at")
        if not _within_window(published[:10] if published else None, since, until):
            continue
        name = normalize_space(release.get("name") or release.get("tag_name"))
        results.append(
            {
                "source": "github-release",
                "source_id": str(release.get("id") or release.get("node_id")),
                "title": f"{repo} {name}",
                "url": release.get("html_url"),
                "abstract": _strip_html(release.get("body")),
                "authors": [normalize_space((release.get("author") or {}).get("login"))],
                "published_at": published,
                "updated_at": release.get("updated_at") or published,
                "container_title": repo,
                "metadata": {
                    "repo": repo,
                    "tag_name": release.get("tag_name"),
                    "prerelease": bool(release.get("prerelease")),
                    "source_type": "project-release",
                    "quality_tier": "A",
                },
                "topics": repository.get("topic_hints", []),
                "trusted_topic_hints": True,
            }
        )
    return results


def collect_all(
    config: dict[str, Any],
    days: int,
    since_date: date | None = None,
    until_date: date | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    since = since_date or date.today() - timedelta(days=days)
    until = until_date or date.today() + timedelta(days=1)
    results: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    for index, topic in enumerate(config["topics"]):
        collectors = (
            ("arxiv", collect_arxiv),
            ("crossref", collect_crossref),
            ("openalex", collect_openalex),
        )
        for source_name, collector in collectors:
            try:
                results.extend(collector(topic, config, since, until))
            except Exception as exc:  # Each source degrades independently.
                errors.append(
                    {
                        "source": source_name,
                        "target": topic["id"],
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                )
        if index < len(config["topics"]) - 1:
            time.sleep(3)

    for feed in config.get("feeds", []):
        if feed.get("enabled", True) is False:
            continue
        try:
            results.extend(collect_feed(feed, config, since, until))
        except Exception as exc:
            errors.append(
                {
                    "source": "rss",
                    "target": feed["name"],
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )

    for repository in config.get("github_repositories", []):
        try:
            results.extend(collect_github_releases(repository, config, since, until))
        except Exception as exc:
            errors.append(
                {
                    "source": "github-release",
                    "target": repository["repo"],
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )

    return results, errors
