---
type: research-source
item_id: 1730
title: "ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG"
source: "arxiv"
published: "2026-08-02T14:22:31Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01269"
url: "https://arxiv.org/abs/2608.01269v1"
generated_by: codex-research-db
aliases:
  - "ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG"
topics:
  - "self-evolving-harness"
---

# ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG

[원문 열기](https://arxiv.org/abs/2608.01269v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2NKRXFKI`)
- 발행일: 2026-08-02T14:22:31Z
- 저자: Yongfeng Huang, Yuren Lai, Ruiying Chen, Haoyu Huang, Mingming Zhao, James Cheng
- 식별자: `arxiv:2608.01269`

## 요약·초록

Hierarchical Graph Retrieval-Augmented Generation (GraphRAG) organizes corpus knowledge at multiple levels of granularity, yet fixed context construction may fail to translate these multi-resolution representations into a context suited to the current query. We identify this mismatch as the representation--inference gap. We propose Agentic Context Engineering for Hierarchical GraphRAG (ACE-GraphRAG), an inference-time context policy layer that supplements and adapts the initial context for generation. ACE-GraphRAG formulates context construction as a policy over gap-aware refinement, retrieval branches, and task-conditioned adaptation. Parallel Differential Retrieval acquires supplementary evidence from depth-oriented factual and breadth-oriented semantic branches. These evidence increments are consolidated with the initial context while preserving provenance and abstraction levels. Full-ACE applies the full policy uniformly within each task family, whereas Adaptive-ACE selects task- and topology-specific policies for individual queries. We evaluate ACE-GraphRAG on HotpotQA, 2WikiMultiHopQA, and four UltraDomain subsets across multi-hop QA and query-focused summarization. Full-ACE outperforms the evaluated RAG and GraphRAG baselines across both task families, while Adaptive-ACE further improves multi-hop QA and is preferred over Full-ACE on all four UltraDomain subsets. Ablation and topology analyses support treating context construction as a query- and task-dependent inference policy rather than a fixed procedure.

## 내 메모


