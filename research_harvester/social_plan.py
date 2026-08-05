from __future__ import annotations

import re
import unicodedata
from typing import Any

from .core import normalize_space


PLATFORM_QUERY_WORD_LIMITS = {
    # ScrapeCreators' Threads search is reliable only for short queries. The
    # upstream adapter also truncates to two words, so make that transformation
    # explicit and observable in our own plan.
    "threads": 2,
}


def _slug(value: str) -> str:
    text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").casefold()
    return text or "social-query"


def _compact_query(value: str, platform: str) -> tuple[str, bool]:
    normalized = normalize_space(value)
    word_limit = PLATFORM_QUERY_WORD_LIMITS.get(platform)
    if not word_limit:
        return normalized, False
    words = normalized.split()
    compacted = " ".join(words[:word_limit])
    return compacted, compacted != normalized


def build_social_plan(
    config: dict[str, Any],
    platform: str,
) -> dict[str, Any]:
    """Build deterministic, platform-specific social search runs.

    Long cross-platform research prompts are poor inputs for short-query social
    APIs. ``platform_queries`` lets the repository preserve multiple deliberate
    search angles instead of letting a provider silently keep the first words.
    """

    social_config = config.get("social_research") or {}
    normalized_platform = normalize_space(platform).casefold()
    configured_platforms = {
        normalize_space(str(entry.get("id") or "")).casefold()
        for entry in social_config.get("platforms") or []
        if isinstance(entry, dict) and entry.get("id")
    }
    if normalized_platform not in configured_platforms:
        raise ValueError(f"unknown social platform: {platform}")

    excluded = {
        normalize_space(str(value)).casefold()
        for value in social_config.get("excluded_platforms") or []
    }
    if normalized_platform in excluded:
        return {
            "schema_version": "1.0",
            "platform": normalized_platform,
            "excluded": True,
            "queries": [],
        }

    runs: list[dict[str, Any]] = []
    run_by_query: dict[str, dict[str, Any]] = {}

    def add_run(
        *,
        name: str,
        raw_query: str,
        topic_hints: list[str],
        query_kind: str,
    ) -> None:
        query, compacted = _compact_query(raw_query, normalized_platform)
        if not query:
            return
        normalized_topics = tuple(
            dict.fromkeys(
                normalize_space(str(topic)).casefold()
                for topic in topic_hints
                if normalize_space(str(topic))
            )
        )
        dedupe_key = query.casefold()
        if dedupe_key in run_by_query:
            existing = run_by_query[dedupe_key]
            existing["topic_hints"] = list(
                dict.fromkeys([*existing["topic_hints"], *normalized_topics])
            )
            if existing["query_kind"] != query_kind:
                existing["query_kind"] = "merged"
            return
        run_name = normalize_space(name) or query
        run = {
            "name": run_name,
            "slug": _slug(f"{normalized_platform}-{run_name}-{query}"),
            "platform": normalized_platform,
            "query": query,
            "raw_query": normalize_space(raw_query),
            "query_kind": query_kind,
            "compacted": compacted,
            "topic_hints": list(normalized_topics),
        }
        runs.append(run)
        run_by_query[dedupe_key] = run

    for entry in social_config.get("queries") or []:
        if not isinstance(entry, dict):
            continue
        base_query = normalize_space(str(entry.get("query") or ""))
        topic_hints = list(entry.get("topic_hints") or [])
        platform_queries = entry.get("platform_queries") or {}
        variants = platform_queries.get(normalized_platform)
        if isinstance(variants, str):
            variants = [variants]
        if not isinstance(variants, list) or not variants:
            variants = [base_query]
            query_kind = "base"
        else:
            query_kind = "platform_variant"
        for index, variant in enumerate(variants, start=1):
            add_run(
                name=f"{entry.get('name') or base_query} {index}",
                raw_query=str(variant),
                topic_hints=topic_hints,
                query_kind=query_kind,
            )

    for entry in social_config.get("watch_queries") or []:
        if not isinstance(entry, dict):
            continue
        watch_platforms = entry.get("platforms") or [entry.get("platform")]
        normalized_watch_platforms = {
            normalize_space(str(value)).casefold()
            for value in watch_platforms
            if value
        }
        if normalized_platform not in normalized_watch_platforms:
            continue
        add_run(
            name=str(entry.get("name") or entry.get("query") or "watch"),
            raw_query=str(entry.get("query") or ""),
            topic_hints=list(entry.get("topic_hints") or []),
            query_kind="watch",
        )

    return {
        "schema_version": "1.0",
        "platform": normalized_platform,
        "excluded": False,
        "queries": runs,
    }
