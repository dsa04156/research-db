from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from .core import ResearchStore, normalize_space


GENERATED_BY = "codex-research-db"
MANIFEST_NAME = ".research-graph-manifest.json"
_INVALID_FILENAME = re.compile(r'[<>:"/\\|?*\x00-\x1f\[\]#^]')
_WHITESPACE = re.compile(r"\s+")


def safe_note_name(value: str | None, fallback: str, limit: int = 96) -> str:
    """Create a readable Windows- and Obsidian-safe note name."""
    name = unicodedata.normalize("NFKC", normalize_space(value))
    name = _INVALID_FILENAME.sub(" ", name)
    name = _WHITESPACE.sub(" ", name).strip(" .")
    if not name:
        name = fallback
    if len(name) > limit:
        name = name[:limit].rstrip(" .")
    return name or fallback


def _yaml_string(value: Any) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def _link_alias(value: str) -> str:
    return normalize_space(value).replace("|", " ").replace("]", " ")


def _parse_topics(raw_topics: str | None) -> list[tuple[str, float]]:
    values: list[tuple[str, float]] = []
    for token in (raw_topics or "").split(","):
        topic_id, separator, raw_score = token.partition(":")
        if not topic_id:
            continue
        try:
            score = float(raw_score) if separator else 0.0
        except ValueError:
            score = 0.0
        values.append((topic_id, score))
    return sorted(values, key=lambda pair: pair[1], reverse=True)


