---
type: research-source
item_id: 1736
title: "Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training"
source: "arxiv"
published: "2026-08-03T15:34:45Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.02391"
url: "https://arxiv.org/abs/2608.02391v1"
generated_by: codex-research-db
aliases:
  - "Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training"
topics:
  - "ai-agents"
---

# Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training

[원문 열기](https://arxiv.org/abs/2608.02391v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`EU96G922`)
- 발행일: 2026-08-03T15:34:45Z
- 저자: Zhiyuan Wang, Shengcai Liu, Jiahao Wu, Ning Lu, Hui Ouyang, Shaofeng Zhang, Haoze Lv, Ke Tang
- 식별자: `arxiv:2608.02391`

## 요약·초록

Tool-using large language model (LLM) agents produce long, multi-turn trajectories, making gradient-based post-training memory-intensive. Evolution strategies (ES) enable memory-efficient full-parameter post-training without backpropagation and can eventually match the performance of gradient-based reinforcement learning (RL). However, resource-constrained settings typically offer only a few GPUs, so the high GPU-hour requirements of ES translate into prohibitively long training times. To address this, we introduce Cooperative Parameter-subspace Evolution Strategy (CoPES), a cooperative coevolutionary method that decomposes the full parameter space into lower-dimensional subspaces and searches over them cooperatively to improve optimization efficiency. We post-train a Qwen3.5-4B tool-using agent for the math task and evaluate it on five benchmarks of varying difficulty. Under the GPU-hour budget of full-parameter GRPO's best validation checkpoint, CoPES recovers 92% of GRPO's validation-accuracy gain, versus 67% for standard ES, while its theoretical GPU memory requirement is less than one-eighth that of full-parameter GRPO. It consistently outperforms standard ES and LoRA-based GRPO on all evaluated pass@k metrics across the five benchmarks. Additional experiments further show the advantage of CoPES on the question-answering task. These results demonstrate an improved trade-off between memory requirements and training time for agentic LLM post-training under resource constraints. The code is open-sourced in https://github.com/MetaronWang/CoPES

## 내 메모


