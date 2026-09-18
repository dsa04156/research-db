---
type: research-source
item_id: 2899
title: "Efficiently Linking Unstructured Data for Multi-step Reasoning"
source: "arxiv"
published: "2026-09-16T23:16:45Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.19491"
url: "https://arxiv.org/abs/2609.19491v1"
generated_by: codex-research-db
aliases:
  - "Efficiently Linking Unstructured Data for Multi-step Reasoning"
topics:
  - "ai-agents"
---

# Efficiently Linking Unstructured Data for Multi-step Reasoning

[원문 열기](https://arxiv.org/abs/2609.19491v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`W4TB9SBI`)
- 발행일: 2026-09-16T23:16:45Z
- 저자: Jiaming Liang, Haydn Jones, Jacob R. Gardner, Mark Yatskar, Zachary Ives
- 식별자: `arxiv:2609.19491`

## 요약·초록

Modern LLMs and AI agents increasingly support data engineering workflows that integrate evidence from unstructured sources. Such pipelines typically do data retrieval, integration, and ranking before proceeding to more complex agentic reasoning or actions, e.g., for scientific discovery. The core retrieval problem in these workflows jointly executes multi-attribute filtering, multi-vector search, exact relational joins, and thresholded embedding-similarity joins. Given a planned query and monotone scoring function, our DASE query engine constructs and ranks candidate evidence tuples. It comprises (i) a multi-step reasoning query model over structured predicates, multiple vectors, and relational links; (ii) SemJI, a sparse materialized embedding-similarity join index for rare near-neighbor pairs; and (iii) a co-designed execution layer that combines predicate-aware ANN traversal, batched access, and threshold-based score aggregation. On scientific-discovery workloads, DASE retrieves candidate evidence for multi-step reasoning queries 6x to 46x faster than strong RDBMS, rerank, and vector-database baselines at comparable recall; and for tasks that require semantic-operator post-processing, DASE acts as a high-recall prefilter that makes downstream LLM evaluation both cheaper and more accurate -- e.g., on SemBench E-Commerce it improves BigQuery quality from 0.67 to 0.80 while cutting cost from $2.42 to $0.54.

## 내 메모


