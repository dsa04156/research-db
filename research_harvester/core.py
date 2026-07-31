from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import unicodedata
from contextlib import contextmanager
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "ref",
    "source",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def local_date() -> str:
    return date.today().isoformat()


def load_config(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    with config_path.open(encoding="utf-8") as handle:
        config = json.load(handle)
    if not isinstance(config.get("topics"), list) or not config["topics"]:
        raise ValueError("config must contain at least one topic")
    return config


def normalize_space(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalize_title(value: str | None) -> str:
    text = unicodedata.normalize("NFKC", normalize_space(value)).casefold()
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def normalize_doi(value: str | None) -> str | None:
    if not value:
        return None
    doi = value.strip().casefold()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi)
    doi = re.sub(r"^doi:\s*", "", doi)
    return doi.rstrip(".,;)") or None


def normalize_arxiv_id(value: str | None) -> str | None:
    if not value:
        return None
    identifier = r"([a-z-]+(?:\.[a-z-]+)?/\d{7}|\d{4}\.\d{4,5})"
    explicit = re.search(
        rf"(?:arxiv:\s*|https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/)"
        rf"{identifier}(?:v\d+)?(?:\.pdf)?(?:[?#]|$)",
        value.strip(),
        flags=re.IGNORECASE,
    )
    if explicit:
        return explicit.group(1).casefold()
    bare = re.fullmatch(
        rf"{identifier}(?:v\d+)?(?:\.pdf)?",
        value.strip(),
        flags=re.IGNORECASE,
    )
    return bare.group(1).casefold() if bare else None


def item_arxiv_id(item: dict[str, Any]) -> str | None:
    for value in (item.get("arxiv_id"), item.get("source_id"), item.get("url")):
        normalized = normalize_arxiv_id(value)
        if normalized:
            return normalized
    return None


def canonicalize_url(value: str | None) -> str | None:
    if not value:
        return None
    try:
        parts = urlsplit(value.strip())
    except ValueError:
        return value.strip() or None
    if not parts.scheme or not parts.netloc:
        return value.strip() or None
    host = parts.netloc.casefold()
    if host.startswith("www."):
        host = host[4:]
    path = re.sub(r"/+", "/", parts.path or "/")
    if path != "/":
        path = path.rstrip("/")
    query = []
    for key, val in parse_qsl(parts.query, keep_blank_values=True):
        lowered = key.casefold()
        if lowered.startswith("utm_") or lowered in TRACKING_QUERY_KEYS:
            continue
        query.append((key, val))
    query.sort()
    return urlunsplit((parts.scheme.casefold(), host, path, urlencode(query), ""))


def extract_year(value: str | None) -> int | None:
    if not value:
        return None
    match = re.search(r"\b(19|20)\d{2}\b", value)
    return int(match.group(0)) if match else None


def first_author(authors: Iterable[str] | None) -> str:
    for author in authors or []:
        cleaned = normalize_title(author)
        if cleaned:
            return cleaned
    return ""


def content_hash(item: dict[str, Any]) -> str:
    material = "\n".join(
        [
            normalize_space(item.get("title")),
            normalize_space(item.get("abstract")),
            normalize_space(item.get("published_at")),
            normalize_space(item.get("updated_at")),
            canonicalize_url(item.get("url")) or "",
        ]
    )
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def identity_key(item: dict[str, Any]) -> str:
    doi = normalize_doi(item.get("doi"))
    if doi:
        return f"doi:{doi}"
    arxiv_id = item_arxiv_id(item)
    if arxiv_id:
        return f"arxiv:{arxiv_id}"
    canonical_url = canonicalize_url(item.get("url"))
    if canonical_url:
        digest = hashlib.sha256(canonical_url.encode("utf-8")).hexdigest()
        return f"url:{digest}"
    title = normalize_title(item.get("title"))
    authors = item.get("authors") or []
    year = extract_year(item.get("published_at"))
    material = f"{title}|{first_author(authors)}|{year or ''}"
    return f"title:{hashlib.sha256(material.encode('utf-8')).hexdigest()}"


def _phrase_score(phrase: str, title: str, body: str, title_weight: float, body_weight: float) -> float:
    token = unicodedata.normalize("NFKC", phrase).casefold().strip()
    if not token:
        return 0.0
    score = 0.0
    if token in title:
        score += title_weight
    if token in body:
        score += body_weight
    return score


def classify_item(
    item: dict[str, Any],
    config: dict[str, Any],
    topic_hints: Iterable[str] | None = None,
) -> list[dict[str, Any]]:
    title = unicodedata.normalize("NFKC", normalize_space(item.get("title"))).casefold()
    body = unicodedata.normalize(
        "NFKC",
        " ".join(
            [
                normalize_space(item.get("abstract")),
                normalize_space(item.get("container_title")),
                " ".join(item.get("subjects") or []),
            ]
        ),
    ).casefold()
    hints = set(topic_hints or item.get("topics") or [])
    explicit_score = item.get("relevance_score")
    trusted_hints = bool(item.get("trusted_topic_hints"))
    metadata = item.get("metadata") or {}
    lead_only = metadata.get("evidence_role") == "lead_only"
    matches: list[dict[str, Any]] = []
    for topic in config["topics"]:
        topic_id = topic["id"]
        trusted_hint = trusted_hints and topic_id in hints
        score = 2.5 if trusted_hint else (1.5 if topic_id in hints else 0.0)
        primary_matches = 0
        matched_terms: list[str] = []
        for keyword in topic.get("keywords", []):
            contribution = _phrase_score(keyword, title, body, 2.0, 0.8)
            if contribution:
                score += contribution
                primary_matches += 1
                matched_terms.append(keyword)
        for keyword in topic.get("boost_keywords", []):
            contribution = _phrase_score(keyword, title, body, 0.75, 0.3)
            if contribution:
                score += contribution
                matched_terms.append(keyword)
        for keyword in topic.get("exclude_keywords", []):
            if keyword.casefold() in title or keyword.casefold() in body:
                score -= 5.0
                matched_terms.append(f"-{keyword}")
        explicit_match = (
            explicit_score is not None
            and topic_id in hints
            and not lead_only
        )
        if explicit_match:
            score = max(score, float(explicit_score))
        if (
            score >= float(config.get("minimum_relevance_score", 2.0))
            and (primary_matches > 0 or trusted_hint or explicit_match)
        ):
            matches.append(
                {
                    "topic_id": topic_id,
                    "score": round(score, 3),
                    "matched_terms": sorted(set(matched_terms)),
                }
            )
    return sorted(matches, key=lambda row: row["score"], reverse=True)


SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    canonical_key TEXT NOT NULL UNIQUE,
    source TEXT NOT NULL,
    source_id TEXT,
    doi TEXT,
    arxiv_id TEXT,
    title TEXT NOT NULL,
    normalized_title TEXT NOT NULL,
    title_year INTEGER,
    url TEXT,
    canonical_url TEXT,
    abstract TEXT,
    authors_json TEXT NOT NULL DEFAULT '[]',
    container_title TEXT,
    published_at TEXT,
    updated_at TEXT,
    first_seen_at TEXT NOT NULL,
    first_seen_date TEXT NOT NULL,
    last_seen_at TEXT NOT NULL,
    last_seen_date TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    review_status TEXT NOT NULL DEFAULT 'pending',
    metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE INDEX IF NOT EXISTS idx_items_doi ON items(doi);
CREATE INDEX IF NOT EXISTS idx_items_arxiv ON items(arxiv_id);
CREATE INDEX IF NOT EXISTS idx_items_url ON items(canonical_url);
CREATE INDEX IF NOT EXISTS idx_items_title_year ON items(normalized_title, title_year);
CREATE INDEX IF NOT EXISTS idx_items_seen_date ON items(first_seen_date);

CREATE TABLE IF NOT EXISTS item_topics (
    item_id INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    topic_id TEXT NOT NULL,
    relevance_score REAL NOT NULL,
    matched_terms_json TEXT NOT NULL DEFAULT '[]',
    PRIMARY KEY(item_id, topic_id)
);

CREATE INDEX IF NOT EXISTS idx_item_topics_topic ON item_topics(topic_id, relevance_score DESC);

CREATE TABLE IF NOT EXISTS sightings (
    id INTEGER PRIMARY KEY,
    item_id INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    source TEXT NOT NULL,
    source_id TEXT,
    source_url TEXT,
    seen_at TEXT NOT NULL,
    seen_date TEXT NOT NULL,
    raw_hash TEXT NOT NULL,
    metadata_json TEXT NOT NULL DEFAULT '{}',
    UNIQUE(item_id, source, source_id, raw_hash)
);

CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY,
    started_at TEXT NOT NULL,
    finished_at TEXT,
    status TEXT NOT NULL,
    new_count INTEGER NOT NULL DEFAULT 0,
    updated_count INTEGER NOT NULL DEFAULT 0,
    duplicate_count INTEGER NOT NULL DEFAULT 0,
    filtered_count INTEGER NOT NULL DEFAULT 0,
    errors_json TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS zotero_links (
    item_id INTEGER PRIMARY KEY REFERENCES items(id) ON DELETE CASCADE,
    library_id TEXT NOT NULL,
    zotero_item_key TEXT,
    zotero_version INTEGER,
    collection_key TEXT,
    sync_status TEXT NOT NULL,
    last_attempt_at TEXT NOT NULL,
    synced_at TEXT,
    error TEXT
);

CREATE INDEX IF NOT EXISTS idx_zotero_links_status
ON zotero_links(sync_status, last_attempt_at);
"""


class ResearchStore:
    def __init__(self, database_path: str | Path):
        self.path = Path(database_path)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys=ON")
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(SCHEMA)
            sighting_columns = {
                row["name"]
                for row in connection.execute("PRAGMA table_info(sightings)").fetchall()
            }
            if "metadata_json" not in sighting_columns:
                connection.execute(
                    "ALTER TABLE sightings ADD COLUMN metadata_json TEXT NOT NULL DEFAULT '{}'"
                )

    def start_run(self) -> int:
        now = utc_now()
        with self.connect() as connection:
            cursor = connection.execute(
                "INSERT INTO runs(started_at, status) VALUES(?, 'running')",
                (now,),
            )
            return int(cursor.lastrowid)

    def finish_run(self, run_id: int, summary: dict[str, Any]) -> None:
        with self.connect() as connection:
            connection.execute(
                """
                UPDATE runs
                SET finished_at=?, status=?, new_count=?, updated_count=?,
                    duplicate_count=?, filtered_count=?, errors_json=?
                WHERE id=?
                """,
                (
                    utc_now(),
                    "completed_with_errors" if summary.get("errors") else "completed",
                    summary.get("new", 0),
                    summary.get("updated", 0),
                    summary.get("duplicate", 0),
                    summary.get("filtered", 0),
                    json.dumps(summary.get("errors", []), ensure_ascii=False),
                    run_id,
                ),
            )

    @staticmethod
    def _find_existing(connection: sqlite3.Connection, item: dict[str, Any]) -> sqlite3.Row | None:
        doi = normalize_doi(item.get("doi"))
        arxiv_id = item_arxiv_id(item)
        url = canonicalize_url(item.get("url"))
        title = normalize_title(item.get("title"))
        year = extract_year(item.get("published_at"))
        if doi:
            row = connection.execute("SELECT * FROM items WHERE doi=?", (doi,)).fetchone()
            if row:
                return row
        if arxiv_id:
            row = connection.execute("SELECT * FROM items WHERE arxiv_id=?", (arxiv_id,)).fetchone()
            if row:
                return row
        if url:
            row = connection.execute("SELECT * FROM items WHERE canonical_url=?", (url,)).fetchone()
            if row:
                return row
        if title and len(title) >= 20:
            if year:
                row = connection.execute(
                    """
                    SELECT * FROM items
                    WHERE normalized_title=?
                      AND (title_year IS NULL OR ABS(title_year - ?) <= 1)
                    ORDER BY id LIMIT 1
                    """,
                    (title, year),
                ).fetchone()
            else:
                row = connection.execute(
                    "SELECT * FROM items WHERE normalized_title=? ORDER BY id LIMIT 1",
                    (title,),
                ).fetchone()
            if row:
                return row
        return None

    def upsert(
        self,
        item: dict[str, Any],
        topic_matches: list[dict[str, Any]],
    ) -> str:
        if not normalize_space(item.get("title")):
            raise ValueError("item title is required")
        now = utc_now()
        today = local_date()
        item_hash = content_hash(item)
        doi = normalize_doi(item.get("doi"))
        arxiv_id = item_arxiv_id(item)
        canonical_url = canonicalize_url(item.get("url"))
        normalized_title = normalize_title(item.get("title"))
        year = extract_year(item.get("published_at"))
        authors = item.get("authors") or []
        metadata = item.get("metadata") or {}
        source = normalize_space(item.get("source")) or "unknown"
        source_id = normalize_space(item.get("source_id")) or None

        with self.connect() as connection:
            existing = self._find_existing(connection, item)
            if existing is None:
                cursor = connection.execute(
                    """
                    INSERT INTO items(
                        canonical_key, source, source_id, doi, arxiv_id, title,
                        normalized_title, title_year, url, canonical_url, abstract,
                        authors_json, container_title, published_at, updated_at,
                        first_seen_at, first_seen_date, last_seen_at, last_seen_date,
                        content_hash, metadata_json
                    ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """,
                    (
                        identity_key(item),
                        source,
                        source_id,
                        doi,
                        arxiv_id,
                        normalize_space(item.get("title")),
                        normalized_title,
                        year,
                        item.get("url"),
                        canonical_url,
                        normalize_space(item.get("abstract")),
                        json.dumps(authors, ensure_ascii=False),
                        normalize_space(item.get("container_title")),
                        normalize_space(item.get("published_at")),
                        normalize_space(item.get("updated_at")),
                        now,
                        today,
                        now,
                        today,
                        item_hash,
                        json.dumps(metadata, ensure_ascii=False),
                    ),
                )
                item_id = int(cursor.lastrowid)
                outcome = "new"
            else:
                item_id = int(existing["id"])
                existing_is_social = str(existing["source"] or "").startswith("social:")
                incoming_is_social = source.startswith("social:")
                social_sighting_only = incoming_is_social and not existing_is_social
                outcome = (
                    "duplicate"
                    if social_sighting_only or existing["content_hash"] == item_hash
                    else "updated"
                )
                old_abstract = existing["abstract"] or ""
                new_abstract = normalize_space(item.get("abstract"))
                best_abstract = (
                    old_abstract
                    if social_sighting_only
                    else new_abstract if len(new_abstract) > len(old_abstract) else old_abstract
                )
                old_authors = json.loads(existing["authors_json"] or "[]")
                best_authors = (
                    old_authors
                    if social_sighting_only
                    else authors if len(authors) > len(old_authors) else old_authors
                )
                old_metadata = json.loads(existing["metadata_json"] or "{}")
                merged_metadata = dict(old_metadata)
                if not (incoming_is_social and not existing_is_social):
                    merged_metadata.update(metadata)
                if not incoming_is_social:
                    merged_metadata.pop("evidence_role", None)
                    for key in (
                        "platform",
                        "engagement",
                        "last30days_query",
                        "last30days_schema_version",
                        "last30days_generated_at",
                        "last30days_cluster",
                        "last30days_relevance_score",
                    ):
                        merged_metadata.pop(key, None)
                incoming_key = identity_key(item)
                identity_rank = {"title": 0, "url": 1, "arxiv": 2, "doi": 3}
                existing_key_type = str(existing["canonical_key"]).partition(":")[0]
                incoming_key_type = incoming_key.partition(":")[0]
                promote_identity = (
                    existing_is_social and not incoming_is_social
                ) or identity_rank.get(incoming_key_type, 0) > identity_rank.get(
                    existing_key_type, 0
                )
                promoted_source = source if existing_is_social and not incoming_is_social else existing["source"]
                promoted_source_id = (
                    source_id if existing_is_social and not incoming_is_social else existing["source_id"]
                )
                connection.execute(
                    """
                    UPDATE items
                    SET canonical_key=?,
                        source=?,
                        source_id=?,
                        title=?,
                        normalized_title=?,
                        title_year=?,
                        doi=COALESCE(doi, ?),
                        arxiv_id=COALESCE(arxiv_id, ?),
                        url=CASE WHEN url IS NULL OR url='' THEN ? ELSE url END,
                        canonical_url=CASE WHEN canonical_url IS NULL OR canonical_url='' THEN ? ELSE canonical_url END,
                        abstract=?,
                        authors_json=?,
                        container_title=CASE WHEN container_title IS NULL OR container_title='' THEN ? ELSE container_title END,
                        published_at=CASE WHEN published_at IS NULL OR published_at='' THEN ? ELSE published_at END,
                        updated_at=CASE WHEN ? IS NOT NULL AND ? != '' THEN ? ELSE updated_at END,
                        last_seen_at=?,
                        last_seen_date=?,
                        content_hash=CASE WHEN ? != content_hash THEN ? ELSE content_hash END,
                        metadata_json=?
                    WHERE id=?
                    """,
                    (
                        incoming_key if promote_identity else existing["canonical_key"],
                        promoted_source,
                        promoted_source_id,
                        (
                            normalize_space(item.get("title"))
                            if promote_identity
                            else existing["title"]
                        ),
                        normalized_title if promote_identity else existing["normalized_title"],
                        year if promote_identity else existing["title_year"],
                        doi,
                        arxiv_id,
                        item.get("url"),
                        canonical_url,
                        best_abstract,
                        json.dumps(best_authors, ensure_ascii=False),
                        normalize_space(item.get("container_title")),
                        normalize_space(item.get("published_at")),
                        item.get("updated_at"),
                        item.get("updated_at"),
                        normalize_space(item.get("updated_at")),
                        now,
                        today,
                        existing["content_hash"] if social_sighting_only else item_hash,
                        existing["content_hash"] if social_sighting_only else item_hash,
                        json.dumps(merged_metadata, ensure_ascii=False),
                        item_id,
                    ),
                )

            raw_hash = hashlib.sha256(
                json.dumps(item, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")
            ).hexdigest()
            connection.execute(
                """
                INSERT OR IGNORE INTO sightings(
                    item_id, source, source_id, source_url, seen_at, seen_date,
                    raw_hash, metadata_json
                ) VALUES(?,?,?,?,?,?,?,?)
                """,
                (
                    item_id,
                    source,
                    source_id,
                    item.get("source_url") or item.get("url"),
                    now,
                    today,
                    raw_hash,
                    json.dumps(metadata, ensure_ascii=False),
                ),
            )
            for match in topic_matches:
                connection.execute(
                    """
                    INSERT INTO item_topics(item_id, topic_id, relevance_score, matched_terms_json)
                    VALUES(?,?,?,?)
                    ON CONFLICT(item_id, topic_id) DO UPDATE SET
                        relevance_score=MAX(item_topics.relevance_score, excluded.relevance_score),
                        matched_terms_json=excluded.matched_terms_json
                    """,
                    (
                        item_id,
                        match["topic_id"],
                        match["score"],
                        json.dumps(match.get("matched_terms", []), ensure_ascii=False),
                    ),
                )
            return outcome

    def items_for_date(self, target_date: str) -> list[sqlite3.Row]:
        with self.connect() as connection:
            return list(
                connection.execute(
                    """
                    SELECT i.*,
                           GROUP_CONCAT(it.topic_id || ':' || printf('%.1f', it.relevance_score), ',') AS topics
                    FROM items i
                    JOIN item_topics it ON it.item_id=i.id
                    WHERE i.first_seen_date=?
                      AND i.review_status NOT LIKE 'excluded_%'
                    GROUP BY i.id
                    ORDER BY MAX(it.relevance_score) DESC, COALESCE(i.published_at, '') DESC, i.id DESC
                    """,
                    (target_date,),
                )
            )

    def active_items(self) -> list[dict[str, Any]]:
        """Return every graph-worthy item with its topic and Zotero metadata."""
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT i.*,
                       GROUP_CONCAT(
                           it.topic_id || ':' || printf('%.1f', it.relevance_score), ','
                       ) AS topics,
                       MAX(it.relevance_score) AS max_relevance_score,
                       zl.zotero_item_key,
                       zl.sync_status AS zotero_sync_status
                FROM items i
                JOIN item_topics it ON it.item_id=i.id
                LEFT JOIN zotero_links zl ON zl.item_id=i.id
                WHERE i.review_status NOT LIKE 'excluded_%'
                GROUP BY i.id
                ORDER BY MAX(it.relevance_score) DESC,
                         COALESCE(i.published_at, '') DESC,
                         i.id DESC
                """
            ).fetchall()
        return [dict(row) for row in rows]

    def pending_items(self, target_date: str | None = None) -> list[dict[str, Any]]:
        clauses = ["i.review_status='pending'"]
        params: list[Any] = []
        if target_date:
            clauses.append("i.first_seen_date=?")
            params.append(target_date)
        with self.connect() as connection:
            rows = connection.execute(
                f"""
                SELECT i.*,
                       GROUP_CONCAT(it.topic_id || ':' || printf('%.1f', it.relevance_score), ',') AS topics
                FROM items i
                JOIN item_topics it ON it.item_id=i.id
                WHERE {' AND '.join(clauses)}
                GROUP BY i.id
                ORDER BY MAX(it.relevance_score) DESC, i.id DESC
                """,
                params,
            ).fetchall()
        return [dict(row) for row in rows]

    def zotero_candidates(
        self,
        target_date: str | None = None,
        limit: int = 100,
    ) -> list[dict[str, Any]]:
        clauses = [
            "i.review_status NOT LIKE 'excluded_%'",
            "(zl.item_id IS NULL OR zl.sync_status='error')",
            "COALESCE(json_extract(i.metadata_json, '$.evidence_role'), '') != 'lead_only'",
        ]
        params: list[Any] = []
        if target_date:
            clauses.append("i.first_seen_date=?")
            params.append(target_date)
        params.append(max(1, int(limit)))
        with self.connect() as connection:
            rows = connection.execute(
                f"""
                SELECT i.*,
                       GROUP_CONCAT(
                           it.topic_id || ':' || printf('%.1f', it.relevance_score), ','
                       ) AS topics,
                       MAX(it.relevance_score) AS max_relevance_score
                FROM items i
                JOIN item_topics it ON it.item_id=i.id
                LEFT JOIN zotero_links zl ON zl.item_id=i.id
                WHERE {' AND '.join(clauses)}
                GROUP BY i.id
                ORDER BY MAX(it.relevance_score) DESC,
                         COALESCE(i.published_at, '') DESC,
                         i.id DESC
                LIMIT ?
                """,
                params,
            ).fetchall()
        return [dict(row) for row in rows]

    def record_zotero_link(
        self,
        item_id: int,
        library_id: str,
        status: str,
        zotero_item_key: str | None = None,
        zotero_version: int | None = None,
        collection_key: str | None = None,
        error: str | None = None,
    ) -> None:
        now = utc_now()
        synced_at = now if status in {"created", "linked_existing"} else None
        with self.connect() as connection:
            connection.execute(
                """
                INSERT INTO zotero_links(
                    item_id, library_id, zotero_item_key, zotero_version,
                    collection_key, sync_status, last_attempt_at, synced_at, error
                ) VALUES(?,?,?,?,?,?,?,?,?)
                ON CONFLICT(item_id) DO UPDATE SET
                    library_id=excluded.library_id,
                    zotero_item_key=COALESCE(
                        excluded.zotero_item_key, zotero_links.zotero_item_key
                    ),
                    zotero_version=COALESCE(
                        excluded.zotero_version, zotero_links.zotero_version
                    ),
                    collection_key=COALESCE(
                        excluded.collection_key, zotero_links.collection_key
                    ),
                    sync_status=excluded.sync_status,
                    last_attempt_at=excluded.last_attempt_at,
                    synced_at=COALESCE(excluded.synced_at, zotero_links.synced_at),
                    error=excluded.error
                """,
                (
                    int(item_id),
                    str(library_id),
                    zotero_item_key,
                    zotero_version,
                    collection_key,
                    status,
                    now,
                    synced_at,
                    error,
                ),
            )

    def zotero_status(self) -> dict[str, Any]:
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT sync_status, COUNT(*) AS item_count, MAX(last_attempt_at) AS last_attempt_at
                FROM zotero_links
                GROUP BY sync_status
                ORDER BY item_count DESC
                """
            ).fetchall()
            unsynced = connection.execute(
                """
                SELECT COUNT(*) AS item_count
                FROM items i
                WHERE i.review_status NOT LIKE 'excluded_%'
                  AND COALESCE(
                      json_extract(i.metadata_json, '$.evidence_role'), ''
                  ) != 'lead_only'
                  AND NOT EXISTS (
                      SELECT 1 FROM zotero_links zl
                      WHERE zl.item_id=i.id
                        AND zl.sync_status IN ('created', 'linked_existing')
                  )
                """
            ).fetchone()
        return {
            "linked": [dict(row) for row in rows],
            "unsynced": int(unsynced["item_count"] or 0),
        }

    def reclassify(self, config: dict[str, Any]) -> dict[str, int]:
        """Re-apply current topic rules without deleting historical records."""
        cutoff = date.today() + timedelta(days=1)
        summary = {"active": 0, "excluded_irrelevant": 0, "excluded_future": 0}
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT i.*,
                       GROUP_CONCAT(it.topic_id, ',') AS topic_hints
                FROM items i
                LEFT JOIN item_topics it ON it.item_id=i.id
                GROUP BY i.id
                ORDER BY i.id
                """
            ).fetchall()
            for row in rows:
                hints = [value for value in (row["topic_hints"] or "").split(",") if value]
                metadata = json.loads(row["metadata_json"] or "{}")
                item = {
                    "source": row["source"],
                    "source_id": row["source_id"],
                    "title": row["title"],
                    "url": row["url"],
                    "abstract": row["abstract"],
                    "authors": json.loads(row["authors_json"] or "[]"),
                    "container_title": row["container_title"],
                    "published_at": row["published_at"],
                    "updated_at": row["updated_at"],
                    "topics": hints,
                    "trusted_topic_hints": (
                        row["source"] == "github-release"
                        or bool(metadata.get("trusted_topic_hints"))
                    ),
                }
                if row["source"] == "seed":
                    item["relevance_score"] = 10.0
                matches = classify_item(item, config, hints)

                published_day = str(row["published_at"] or "")[:10]
                is_future = False
                if re.fullmatch(r"\d{4}-\d{2}-\d{2}", published_day):
                    try:
                        is_future = date.fromisoformat(published_day) > cutoff
                    except ValueError:
                        pass

                if is_future:
                    status = "excluded_future"
                elif not matches:
                    status = "excluded_irrelevant"
                else:
                    status = (
                        "pending"
                        if str(row["review_status"]).startswith("excluded_")
                        else row["review_status"]
                    )

                if matches:
                    connection.execute("DELETE FROM item_topics WHERE item_id=?", (row["id"],))
                    for match in matches:
                        connection.execute(
                            """
                            INSERT INTO item_topics(
                                item_id, topic_id, relevance_score, matched_terms_json
                            ) VALUES(?,?,?,?)
                            """,
                            (
                                row["id"],
                                match["topic_id"],
                                match["score"],
                                json.dumps(match.get("matched_terms", []), ensure_ascii=False),
                            ),
                        )
                connection.execute(
                    "UPDATE items SET review_status=? WHERE id=?",
                    (status, row["id"]),
                )
                if status.startswith("excluded_"):
                    summary[status] += 1
                else:
                    summary["active"] += 1
        return summary

    def status(self) -> dict[str, Any]:
        with self.connect() as connection:
            counts = connection.execute(
                """
                SELECT
                    COUNT(*) AS items,
                    SUM(CASE WHEN review_status='pending' THEN 1 ELSE 0 END) AS pending,
                    SUM(CASE WHEN review_status LIKE 'excluded_%' THEN 1 ELSE 0 END) AS excluded,
                    MIN(first_seen_at) AS first_seen,
                    MAX(last_seen_at) AS last_seen
                FROM items
                """
            ).fetchone()
            topics = connection.execute(
                """
                SELECT topic_id, COUNT(*) AS item_count, MAX(relevance_score) AS max_score
                FROM item_topics it
                JOIN items i ON i.id=it.item_id
                WHERE i.review_status NOT LIKE 'excluded_%'
                GROUP BY topic_id ORDER BY item_count DESC
                """
            ).fetchall()
            sources = connection.execute(
                """
                SELECT source, COUNT(*) AS item_count
                FROM items
                WHERE review_status NOT LIKE 'excluded_%'
                GROUP BY source ORDER BY item_count DESC
                """
            ).fetchall()
            publication_years = connection.execute(
                """
                SELECT
                    CASE
                        WHEN published_at GLOB '[0-9][0-9][0-9][0-9]*'
                            THEN SUBSTR(published_at, 1, 4)
                        ELSE 'unknown'
                    END AS publication_year,
                    COUNT(*) AS item_count
                FROM items
                WHERE review_status NOT LIKE 'excluded_%'
                GROUP BY publication_year
                ORDER BY publication_year DESC
                """
            ).fetchall()
            sighting_count = connection.execute(
                "SELECT COUNT(*) AS count FROM sightings"
            ).fetchone()
            sighting_metadata = connection.execute(
                "SELECT metadata_json FROM sightings"
            ).fetchall()
            last_run = connection.execute(
                "SELECT * FROM runs ORDER BY id DESC LIMIT 1"
            ).fetchone()
            zotero_rows = connection.execute(
                """
                SELECT sync_status, COUNT(*) AS item_count
                FROM zotero_links
                GROUP BY sync_status
                ORDER BY item_count DESC
                """
            ).fetchall()
        social_platforms: dict[str, int] = {}
        social_signals = 0
        for row in sighting_metadata:
            try:
                metadata = json.loads(row["metadata_json"] or "{}")
            except json.JSONDecodeError:
                continue
            if metadata.get("evidence_role") != "lead_only":
                continue
            social_signals += 1
            platform = normalize_space(str(metadata.get("platform") or "unknown")).casefold()
            social_platforms[platform] = social_platforms.get(platform, 0) + 1

        return {
            "database": str(self.path.resolve()),
            "items": int(counts["items"] or 0),
            "pending": int(counts["pending"] or 0),
            "excluded": int(counts["excluded"] or 0),
            "first_seen": counts["first_seen"],
            "last_seen": counts["last_seen"],
            "topics": [dict(row) for row in topics],
            "sources": [dict(row) for row in sources],
            "publication_years": [dict(row) for row in publication_years],
            "sightings": int(sighting_count["count"] or 0),
            "social_signals": social_signals,
            "social_platforms": [
                {"platform": platform, "sighting_count": count}
                for platform, count in sorted(
                    social_platforms.items(), key=lambda pair: (-pair[1], pair[0])
                )
            ],
            "zotero": [dict(row) for row in zotero_rows],
            "last_run": dict(last_run) if last_run else None,
        }
