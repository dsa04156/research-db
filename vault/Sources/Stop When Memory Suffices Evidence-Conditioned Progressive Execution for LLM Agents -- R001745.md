---
type: research-source
item_id: 1745
title: "Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents"
source: "arxiv"
published: "2026-08-02T14:49:24Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01285"
url: "https://arxiv.org/abs/2608.01285v1"
generated_by: codex-research-db
aliases:
  - "Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents"
topics:
  - "ai-agents"
---

# Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents

[원문 열기](https://arxiv.org/abs/2608.01285v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2N86PETB`)
- 발행일: 2026-08-02T14:49:24Z
- 저자: Yidan Lin, Kaixiang Wang, Jiong Lou, Jie Li
- 식별자: `arxiv:2608.01285`

## 요약·초록

The continued development of LLMs toward persistent and adaptive intelligence increasingly requires long-term memory mechanisms that preserve and reuse information across interactions. Existing memory systems either compress and structure histories for efficient access or perform deep research over broader trajectories. The former lowers online cost but may omit temporal, causal, or cross-step dependencies, while the latter improves evidence coverage at substantial latency and inference cost. This raises a key question: can a memory system achieve strong answer quality while maintaining low online latency? We introduce Router-Mem, an evidence-conditioned progressive execution framework for long-horizon agent memory. Router-Mem first applies a shared low-cost retrieval prefix to obtain evidence. A lightweight sufficiency router then predicts whether the context supports early termination, which enable a single-token decision at inference time. It is trained with evidence-level supervision and rationale-conditioned representation distillation. When evidence is insufficient, Router-Mem reuses retrieval hits to expand memory blocks and perform deeper analysis and aggregation. Experiments on AMA-Bench and BEAM show that Router-Mem achieves 55.17\% and 38.77\% score while reducing average inference time by 27.3\% and 25.5\% compared with full memory execution.

## 내 메모


