---
type: research-source
item_id: 1610
title: "ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory"
source: "arxiv"
published: "2026-07-30T07:07:39Z"
first_seen: "2026-07-31"
review_status: "pending"
canonical_key: "arxiv:2607.27773"
url: "https://arxiv.org/abs/2607.27773v1"
generated_by: codex-research-db
aliases:
  - "ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory"
topics:
  - "ai-agents"
---

# ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory

[원문 열기](https://arxiv.org/abs/2607.27773v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-31|2026-07-31]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7EKNEBV4`)
- 발행일: 2026-07-30T07:07:39Z
- 저자: Yongye Su, Wujiang Xu, Chaoji Zuo, Elisa Bertino
- 식별자: `arxiv:2607.27773`

## 요약·초록

LLM agents increasingly rely on long-term memory to support multi-session interaction and personalization. However, existing agent memory systems are designed around forward-only evolution, continuously accumulating, consolidating, and overwriting knowledge, with no principled mechanism to inspect, version, or revert prior states. This makes agents brittle under corrections, concept drift, and memory corruption, particularly after they have already been exposed to subsequent information. We present ChronoMem, a semantic version-control layer for agentic memory integrated into the production-ready, open-source Agent Development Kit by Google. ChronoMem commits whole-memory snapshots at each memory write, maintains structured version histories, and supports natural-language rollback requests by mapping undo intents to concrete historical versions through hybrid lexical and semantic retrieval, rank fusion, and reranking. We further introduce a post-exposure evaluation protocol that tests whether an agent can behave counterfactually after rollback by answering queries and summarizing history as if future updates had never occurred. On long-horizon conversational benchmarks augmented with evolving memory states and rollback tasks, ChronoMem substantially improves rollback-consistent question answering and history summarization relative to prompt-only and retrieval-only baselines, while achieving strong performance in semantic version selection. To our knowledge, ChronoMem is the first open-source system and benchmark for systematic semantic global memory rollback in LLM agents.

## 내 메모


