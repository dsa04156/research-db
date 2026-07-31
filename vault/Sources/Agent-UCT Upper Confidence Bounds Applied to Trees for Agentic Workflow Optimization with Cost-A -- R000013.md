---
type: research-source
item_id: 13
title: "Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness"
source: "arxiv"
published: "2026-07-27T08:41:18Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.24162"
url: "https://arxiv.org/abs/2607.24162v2"
generated_by: codex-research-db
aliases:
  - "Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness"
topics:
  - "self-evolving-harness"
---

# Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness

[원문 열기](https://arxiv.org/abs/2607.24162v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`X6GIRGFH`)
- 발행일: 2026-07-27T08:41:18Z
- 저자: Yang Li, Hai Liu, Dian Shao, Yu Wang, Xiyu Chen, Sergey Volkov, Bozhi Wang, Ziyu Sun, Sihang Liu, Ye Luo, Xiaowei Zhang
- 식별자: `arxiv:2607.24162`

## 요약·초록

Optimizing agentic workflows, such as retrieval-augmented generation (RAG) pipelines, requires navigating a combinatorial space of discrete component choices under tight evaluation budgets. Existing approaches - heuristic search, black-box optimization, and standard tree search methods - do not explicitly exploit the compositional structure of these workflows, leading to redundant computation and inefficient budget allocation. We introduce Agent-UCT (Agent-based Cost-Aware Upper Confidence Bounds Applied to Trees), a tree search algorithm that extends UCT with a reuse-aware regularization term derived from a bipartite prefix reuse graph. Agent-UCT biases selection toward branches that leverage previously materialized configuration prefixes, reducing redundant execution while maintaining effective exploration. Our framework, RAGSpace, unifies heterogeneous RAG components from LongRAG, LightRAG, and Self-RAG into a five-dimensional configuration space, enabling systematic cross-framework recombination. WTB (Workflow Test Bench) provides deterministic replay, content-addressable caching, and transactional consistency, ensuring that intermediate states are materialized once and reused across the search. Experiments on HotpotQA and UltraDomain demonstrate that Agent-UCT identifies configurations with the highest out-of-sample performance among the evaluated fixed framework presets. Under full-pool evaluation, bipartite prefix reuse reduces logical search cost by 73.6% relative to the no-prefix-sharing cost upper bound. Compared with full-pool evaluation, sampling-based evaluation further achieves a 4.2x wall-clock speedup. Agent-UCT, RAGSpace, and WTB together provide a unified framework for cost-aware, reproducible, and compositionally efficient agentic workflow optimization.

## 내 메모


