---
type: research-source
item_id: 3050
title: "MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents"
source: "arxiv"
published: "2026-09-21T08:22:21Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.24259"
url: "https://arxiv.org/abs/2609.24259v1"
generated_by: codex-research-db
aliases:
  - "MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents"
topics:
  - "ai-agents"
---

# MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents

[원문 열기](https://arxiv.org/abs/2609.24259v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T08:22:21Z
- 저자: Ruike Cao, Fanyu Zhao, Fugen Yao, Liang Dong, Jian Xu, Guanjun Jiang, Yifei Zhao, Han Zhang, Li Xiao
- 식별자: `arxiv:2609.24259`

## 요약·초록

The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system scenarios for evaluating memory use and advancing optimization algorithms. Results on the MemCalib test set reveal that frontier open- and closed-source models struggle to use memory appropriately. They frequently over-use or under-use memory rather than matching each proposition's actual use to its target level, leading to biased, low-quality responses. Experiments with common post-training algorithms, including group relative policy optimization and on-policy self-distillation, further reveal a clear directional skew: trained models improve in one direction while deteriorating in the other. We therefore propose MemCalib-RL, an ordered bidirectional counterfactual credit-assignment algorithm that separates over- and under-use signals and localizes their credit to response tokens through exact atom ablation. Results across model families and scales (Qwen3-8B, Ministral-3-8B-Instruct, and Qwen3.5-35B-A3B) show that MemCalib-RL achieves the best overall performance while better balancing over-use and under-use, with gains generalizing beyond MemCalib in external benchmark evaluation. Further experiments support its design choices and robustness and provide insight into its training dynamics.

## 내 메모
