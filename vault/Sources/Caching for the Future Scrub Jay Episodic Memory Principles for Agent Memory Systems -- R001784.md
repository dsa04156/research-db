---
type: research-source
item_id: 1784
title: "Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems"
source: "arxiv"
published: "2026-08-05T12:12:44Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.04746"
url: "https://arxiv.org/abs/2608.04746v1"
generated_by: codex-research-db
aliases:
  - "Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems"
topics:
  - "ai-agents"
---

# Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems

[원문 열기](https://arxiv.org/abs/2608.04746v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TS62GWXA`)
- 발행일: 2026-08-05T12:12:44Z
- 저자: Kartikey Singh Bhandari, Aarya Wadhwani, Dhruv Kumar, Pratik Narang
- 식별자: `arxiv:2608.04746`

## 요약·초록

LLM agents that persist across sessions accumulate stored memories whose validity varies enormously by content type, yet existing memory architectures treat all memories as equally persistent and systematically contaminate retrieved context with outdated facts. We show that per-memory, type-conditioned temporal decay, a property of western scrub jay episodic memory, can be operationalized as an auto-classified coefficient $π_i$ in an external LLM-agent memory store, yielding ScrubJay-MEM: each memory is encoded as a jointly-bound What--Where--When tuple with an estimated perishability $π_i$ and utility horizon $τ_i$, retrieved by query-adaptive scoring, and revised retroactively at $O(1)$ LLM calls per update. We introduce the Temporal Generalization Test (TGT), a benchmark with held-out retention intervals and a Generalization Gap (GenGap) metric. On TGT, ScrubJay-MEM is the only retrieval-based system with substantially positive GenGap ($+0.108$); on MemoryAgentBench EventQA-64k it improves F1 by $+2.66$ over Mem0 and $+3.09$ over Qwen3-Embedding-4B under a llm backbone. A decay ablation collapses GenGap by $5.7\times$, establishing type-conditioned decay as necessary for the result. Gains narrow under stronger backbones and reverse on fact-consolidation tasks, scoping the contribution to temporal reasoning over perishable facts.

## 내 메모


