from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from research_harvester.core import ResearchStore, classify_item
from research_harvester.zotero import (
    ZoteroError,
    build_existing_index,
    find_existing,
    sync_store_to_zotero,
    to_zotero_item,
)


CONFIG = {
    "minimum_relevance_score": 2.0,
    "topics": [
        {
            "id": "agents",
            "name": "AI agents",
            "keywords": ["ai agent"],
            "boost_keywords": ["evaluation"],
            "exclude_keywords": [],
        }
    ],
}


def local_item(**overrides):
    value = {
        "source": "rss:Engineering Blog",
        "source_id": "post-1",
        "title": "AI Agent Evaluation in Production",
        "url": "https://example.com/post?utm_source=rss",
        "abstract": "An AI agent evaluation field report.",
        "authors": ["Ada Researcher"],
        "container_title": "Engineering Blog",
        "published_at": "2026-07-29",
        "topics": ["agents"],
        "trusted_topic_hints": True,
        "metadata": {
            "source_type": "official-blog",
            "quality_tier": "A",
            "trusted_topic_hints": True,
        },
    }
    value.update(overrides)
    return value


class ZoteroMappingTests(unittest.TestCase):
    def test_existing_index_matches_canonical_url(self):
        existing = {
            "key": "ABC12345",
            "data": {
                "title": "AI Agent Evaluation in Production",
                "url": "https://example.com/post",
                "extra": "",
            },
        }
        index = build_existing_index([existing])
        row = {
            "title": "Different mirror title",
            "url": "https://www.example.com/post?utm_campaign=x",
        }
        self.assertIs(find_existing(row, index), existing)

    def test_blog_maps_to_blog_post_with_codex_key(self):
        row = {
            "canonical_key": "url:abc",
            "source": "rss:Engineering Blog",
            "title": "AI Agent Evaluation in Production",
            "url": "https://example.com/post",
            "abstract": "Summary",
            "authors_json": json.dumps(["Ada Researcher"]),
            "container_title": "Engineering Blog",
            "published_at": "2026-07-29",
            "topics": "agents:4.0",
            "metadata_json": json.dumps({"source_type": "official-blog"}),
            "doi": None,
            "arxiv_id": None,
        }
        payload = to_zotero_item(row, "COLL1234")
        self.assertEqual(payload["itemType"], "blogPost")
        self.assertEqual(payload["blogTitle"], "Engineering Blog")
        self.assertIn("Codex Research Key: url:abc", payload["extra"])
        self.assertEqual(payload["collections"], ["COLL1234"])


class _FakeZoteroClient:
    user_id = "12345"

    def __init__(self):
        self.created = []

    def verify_access(self):
        return {"access": {"user": {"library": True, "write": True}}}

    def list_top_items(self):
        return []

    def ensure_collection(self, name):
        self.collection_name = name
        return "COLL1234"

    def create_items(self, items):
        self.created.extend(items)
        return {
            "successful": {
                str(index): {"key": f"ITEM{index:04d}", "version": 1}
                for index in range(len(items))
            }
        }


class _RateLimitedZoteroClient(_FakeZoteroClient):
    def create_items(self, items):
        raise ZoteroError(
            "Zotero API returned HTTP 429",
            status_code=429,
            retry_after=60,
        )


class ZoteroSyncTests(unittest.TestCase):
    def test_sync_is_idempotent_locally(self):
        with tempfile.TemporaryDirectory() as directory:
            store = ResearchStore(Path(directory) / "research.db")
            store.initialize()
            value = local_item()
            store.upsert(value, classify_item(value, CONFIG, value["topics"]))
            client = _FakeZoteroClient()

            first = sync_store_to_zotero(
                store,
                client,
                collection_name="Codex Research Inbox",
            )
            second = sync_store_to_zotero(
                store,
                client,
                collection_name="Codex Research Inbox",
            )

            self.assertEqual(first["created"], 1)
            self.assertEqual(second["candidates"], 0)
            self.assertEqual(len(client.created), 1)
            self.assertEqual(store.zotero_status()["unsynced"], 0)

    def test_lead_only_social_signal_is_not_sent_to_zotero(self):
        with tempfile.TemporaryDirectory() as directory:
            store = ResearchStore(Path(directory) / "research.db")
            store.initialize()
            value = local_item(
                source="social:threads",
                source_id="thread-1",
                url="https://www.threads.net/@researcher/post/thread-1",
                metadata={
                    "source_type": "social-post",
                    "evidence_role": "lead_only",
                    "platform": "threads",
                },
            )
            store.upsert(value, classify_item(value, CONFIG, value["topics"]))
            client = _FakeZoteroClient()

            result = sync_store_to_zotero(
                store,
                client,
                collection_name="Codex Research Inbox",
            )

            self.assertEqual(result["candidates"], 0)
            self.assertEqual(client.created, [])
            self.assertEqual(store.zotero_status()["unsynced"], 0)

    def test_rate_limit_stops_remaining_batches(self):
        with tempfile.TemporaryDirectory() as directory:
            store = ResearchStore(Path(directory) / "research.db")
            store.initialize()
            for index in range(60):
                value = local_item(
                    source_id=f"post-{index}",
                    title=f"AI Agent Evaluation in Production {index}",
                    url=f"https://example.com/post-{index}",
                )
                store.upsert(value, classify_item(value, CONFIG, value["topics"]))
            client = _RateLimitedZoteroClient()

            result = sync_store_to_zotero(
                store,
                client,
                collection_name="Codex Research Inbox",
                limit=100,
            )

            self.assertTrue(result["rate_limited"])
            self.assertEqual(result["failed"], 50)
            self.assertEqual(result["deferred"], 10)
            self.assertEqual(result["retry_after_seconds"], 60)
            self.assertEqual(store.zotero_status()["unsynced"], 60)


if __name__ == "__main__":
    unittest.main()
