from __future__ import annotations

import hashlib
from typing import Any, Iterable

from .core import normalize_space


def _reports(payload: dict[str, Any]) -> Iterable[dict[str, Any]]:
    if isinstance(payload.get("results"), list):
        yield payload
        return
    for entry in payload.get("reports") or []:
        report = entry.get("report") if isinstance(entry, dict) else None
        if isinstance(report, dict):
            yield report


def _source_id(result: dict[str, Any]) -> str:
    candidate_id = normalize_space(str(result.get("candidate_id") or ""))
    if candidate_id:
        return candidate_id
    material = normalize_space(str(result.get("url") or result.get("title") or ""))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:24]


def items_from_last30days_agent(
    payload: dict[str, Any],
    config: dict[str, Any],
    topic_hints: list[str],
) -> list[dict[str, Any]]:
    """Convert stable last30days agent JSON into lead-only DB items.

    A caller may add ``primary_url`` to a result after following an outbound
    link. In that case the primary URL becomes the canonical item URL while
    the social post remains the sighting URL.
    """

    social_config = config.get("social_research") or {}
    minimum_relevance = float(social_config.get("minimum_result_relevance", 0.45))
    excluded = {
        str(value).strip().casefold()
        for value in social_config.get("excluded_platforms") or []
    }
    platform_config = {
        str(entry.get("id") or "").casefold(): entry
        for entry in social_config.get("platforms") or []
        if isinstance(entry, dict) and entry.get("id")
    }
    items: list[dict[str, Any]] = []

    for report in _reports(payload):
        query = normalize_space(str(report.get("query") or payload.get("query") or ""))
        generated_at = normalize_space(
            str(report.get("generated_at") or payload.get("generated_at") or "")
        )
        schema_version = report.get("schema_version") or payload.get("schema_version")
        for result in report.get("results") or []:
            if not isinstance(result, dict):
                continue
            platform = normalize_space(str(result.get("source") or "")).casefold()
            if not platform or platform in excluded or platform not in platform_config:
                continue
            try:
                relevance = float(result.get("relevance_score") or 0.0)
            except (TypeError, ValueError):
                relevance = 0.0
            if relevance < minimum_relevance:
                continue
            title = normalize_space(str(result.get("title") or ""))
            social_url = normalize_space(str(result.get("url") or ""))
            if not title or not social_url:
                continue
            primary_url = normalize_space(str(result.get("primary_url") or "")) or social_url
            platform_policy = platform_config[platform]
            metadata = {
                "source_type": "social-post",
                "evidence_role": "lead_only",
                "platform": platform,
                "quality_tier": platform_policy.get("quality_tier", "E"),
                "engagement": result.get("engagement") or {},
                "last30days_query": query,
                "last30days_schema_version": schema_version,
                "last30days_generated_at": generated_at,
                "last30days_cluster": result.get("cluster"),
                "last30days_relevance_score": relevance,
            }
            items.append(
                {
                    "source": f"social:{platform}",
                    "source_id": _source_id(result),
                    "title": title,
                    "url": primary_url,
                    "source_url": social_url,
                    "abstract": normalize_space(str(result.get("summary") or "")),
                    "authors": [],
                    "published_at": normalize_space(
                        str(result.get("published_at") or "")
                    ),
                    "topics": list(topic_hints),
                    "relevance_score": round(2.0 + 3.0 * min(1.0, relevance), 3),
                    "metadata": metadata,
                }
            )
    return items
