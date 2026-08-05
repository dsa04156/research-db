from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from research_harvester.core import (
    ResearchStore,
    canonicalize_url,
    classify_item,
    local_date,
    normalize_arxiv_id,
    normalize_doi,
)
from research_harvester.digest import write_digest
from research_harvester.obsidian import export_obsidian_graph
from research_harvester.social import items_from_last30days_agent
from research_harvester.social_plan import build_social_plan


CONFIG = {
    "minimum_relevance_score": 2.0,
    "topics": [
        {
            "id": "harness",
            "name": "Harness",
            "keywords": ["agent harness", "self-improving agent"],
            "boost_keywords": ["evaluation"],
            "exclude_keywords": ["horse harness"],
        }
    ],
}


def item(**overrides):
    value = {
        "source": "test",
        "source_id": "one",
        "title": "Agent Harness Design for Self-Improving Agents",
        "url": "https://example.com/paper?utm_source=test",
        "abstract": "Evaluation and workflow design for a self-improving agent.",
        "authors": ["Ada Researcher"],
        "published_at": "2026-07-20",
        "topics": ["harness"],
    }
    value.update(overrides)
    return value


class NormalizationTests(unittest.TestCase):
    def test_normalize_identifiers(self):
        self.assertEqual(normalize_doi("https://doi.org/10.1234/ABC"), "10.1234/abc")
        self.assertEqual(normalize_arxiv_id("https://arxiv.org/abs/2607.12345v2"), "2607.12345")
        self.assertIsNone(
            normalize_arxiv_id("https://doi.org/10.22266/ijies2026.0831.18")
        )
        self.assertIsNone(
            normalize_arxiv_id("https://tiktok.com/@creator/video/7668189103212530976")
        )
        self.assertIsNone(
            normalize_arxiv_id("https://example.com/event/1662511")
        )

    def test_canonical_url_removes_tracking(self):
        self.assertEqual(
            canonicalize_url("https://www.Example.com/a/?utm_source=x&b=2&a=1#section"),
            "https://example.com/a?a=1&b=2",
        )


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = ResearchStore(self.root / "research.db")
        self.store.initialize()

    def tearDown(self):
        self.temp.cleanup()

    def test_deduplicates_by_doi_across_sources(self):
        first = item(doi="10.1000/XYZ", source="crossref")
        second = item(
            doi="https://doi.org/10.1000/xyz",
            source="openalex",
            url="https://different.example/article",
            source_id="two",
        )
        first_matches = classify_item(first, CONFIG, first["topics"])
        second_matches = classify_item(second, CONFIG, second["topics"])
        self.assertEqual(self.store.upsert(first, first_matches), "new")
        self.assertIn(self.store.upsert(second, second_matches), {"updated", "duplicate"})
        self.assertEqual(self.store.status()["items"], 1)

    def test_arxiv_url_is_checked_when_social_source_id_is_not_arxiv(self):
        primary = item(
            source="arxiv",
            source_id="2607.13285",
            arxiv_id="2607.13285",
            url="https://export.arxiv.org/abs/2607.13285",
        )
        social = item(
            source="social:linkedin",
            source_id="https://linkedin.com/posts/example",
            url="https://arxiv.org/abs/2607.13285",
            source_url="https://www.linkedin.com/posts/example",
        )
        self.store.upsert(primary, classify_item(primary, CONFIG, primary["topics"]))
        outcome = self.store.upsert(
            social, classify_item(social, CONFIG, social["topics"])
        )
        self.assertEqual(self.store.status()["items"], 1)
        self.assertEqual(outcome, "duplicate")

    def test_deduplicates_by_normalized_title(self):
        first = item(url="https://one.example/paper", source_id="one")
        second = item(
            title="Agent Harness Design: for Self Improving Agents",
            url="https://two.example/preprint",
            source_id="two",
        )
        self.store.upsert(first, classify_item(first, CONFIG, first["topics"]))
        self.store.upsert(second, classify_item(second, CONFIG, second["topics"]))
        self.assertEqual(self.store.status()["items"], 1)

    def test_social_discovery_url_is_preserved_as_a_sighting(self):
        primary = item(source="official-blog", source_id="post")
        social = item(
            source="social:threads",
            source_id="thread-1",
            source_url="https://www.threads.net/@researcher/post/thread-1",
            metadata={
                "source_type": "social-post",
                "evidence_role": "lead_only",
                "platform": "threads",
            },
        )
        self.store.upsert(primary, classify_item(primary, CONFIG, primary["topics"]))
        self.store.upsert(social, classify_item(social, CONFIG, social["topics"]))

        with self.store.connect() as connection:
            rows = connection.execute(
                "SELECT source, source_url, metadata_json FROM sightings ORDER BY id"
            ).fetchall()
            stored = connection.execute("SELECT source, metadata_json FROM items").fetchone()

        self.assertEqual(self.store.status()["items"], 1)
        self.assertEqual(rows[1]["source_url"], social["source_url"])
        self.assertEqual(json.loads(rows[1]["metadata_json"])["platform"], "threads")
        self.assertEqual(stored["source"], "official-blog")
        self.assertNotIn("evidence_role", json.loads(stored["metadata_json"]))

    def test_primary_source_promotes_social_first_item(self):
        social = item(
            source="social:linkedin",
            source_id="linkedin-1",
            source_url="https://www.linkedin.com/posts/example",
            metadata={
                "source_type": "social-post",
                "evidence_role": "lead_only",
                "platform": "linkedin",
            },
        )
        primary = item(
            source="official-blog",
            source_id="post",
            doi="10.1000/primary",
            title="Primary AI Agent Harness Research",
        )
        self.store.upsert(social, classify_item(social, CONFIG, social["topics"]))
        self.store.upsert(primary, classify_item(primary, CONFIG, primary["topics"]))

        with self.store.connect() as connection:
            stored = connection.execute(
                "SELECT canonical_key, source, title, metadata_json FROM items"
            ).fetchone()

        self.assertEqual(stored["source"], "official-blog")
        self.assertEqual(stored["canonical_key"], "doi:10.1000/primary")
        self.assertEqual(stored["title"], primary["title"])
        self.assertNotIn("evidence_role", json.loads(stored["metadata_json"]))
        self.assertEqual(self.store.status()["social_platforms"][0]["platform"], "linkedin")

    def test_filters_irrelevant_item(self):
        irrelevant = item(
            title="Horse Harness Buying Guide",
            abstract="A practical guide.",
            topics=[],
        )
        self.assertEqual(classify_item(irrelevant, CONFIG), [])

    def test_lead_only_external_score_does_not_override_local_topic_match(self):
        value = item(
            title="Edge Drop clipboard utility",
            abstract="A desktop clipboard manager with no AI infrastructure features.",
            topics=["harness"],
            relevance_score=0.9,
            metadata={
                "source_type": "social-post",
                "evidence_role": "lead_only",
                "platform": "hackernews",
            },
        )
        self.assertEqual(classify_item(value, CONFIG, value["topics"]), [])

    def test_query_hint_does_not_admit_generic_boost_only_item(self):
        generic = item(
            title="A Runtime Evaluation",
            abstract="A general systems paper.",
            topics=["harness"],
        )
        self.assertEqual(classify_item(generic, CONFIG, generic["topics"]), [])

    def test_trusted_source_hint_is_accepted(self):
        release = item(
            title="Trusted Project v1.2.3",
            abstract="Maintenance release.",
            topics=["harness"],
            trusted_topic_hints=True,
        )
        self.assertEqual(classify_item(release, CONFIG, release["topics"])[0]["topic_id"], "harness")

    def test_reclassify_quarantines_future_item(self):
        future = item(published_at="2099-01-01")
        self.store.upsert(future, classify_item(future, CONFIG, future["topics"]))
        summary = self.store.reclassify(CONFIG)
        self.assertEqual(summary["excluded_future"], 1)
        self.assertEqual(self.store.items_for_date("2026-07-30"), [])

    def test_digest_contains_one_unique_item(self):
        value = item()
        self.store.upsert(value, classify_item(value, CONFIG, value["topics"]))
        export_obsidian_graph(self.store, CONFIG, self.root, "Research")
        target_date = local_date()
        target = write_digest(
            self.store,
            CONFIG,
            target_date,
            self.root / "Daily",
            "Research",
        )
        content = target.read_text(encoding="utf-8")
        self.assertIn("새로 수집된 고유 자료", content)
        self.assertEqual(content.count("### [["), 1)
        self.assertIn("Agent Harness Design for Self-Improving Agents", content)
        self.assertIn("> Evaluation and workflow design", content)

    def test_obsidian_export_creates_idempotent_graph_notes(self):
        value = item(title='Agent Harness: Design / "Evaluation"?')
        self.store.upsert(value, classify_item(value, CONFIG, value["topics"]))

        first = export_obsidian_graph(self.store, CONFIG, self.root, "Research")
        second = export_obsidian_graph(self.store, CONFIG, self.root, "Research")
        source_notes = list((self.root / "Research" / "Sources").glob("*.md"))
        topic_note = self.root / "Research" / "Topics" / "Harness.md"

        self.assertEqual(first["source_notes"], 1)
        self.assertEqual(second["source_notes"], 1)
        self.assertEqual(len(source_notes), 1)
        self.assertTrue(topic_note.exists())
        source_content = source_notes[0].read_text(encoding="utf-8")
        topic_content = topic_note.read_text(encoding="utf-8")
        self.assertIn("[[Research/Topics/Harness]]", source_content)
        target_date = local_date()
        self.assertIn(
            f"[[Research/Daily/{target_date}|{target_date}]]",
            source_content,
        )
        self.assertIn("[[Research/Sources/", topic_content)
        self.assertTrue((self.root / "Research" / "Research Graph.md").exists())

        source_notes[0].write_text(
            source_content + "사용자가 작성한 메모\n",
            encoding="utf-8",
        )
        export_obsidian_graph(self.store, CONFIG, self.root, "Research")
        self.assertIn(
            "사용자가 작성한 메모",
            source_notes[0].read_text(encoding="utf-8"),
        )


