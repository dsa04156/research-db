from __future__ import annotations

import argparse
import getpass
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

WORKSPACE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORKSPACE))

from research_harvester.core import ResearchStore, classify_item, load_config, local_date
from research_harvester.credentials import (
    CredentialError,
    load_zotero_credentials,
    save_zotero_environment,
)
from research_harvester.digest import write_digest
from research_harvester.obsidian import export_obsidian_graph
from research_harvester.sources import collect_all
from research_harvester.social import items_from_last30days_agent
from research_harvester.social_plan import build_social_plan
from research_harvester.zotero import (
    ZoteroClient,
    ZoteroError,
    sync_store_to_zotero,
    verify_api_key,
)


def resolve_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else WORKSPACE / path


def load_runtime_config(path: str | Path) -> dict[str, Any]:
    return load_config(resolve_path(path))


def store_from_config(config: dict[str, Any]) -> ResearchStore:
    return ResearchStore(resolve_path(config["database"]))


def ingest_items(
    store: ResearchStore,
    config: dict[str, Any],
    items: list[dict[str, Any]],
) -> dict[str, int]:
    summary = {"new": 0, "updated": 0, "duplicate": 0, "filtered": 0}
    for item in items:
        topic_matches = classify_item(item, config, item.get("topics"))
        if not topic_matches:
            summary["filtered"] += 1
            continue
        outcome = store.upsert(item, topic_matches)
        summary[outcome] += 1
    return summary