def _read_manifest(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    items = payload.get("items") if isinstance(payload, dict) else None
    if not isinstance(items, dict):
        return {}
    return {
        str(item_id): str(relative_path)
        for item_id, relative_path in items.items()
        if str(item_id).isdigit() and isinstance(relative_path, str)
    }


def _source_relative_path(
    row: dict[str, Any],
    research_directory: Path,
    existing_manifest: dict[str, str],
) -> Path:
    item_id = str(int(row["id"]))
    existing = existing_manifest.get(item_id)
    if existing:
        candidate = Path(existing)
        if (
            not candidate.is_absolute()
            and ".." not in candidate.parts
            and candidate.suffix.casefold() == ".md"
        ):
            return candidate
    title = safe_note_name(row.get("title"), f"Research item {item_id}")
    return research_directory / "Sources" / f"{title} -- R{int(item_id):06d}.md"


def _wikilink(relative_path: Path, alias: str | None = None) -> str:
    target = relative_path.with_suffix("").as_posix()
    if alias:
        return f"[[{target}|{_link_alias(alias)}]]"
    return f"[[{target}]]"


def source_note_wikilink(
    row: dict[str, Any],
    research_directory: str | Path = "vault",
    manifest: dict[str, str] | None = None,
) -> str:
    research_path = Path(research_directory)
    relative_path = _source_relative_path(row, research_path, manifest or {})
    return _wikilink(relative_path, str(row["title"]))


def _source_note(
    row: dict[str, Any],
    source_relative_path: Path,
    topic_paths: dict[str, Path],
    personal_memo: str = "",
) -> str:
    authors = json.loads(row.get("authors_json") or "[]")
    metadata = json.loads(row.get("metadata_json") or "{}")
    topics = _parse_topics(row.get("topics"))
    url = row.get("url") or row.get("canonical_url") or ""
    lines = [
        "---",
        "type: research-source",
        f"item_id: {int(row['id'])}",
        f"title: {_yaml_string(row['title'])}",
        f"source: {_yaml_string(row['source'])}",
        f"published: {_yaml_string(row.get('published_at') or '')}",
        f"first_seen: {_yaml_string(row.get('first_seen_date') or '')}",
        f"review_status: {_yaml_string(row.get('review_status') or '')}",
        f"canonical_key: {_yaml_string(row.get('canonical_key') or '')}",
        f"url: {_yaml_string(url)}",
        f"generated_by: {GENERATED_BY}",
        "aliases:",
        f"  - {_yaml_string(row['title'])}",
        "topics:",
    ]
    lines.extend(f"  - {_yaml_string(topic_id)}" for topic_id, _ in topics)
    lines.extend(["---", "", f"# {row['title']}", ""])
    if metadata.get("evidence_role") == "lead_only":
        lines.extend(
            [
                "> [!warning] SNS 탐색 신호",
                "> 원문이나 1차 자료를 확인하기 전에는 근거로 인용하지 않습니다.",
                "",
            ]
        )
    if url:
        lines.extend([f"[원문 열기]({url})", ""])
    lines.extend(["## 연결", ""])
    if topics:
        topic_links = [
            _wikilink(topic_paths[topic_id])
            for topic_id, _ in topics
            if topic_id in topic_paths
        ]
        lines.append(f"- 주제: {', '.join(topic_links)}")
    if row.get("first_seen_date"):
        daily_path = source_relative_path.parents[1] / "Daily" / (
            str(row["first_seen_date"]) + ".md"
        )
        lines.append(
            f"- 최초 수집: {_wikilink(daily_path, str(row['first_seen_date']))}"
        )
    lines.extend(
        [
            f"- 수집 채널: `{row['source']}`",
            f"- 검토 상태: `{row['review_status']}`",
        ]
    )
    if row.get("zotero_sync_status"):
        zotero_text = str(row["zotero_sync_status"])
        if row.get("zotero_item_key"):
            zotero_text += f" (`{row['zotero_item_key']}`)"
        lines.append(f"- Zotero: {zotero_text}")
    if row.get("published_at"):
        lines.append(f"- 발행일: {row['published_at']}")
    if authors:
        lines.append(f"- 저자: {', '.join(str(author) for author in authors)}")
    lines.extend(
        [
            f"- 식별자: `{row['canonical_key']}`",
            "",
            "## 요약·초록",
            "",
            normalize_space(row.get("abstract")) or "_수집된 요약이 없습니다._",
            "",
            "## 내 메모",
            "",
            personal_memo.rstrip(),
            "",
        ]
    )
    return "\n".join(lines)


def _existing_personal_memo(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    marker = "\n## 내 메모\n"
    _, separator, memo = content.partition(marker)
    return memo.strip() if separator else ""


def _topic_note(
    topic: dict[str, Any],
    topic_rows: Iterable[tuple[dict[str, Any], float]],
    source_paths: dict[int, Path],
) -> str:
    rows = list(topic_rows)
    lines = [
        "---",
        "type: research-topic",
        f"topic_id: {_yaml_string(topic['id'])}",
        f"generated_by: {GENERATED_BY}",
        f"source_count: {len(rows)}",
        "---",
        "",
        f"# {topic['name']}",
        "",
        normalize_space(topic.get("description")),
        "",
        f"연결된 자료: **{len(rows)}개**",
        "",
        "## 자료",
        "",
    ]
    for row, score in rows:
        link = _wikilink(source_paths[int(row["id"])], str(row["title"]))
        date_text = str(row.get("published_at") or "")[:10] or "날짜 없음"
        lines.append(f"- {link} — {date_text} · `{row['source']}` · 관련도 {score:.1f}")
    lines.append("")
    return "\n".join(lines)


def export_obsidian_graph(
    store: ResearchStore,
    config: dict[str, Any],
    vault_root: str | Path,
    research_directory: str | Path = "vault",
) -> dict[str, Any]:
    """Export active DB rows as linked Obsidian topic and source notes."""
    root = Path(vault_root)
    research_path = Path(research_directory)
    if research_path.is_absolute() or ".." in research_path.parts:
        raise ValueError("research_directory must stay inside the Obsidian vault")

    output_root = root / research_path
    source_directory = output_root / "Sources"
    topic_directory = output_root / "Topics"
    source_directory.mkdir(parents=True, exist_ok=True)
    topic_directory.mkdir(parents=True, exist_ok=True)

    manifest_path = output_root / MANIFEST_NAME
    existing_manifest = _read_manifest(manifest_path)
    rows = store.active_items()
    configured_topics = {topic["id"]: topic for topic in config["topics"]}
    topic_paths = {
        topic_id: research_path
        / "Topics"
        / f"{safe_note_name(topic['name'], topic_id)}.md"
        for topic_id, topic in configured_topics.items()
    }
    source_paths = {
        int(row["id"]): _source_relative_path(row, research_path, existing_manifest)
        for row in rows
    }

    topics_to_rows: dict[str, list[tuple[dict[str, Any], float]]] = defaultdict(list)
    graph_links = 0
    for row in rows:
        relative_path = source_paths[int(row["id"])]
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        parsed_topics = _parse_topics(row.get("topics"))
        for topic_id, score in parsed_topics:
            if topic_id in configured_topics:
                topics_to_rows[topic_id].append((row, score))
                graph_links += 1
        if row.get("first_seen_date"):
            graph_links += 1
        personal_memo = _existing_personal_memo(target)
        target.write_text(
            _source_note(row, relative_path, topic_paths, personal_memo),
            encoding="utf-8",
        )

    for topic_id, topic in configured_topics.items():
        topic_rows = topics_to_rows.get(topic_id, [])
        topic_rows.sort(
            key=lambda pair: (
                pair[1],
                str(pair[0].get("published_at") or ""),
                int(pair[0]["id"]),
            ),
            reverse=True,
        )
        target = root / topic_paths[topic_id]
        target.write_text(
            _topic_note(topic, topic_rows, source_paths),
            encoding="utf-8",
        )

    index_path = research_path / "Research Graph.md"
    index_lines = [
        "---",
        "type: research-graph-index",
        f"generated_by: {GENERATED_BY}",
        f"source_count: {len(rows)}",
        f"topic_count: {len(configured_topics)}",
        "---",
        "",
        "# Research Graph",
        "",
        "SQLite 연구 DB를 Obsidian 그래프로 탐색하기 위한 시작점입니다.",
        "",
        "## 관심 주제",
        "",
    ]
    for topic_id, topic in configured_topics.items():
        count = len(topics_to_rows.get(topic_id, []))
        index_lines.append(
            f"- {_wikilink(topic_paths[topic_id], str(topic['name']))} — {count}개"
        )
        graph_links += 1
    synthesis_directory = output_root / "Synthesis"
    synthesis_notes = (
        sorted(
            (
                path
                for path in synthesis_directory.glob("*.md")
                if path.name.casefold() != "readme.md"
            ),
            key=lambda path: path.name,
            reverse=True,
        )
        if synthesis_directory.exists()
        else []
    )
    if synthesis_notes:
        index_lines.extend(["", "## 주간 종합", ""])
        for path in synthesis_notes[:12]:
            relative_path = path.relative_to(root)
            index_lines.append(f"- {_wikilink(relative_path, path.stem)}")
            graph_links += 1
    briefing_directory = output_root / "Briefings"
    briefing_notes = (
        sorted(
            (
                path
                for path in briefing_directory.glob("*.md")
                if path.name.casefold() != "readme.md"
            ),
            key=lambda path: path.name,
            reverse=True,
        )
        if briefing_directory.exists()
        else []
    )
    if briefing_notes:
        index_lines.extend(["", "## 일일 브리핑", ""])
        for path in briefing_notes[:14]:
            relative_path = path.relative_to(root)
            index_lines.append(f"- {_wikilink(relative_path, path.stem)}")
            graph_links += 1
    index_lines.extend(
        [
            "",
            "## 사용법",
            "",
            "- 그래프에서 이 노트를 중심으로 열면 다섯 관심 주제와 자료 군집을 볼 수 있습니다.",
            "- `Sources/` 노트의 `내 메모` 영역은 개인 연구 메모용입니다.",
            "- 원시 수집·중복 제거의 기준 데이터는 SQLite DB입니다.",
            "",
        ]
    )
    (root / index_path).write_text("\n".join(index_lines), encoding="utf-8")

    manifest = {
        "generated_by": GENERATED_BY,
        "items": {
            str(item_id): relative_path.as_posix()
            for item_id, relative_path in source_paths.items()
        },
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return {
        "index": str((root / index_path).resolve()),
        "source_notes": len(rows),
        "topic_notes": len(configured_topics),
        "graph_links": graph_links,
        "manifest": str(manifest_path.resolve()),
    }
