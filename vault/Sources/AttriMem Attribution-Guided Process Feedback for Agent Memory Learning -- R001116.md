---
type: research-source
item_id: 1116
title: "AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning"
source: "arxiv"
published: "2026-07-23T09:35:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.21106"
url: "https://arxiv.org/abs/2607.21106v1"
generated_by: codex-research-db
aliases:
  - "AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning"
topics:
  - "ai-agents"
---

# AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning

[원문 열기](https://arxiv.org/abs/2607.21106v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NVDTHJC8`)
- 발행일: 2026-07-23T09:35:34Z
- 저자: Qinfeng Li, Yuntai Bao, Xinyan Yu, Hongze Chen, Wenqi Zhang, Xuhong Zhang
- 식별자: `arxiv:2607.21106`

## 요약·초록

Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging. A memory-construction policy decides what information to extract, store, update, compress, or discard as interactions accumulate. Heuristic memory methods rely on subjective, task-specific rules, which can misalign with downstream objectives and limit cross-task adaptability. RL-based methods, by contrast, learn from task feedback but mainly use outcome- or module-level rewards. These coarse signals indicate task success but cannot identify which intermediate memory contents support the final answer, creating a fine-grained credit-assignment bottleneck. However, constructing such process feedback is prohibitively difficult because intermediate memory decisions lack unique ground-truth targets, while the appropriate credit varies with the agent's uncertain reasoning trajectory and therefore cannot be specified in advance. We propose AttriMem, an attribution-guided process-feedback framework for learning memory-construction policies with RL. AttriMem augments the global outcome reward with local rewards derived from token-level contributions to the final answer. Experiments on long-horizon dialogue question answering show that AttriMem outperforms retrieval-based, heuristic, and RL-based baselines, generalizes across benchmarks and answer models, stabilizes RL optimization.

## 내 메모


