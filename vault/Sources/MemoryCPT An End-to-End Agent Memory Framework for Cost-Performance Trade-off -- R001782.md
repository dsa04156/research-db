---
type: research-source
item_id: 1782
title: "MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off"
source: "arxiv"
published: "2026-08-05T13:37:08Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.04843"
url: "https://arxiv.org/abs/2608.04843v1"
generated_by: codex-research-db
aliases:
  - "MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off"
topics:
  - "ai-agents"
---

# MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off

[원문 열기](https://arxiv.org/abs/2608.04843v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2VPMDQF4`)
- 발행일: 2026-08-05T13:37:08Z
- 저자: Songxin Lei, Kun Ouyang, Weilin Ruan, Yuqian Wu, Zhijiang Guo, Yushi Sun, Fugee Tsung
- 식별자: `arxiv:2608.04843`

## 요약·초록

Long-horizon LLM agents require memory systems that recover useful evidence from large interaction histories without passing excessive context to downstream models. Existing memory pipelines often rely on hand-crafted heuristics and repeated LLM calls, which can introduce redundant context and high inference cost. We propose MemoryCPT, an end-to-end trainable agent memory pipeline that spans offline memory construction and online query-conditioned context generation. MemoryCPT consists of two stages: Query-agnostic Distillation (QAD), which distills a modular memory-construction pipeline into a compact model using explicit reasoning traces; and Query-aware Retrieval and Summarization (QAR), which combines reciprocal rank fusion (RRF) with a LoRA-based summarizer trained via Group Relative Policy Optimization (GRPO) under a cost-aware reward. We further introduce Quality per Cost (QPC) to quantify answer quality per unit inference cost. Experiments on LoCoMo and LongMemEval show that MemoryCPT improves the cost-performance trade-off over the evaluated baselines, while ablation and sensitivity analyses characterize the contributions of its components and the effects of key design choices.

## 내 메모


