---
type: research-source
item_id: 1123
title: "Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking"
source: "arxiv"
published: "2026-07-22T04:45:10Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19747"
url: "https://arxiv.org/abs/2607.19747v2"
generated_by: codex-research-db
aliases:
  - "Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking"
topics:
  - "ai-agents"
---

# Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking

[원문 열기](https://arxiv.org/abs/2607.19747v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6VIPMHMC`)
- 발행일: 2026-07-22T04:45:10Z
- 저자: Kailin Jiang, Lei Liu, Jian Xi, Hui Xu, Junlin Liu, Baochen Fu, Bin Li, Vichwang, Yu Lu, Haibo Shi
- 식별자: `arxiv:2607.19747`

## 요약·초록

As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream generation. Yet existing evaluation systems remain confined to scoring documents independently and aggregating via nDCG, ignoring inter-document interactions (redundancy, conflict, complementarity) and unable to answer what makes one document set better than another. To address these issues, we propose a complete evaluate-diagnose-optimize framework. We design SetwiseEvalKit, a three-level, nine-dimension document set evaluation benchmark covering both short-form and long-form scenarios, comprising approximately 28K high-quality evaluation rubrics. We systematically evaluate 12 rerankers: even the best method achieves no more than 45% coverage, cross-document coordination dimensions are universally weak, and no single method maintains top performance across both settings. Building on this, we propose Rubric4Setwise, a training-free method that converts rubric-based evaluation criteria into document set selection signals, achieving the best downstream generation performance with fewer documents and search rounds. It is the only method that maintains state-of-the-art results across both scenarios, validating the effectiveness of closing the loop from evaluation to optimization.

## 내 메모