class SocialImportTests(unittest.TestCase):
    def test_agent_export_maps_primary_and_discovery_urls(self):
        config = {
            **CONFIG,
            "social_research": {
                "minimum_result_relevance": 0.45,
                "excluded_platforms": ["x"],
                "platforms": [
                    {
                        "id": "threads",
                        "quality_tier": "E",
                        "evidence_role": "lead_only",
                    }
                ],
            },
        }
        payload = {
            "schema_version": "1.0",
            "query": "agent harness",
            "generated_at": "2026-07-30T00:00:00Z",
            "results": [
                {
                    "candidate_id": "thread-1",
                    "title": "Agent Harness Evaluation",
                    "source": "threads",
                    "url": "https://www.threads.net/@researcher/post/thread-1",
                    "primary_url": "https://example.com/agent-harness",
                    "summary": "A self-improving agent evaluation workflow.",
                    "relevance_score": 0.8,
                    "engagement": {"likes": 120},
                },
                {
                    "candidate_id": "x-1",
                    "title": "Excluded X post",
                    "source": "x",
                    "url": "https://x.com/example/status/1",
                    "relevance_score": 0.9,
                },
            ],
        }

        items = items_from_last30days_agent(payload, config, ["harness"])

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["url"], "https://example.com/agent-harness")
        self.assertEqual(
            items[0]["source_url"],
            "https://www.threads.net/@researcher/post/thread-1",
        )
        self.assertEqual(items[0]["metadata"]["engagement"]["likes"], 120)


