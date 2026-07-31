from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .core import ResearchStore, normalize_space
from .obsidian import source_note_wikilink


def _shorten(value: str | None, limit: int = 360) -> str:
    text = normalize_space(value)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def write_digest(
    store: ResearchStore,
    config: dict[str, Any],
    target_date: str,
    output_directory: str | Path,
    research_directory: str | Path = "vault",
) -> Path:
    rows = store.items_for_date(target_date)
    manifest_path = Path(output_directory).parent / ".research-graph-manifest.json"
    manifest: dict[str, str] = {}
    if manifest_path.exists():
        try:
            payload = json.loads(manifest_path.read_text(encoding="utf-8"))
            if isinstance(payload, dict) and isinstance(payload.get("items"), dict):
                manifest = {
                    str(key): str(value)
                    for key, value in payload["items"].items()
                    if isinstance(value, str)
                }
        except (OSError, json.JSONDecodeError):
            manifest = {}
    max_per_topic = max(1, int(config.get("digest_max_per_topic", 20)))
    topic_names = {topic["id"]: topic["name"] for topic in config["topics"]}
    by_topic: dict[str, list[Any]] = {topic["id"]: [] for topic in config["topics"]}
    for row in rows:
        topic_values = []
        for token in (row["topics"] or "").split(","):
            if not token:
                continue
            topic_id, _, raw_score = token.partition(":")
            try:
                score = float(raw_score)
            except ValueError:
                score = 0.0
            topic_values.append((topic_id, score))
        topic_values.sort(key=lambda pair: pair[1], reverse=True)
        if topic_values:
            by_topic.setdefault(topic_values[0][0], []).append(row)

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"{target_date}.md"
    lines = [
        "---",
        f"date: {target_date}",
        "type: daily-research-digest",
        f"new_items: {len(rows)}",
        "codex_reviewed: false",
        "---",
        "",
        f"# Daily Research Digest - {target_date}",
        "",
        f"새로 수집된 고유 자료: **{len(rows)}개**",
        "",
        "> 동일 DOI, arXiv ID, URL 또는 제목·저자·연도 조합은 한 항목으로 합쳐집니다.",
        f"> 이 검토용 문서에는 주제별 관련도 상위 {max_per_topic}개만 표시하며, 전체 자료는 DB에 보존됩니다.",
        "",
    ]
    if not rows:
        lines.extend(
            [
                "오늘 기준을 통과한 새 자료가 없습니다.",
                "",
                "## Codex 분석",
                "",
                "_자동화가 최신 웹 보강 후 이 부분을 갱신합니다._",
                "",
            ]
        )
    else:
        for topic_id, topic_rows in by_topic.items():
            if not topic_rows:
                continue
            lines.extend([f"## {topic_names.get(topic_id, topic_id)}", ""])
            for row in topic_rows[:max_per_topic]:
                row_dict = dict(row)
                authors = json.loads(row["authors_json"] or "[]")
                metadata = json.loads(row["metadata_json"] or "{}")
                author_text = ", ".join(authors[:3])
                metadata_bits = [row["source"]]
                if row["published_at"]:
                    metadata_bits.append(str(row["published_at"])[:10])
                if author_text:
                    metadata_bits.append(author_text)
                lines.extend(
                    [
                        f"### {source_note_wikilink(row_dict, research_directory, manifest)}",
                        "",
                        f"- 원문: [{row['url'] or row['canonical_url'] or '링크 없음'}]({row['url'] or row['canonical_url'] or ''})",
                        f"- 식별자: `{row['canonical_key']}`",
                        f"- 출처: {' | '.join(metadata_bits)}",
                        f"- 상태: `{row['review_status']}`",
                    ]
                )
                if metadata.get("evidence_role") == "lead_only":
                    lines.append("- 근거 역할: `SNS 신호 (원문 확인 전)`")
                if row["abstract"]:
                    lines.extend(["", f"> {_shorten(row['abstract'])}", ""])
                else:
                    lines.append("")
        lines.extend(
            [
                "## Codex 분석",
                "",
                "_시드 글과의 연결점, 인프라 영향, 우선순위는 자동화 실행에서 작성합니다._",
                "",
            ]
        )
    target.write_text("\n".join(lines), encoding="utf-8")
    return target