def command_init(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    print(json.dumps(store.status(), ensure_ascii=False, indent=2))
    return 0


def command_collect(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    if args.max_results is not None:
        config["max_results_per_query"] = args.max_results
    store = store_from_config(config)
    store.initialize()
    days = args.days if args.days is not None else int(config.get("lookback_days", 14))
    since_date = date.fromisoformat(args.since) if args.since else None
    until_date = date.fromisoformat(args.until) if args.until else None
    if since_date and args.days is not None:
        raise ValueError("--since and --days cannot be used together")
    if until_date and not since_date:
        raise ValueError("--until requires --since")
    if since_date and until_date and since_date > until_date:
        raise ValueError("--since must be on or before --until")
    run_id = store.start_run()
    summary: dict[str, Any] = {
        "new": 0,
        "updated": 0,
        "duplicate": 0,
        "filtered": 0,
        "errors": [],
    }
    try:
        items, errors = collect_all(
            config,
            days,
            since_date=since_date,
            until_date=until_date,
        )
        ingest_summary = ingest_items(store, config, items)
        summary.update(ingest_summary)
        summary["errors"] = errors
        summary["fetched"] = len(items)
        summary["days"] = (
            (until_date - since_date).days + 1
            if since_date and until_date
            else days
        )
        summary["since"] = since_date.isoformat() if since_date else None
        summary["until"] = until_date.isoformat() if until_date else None
        summary["max_results_per_query"] = int(config.get("max_results_per_query", 20))
    except Exception as exc:
        summary["errors"].append(
            {"source": "collector", "target": "all", "error": f"{type(exc).__name__}: {exc}"}
        )
    finally:
        store.finish_run(run_id, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    fatal = any(error.get("source") == "collector" for error in summary["errors"])
    return 1 if fatal else 0


def read_jsonl(path: str) -> list[dict[str, Any]]:
    handle = sys.stdin if path == "-" else resolve_path(path).open(encoding="utf-8")
    should_close = handle is not sys.stdin
    try:
        items = []
        for line_number, line in enumerate(handle, 1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON on line {line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"line {line_number} must be a JSON object")
            items.append(value)
        return items
    finally:
        if should_close:
            handle.close()


def command_ingest_jsonl(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    items = read_jsonl(args.input)
    summary = ingest_items(store, config, items)
    summary["input_items"] = len(items)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def command_ingest_social_report(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    with resolve_path(args.input).open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("social report must be a JSON object")

    topic_hints = [
        token.strip()
        for token in (args.topics or "").split(",")
        if token.strip()
    ]
    known_topics = {topic["id"] for topic in config["topics"]}
    unknown_topics = sorted(set(topic_hints) - known_topics)
    if unknown_topics:
        raise ValueError(f"unknown topic ids: {', '.join(unknown_topics)}")
    if not topic_hints:
        raise ValueError("--topics must contain at least one configured topic id")

    items = items_from_last30days_agent(payload, config, topic_hints)
    summary = ingest_items(store, config, items)
    reports = (
        [payload]
        if isinstance(payload.get("results"), list)
        else [
            entry.get("report") or {}
            for entry in payload.get("reports") or []
            if isinstance(entry, dict)
        ]
    )
    summary["converted"] = len(items)
    summary["input_results"] = sum(len(report.get("results") or []) for report in reports)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def command_social_plan(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    plan = build_social_plan(config, args.platform)
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


def command_digest(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    target_date = args.date or local_date()
    date.fromisoformat(target_date)
    obsidian_config = config.get("obsidian") or {}
    research_directory = obsidian_config.get("research_directory", "vault")
    if obsidian_config.get("export_on_digest", True):
        export_obsidian_graph(
            store,
            config,
            resolve_path(obsidian_config.get("vault_root", ".")),
            research_directory,
        )
    target = write_digest(
        store,
        config,
        target_date,
        resolve_path(config["digest_directory"]),
        research_directory,
    )
    print(str(target.resolve()))
    return 0


def command_obsidian_export(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    obsidian_config = config.get("obsidian") or {}
    summary = export_obsidian_graph(
        store,
        config,
        resolve_path(obsidian_config.get("vault_root", ".")),
        obsidian_config.get("research_directory", "vault"),
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def command_reclassify(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    print(json.dumps(store.reclassify(config), ensure_ascii=False, indent=2))
    return 0


def command_pending(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    rows = store.pending_items(args.date)
    payload = []
    for row in rows:
        payload.append(
            {
                "id": row["id"],
                "canonical_key": row["canonical_key"],
                "title": row["title"],
                "url": row["url"],
                "abstract": row["abstract"],
                "source": row["source"],
                "published_at": row["published_at"],
                "topics": row["topics"],
            }
        )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def command_status(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    print(json.dumps(store.status(), ensure_ascii=False, indent=2))
    return 0


def command_zotero_configure(args: argparse.Namespace) -> int:
    del args
    api_key = getpass.getpass("Zotero API key (input hidden): ").strip()
    if not api_key:
        raise ValueError("Zotero API key cannot be empty.")
    access = verify_api_key(api_key)
    user_id = str(access["userID"])
    save_zotero_environment(user_id, api_key)
    print(
        json.dumps(
            {
                "configured": True,
                "storage": "Windows user environment",
                "variables": ["ZOTERO_USER_ID", "ZOTERO_API_KEY"],
                "user_id": user_id,
                "library_read": True,
                "library_write": True,
                "api_key_displayed": False,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def command_zotero_status(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    payload: dict[str, Any] = {
        "configured": False,
        "database": store.zotero_status(),
    }
    try:
        user_id, api_key = load_zotero_credentials()
        client = ZoteroClient(
            user_id,
            api_key,
            int(config.get("request_timeout_seconds", 30)),
        )
        access = client.verify_access()
        payload.update(
            {
                "configured": True,
                "user_id": user_id,
                "library_read": bool(
                    access.get("access", {}).get("user", {}).get("library")
                ),
                "library_write": bool(
                    access.get("access", {}).get("user", {}).get("write")
                ),
            }
        )
    except (CredentialError, ZoteroError) as exc:
        payload["error"] = str(exc)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["configured"] else 1


def command_zotero_sync(args: argparse.Namespace) -> int:
    config = load_runtime_config(args.config)
    store = store_from_config(config)
    store.initialize()
    if args.date:
        date.fromisoformat(args.date)
    user_id, api_key = load_zotero_credentials()
    client = ZoteroClient(
        user_id,
        api_key,
        int(config.get("request_timeout_seconds", 30)),
    )
    zotero_config = config.get("zotero") or {}
    summary = sync_store_to_zotero(
        store,
        client,
        collection_name=zotero_config.get(
            "collection_name", "Codex Research Inbox"
        ),
        target_date=args.date,
        limit=args.limit,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if summary.get("failed") else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Collect and deduplicate personal research.")
    parser.add_argument("--config", default="config/research.json")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize the SQLite database.")
    init_parser.set_defaults(handler=command_init)

    collect_parser = subparsers.add_parser("collect", help="Collect structured sources.")
    collect_parser.add_argument("--days", type=int)
    collect_parser.add_argument(
        "--since",
        help="Inclusive start date (YYYY-MM-DD) for a bounded bootstrap window.",
    )
    collect_parser.add_argument(
        "--until",
        help="Inclusive end date (YYYY-MM-DD); requires --since.",
    )
    collect_parser.add_argument(
        "--max-results",
        type=int,
        help="Override the per-topic result cap for this run only.",
    )
    collect_parser.set_defaults(handler=command_collect)

    ingest_parser = subparsers.add_parser(
        "ingest-jsonl", help="Ingest Codex or manually gathered JSONL findings."
    )
    ingest_parser.add_argument("--input", required=True, help="JSONL file or - for stdin.")
    ingest_parser.set_defaults(handler=command_ingest_jsonl)

    social_parser = subparsers.add_parser(
        "ingest-social-report",
        help="Ingest a last30days agent JSON report as lead-only social signals.",
    )
    social_parser.add_argument("--input", required=True, help="Agent-profile JSON file.")
    social_parser.add_argument(
        "--topics",
        required=True,
        help="Comma-separated configured topic ids used by the social query.",
    )
    social_parser.set_defaults(handler=command_ingest_social_report)

    social_plan_parser = subparsers.add_parser(
        "social-plan",
        help="Print deterministic platform-specific social search queries.",
    )
    social_plan_parser.add_argument(
        "--platform",
        required=True,
        help="Configured social platform id, for example threads.",
    )
    social_plan_parser.set_defaults(handler=command_social_plan)

    digest_parser = subparsers.add_parser("digest", help="Write a daily Markdown digest.")
    digest_parser.add_argument("--date", help="Local date in YYYY-MM-DD.")
    digest_parser.set_defaults(handler=command_digest)

    obsidian_export_parser = subparsers.add_parser(
        "obsidian-export",
        help="Export active DB items as linked Obsidian source and topic notes.",
    )
    obsidian_export_parser.set_defaults(handler=command_obsidian_export)

    reclassify_parser = subparsers.add_parser(
        "reclassify",
        help="Re-apply topic and future-date filters without deleting records.",
    )
    reclassify_parser.set_defaults(handler=command_reclassify)

    pending_parser = subparsers.add_parser("pending", help="Print pending items as JSON.")
    pending_parser.add_argument("--date", help="Filter by first-seen local date.")
    pending_parser.set_defaults(handler=command_pending)

    status_parser = subparsers.add_parser("status", help="Show database and last-run status.")
    status_parser.set_defaults(handler=command_status)

    zotero_configure_parser = subparsers.add_parser(
        "zotero-configure",
        help="Securely save a write-capable Zotero API key in the Windows user environment.",
    )
    zotero_configure_parser.set_defaults(handler=command_zotero_configure)

    zotero_status_parser = subparsers.add_parser(
        "zotero-status",
        help="Verify Zotero credentials and show synchronization status.",
    )
    zotero_status_parser.set_defaults(handler=command_zotero_status)

    zotero_sync_parser = subparsers.add_parser(
        "zotero-sync",
        help="Create missing research items in Zotero without duplicating existing items.",
    )
    zotero_sync_parser.add_argument("--date", help="Filter by first-seen local date.")
    zotero_sync_parser.add_argument("--limit", type=int, default=100)
    zotero_sync_parser.set_defaults(handler=command_zotero_sync)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.handler(args))
    except (CredentialError, OSError, ValueError, KeyError, ZoteroError) as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