class SocialPlanTests(unittest.TestCase):
    def test_threads_uses_multiple_short_platform_queries(self):
        config = {
            **CONFIG,
            "social_research": {
                "excluded_platforms": ["x"],
                "platforms": [{"id": "threads"}, {"id": "x"}],
                "queries": [
                    {
                        "name": "Harnesses",
                        "query": "self improving AI agent harness context engineering",
                        "platform_queries": {
                            "threads": [
                                "agent harness",
                                "harness engineering",
                                "self-improving agent",
                            ]
                        },
                        "topic_hints": ["harness"],
                    }
                ],
            },
        }

        plan = build_social_plan(config, "threads")

        self.assertFalse(plan["excluded"])
        self.assertEqual(
            [entry["query"] for entry in plan["queries"]],
            ["agent harness", "harness engineering", "self-improving agent"],
        )
        self.assertTrue(
            all(len(entry["query"].split()) <= 2 for entry in plan["queries"])
        )

    def test_threads_compaction_is_explicit_and_watch_queries_are_included(self):
        config = {
            **CONFIG,
            "social_research": {
                "platforms": [{"id": "threads"}],
                "queries": [
                    {
                        "name": "Harnesses",
                        "query": "agent harness evaluation",
                        "topic_hints": ["harness"],
                    }
                ],
                "watch_queries": [
                    {
                        "name": "Researcher watch",
                        "platform": "threads",
                        "query": "researcher handle",
                        "topic_hints": ["harness"],
                    }
                ],
            },
        }

        plan = build_social_plan(config, "threads")

        self.assertEqual(len(plan["queries"]), 2)
        self.assertEqual(plan["queries"][0]["query"], "agent harness")
        self.assertEqual(plan["queries"][0]["raw_query"], "agent harness evaluation")
        self.assertTrue(plan["queries"][0]["compacted"])
        self.assertEqual(plan["queries"][1]["query_kind"], "watch")

    def test_excluded_platform_produces_no_runs(self):
        config = {
            **CONFIG,
            "social_research": {
                "platforms": [{"id": "x"}],
                "excluded_platforms": ["x"],
                "queries": [{"query": "agent harness", "topic_hints": ["harness"]}],
            },
        }

        plan = build_social_plan(config, "x")

        self.assertTrue(plan["excluded"])
        self.assertEqual(plan["queries"], [])

    def test_duplicate_queries_merge_topics_to_save_api_calls(self):
        config = {
            **CONFIG,
            "social_research": {
                "platforms": [{"id": "threads"}],
                "queries": [
                    {
                        "name": "Harnesses",
                        "query": "agent harness",
                        "topic_hints": ["harness"],
                    },
                    {
                        "name": "Agents",
                        "query": "agent harness",
                        "topic_hints": ["agents"],
                    },
                ],
            },
        }

        plan = build_social_plan(config, "threads")

        self.assertEqual(len(plan["queries"]), 1)
        self.assertEqual(plan["queries"][0]["topic_hints"], ["harness", "agents"])


if __name__ == "__main__":
    unittest.main()
