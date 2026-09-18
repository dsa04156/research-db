---
type: research-source
item_id: 2896
title: "Self-Evolving Search Index"
source: "arxiv"
published: "2026-09-17T03:56:03Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.19656"
url: "https://arxiv.org/abs/2609.19656v1"
generated_by: codex-research-db
aliases:
  - "Self-Evolving Search Index"
topics:
  - "ai-agents"
---

# Self-Evolving Search Index

[원문 열기](https://arxiv.org/abs/2609.19656v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2JIFBPWM`)
- 발행일: 2026-09-17T03:56:03Z
- 저자: Sangam Lee, Wonjae Lee, Sunghwan Kim, Deogyong Kim, Jaehoon Kim, Daye Nam, SeongKu Kang, Dongha Lee
- 식별자: `arxiv:2609.19656`

## 요약·초록

Information retrieval is increasingly important as LLM agents tackle complex tasks involving diverse information needs. Because retrieval relies on an index that represents each document through index keys, retrieval quality depends heavily on how effectively these keys expose the knowledge contained in each document. However, effective index representations vary across retrieval environments, making it difficult for any fixed optimization strategy to perform consistently. Yet evolving an index to its retrieval environment remains largely human-driven, requiring humans to diagnose retrieval failures, refine the optimization strategy, and reprocess the index accordingly. We propose SELF-INDEX, a framework that enables an index to self-evolve without human intervention. Its Optimizer autonomously diagnoses retrieval shortfalls, selectively revises the responsible index keys, and validates each revision before updating the index. Beyond reacting to observed retrieval demands, SELF-INDEX proactively explores additional demands through a Query Simulator, allowing the index to evolve beyond the queries already available for optimization. Across diverse corpora and retrievers, SELF-INDEX consistently improves retrieval performance while outperforming existing index optimization methods. We further show that these benefits extend to downstream applications, improving the effectiveness and efficiency of search agents and helping agent memory systems retrieve useful past interactions.

## 내 메모


