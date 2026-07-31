---
type: research-source
item_id: 1376
title: "Multi-Turn Reasoning LLMs for Task Offloading in Mobile Edge Computing"
source: "arxiv"
published: "2026-04-08T14:38:48Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.07148"
url: "https://arxiv.org/abs/2604.07148v1"
generated_by: codex-research-db
aliases:
  - "Multi-Turn Reasoning LLMs for Task Offloading in Mobile Edge Computing"
topics:
  - "edge-computing"
---

# Multi-Turn Reasoning LLMs for Task Offloading in Mobile Edge Computing

[원문 열기](https://arxiv.org/abs/2604.07148v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZI99FFIH`)
- 발행일: 2026-04-08T14:38:48Z
- 저자: Ning Yang, Chuangxin Cheng, Haijun Zhang
- 식별자: `arxiv:2604.07148`

## 요약·초록

Emerging computation-intensive applications impose stringent latency requirements on resource-constrained mobile devices. Mobile Edge Computing (MEC) addresses this challenge through task offloading. However, designing effective policies remains difficult due to dynamic task arrivals, time-varying channels, and the spatio-temporal coupling of server queues. Conventional heuristics lack adaptability, while Deep Reinforcement Learning (DRL) suffers from limited generalization and architectural rigidity, requiring retraining when network topology changes. Although Large Language Models (LLMs) offer semantic reasoning capabilities, standard Supervised Fine-Tuning (SFT) yields myopic policies that greedily minimize immediate latency without accounting for long-term system evolution. To address these limitations, we propose COMLLM, a generative framework that enables foresighted decision-making in MEC systems. COMLLM integrates Group Relative Policy Optimization (GRPO) with a Look-Ahead Collaborative Simulation (LACS) mechanism, which performs multi-step Monte Carlo rollouts while jointly modeling server queue dynamics. By incorporating these rollouts into the reward design, the framework captures the long-term impact of current decisions on future system states. Experimental results demonstrate that COMLLM achieves near-optimal latency and improved load-balancing fairness. Notably, it exhibits zero-shot topological scalability, allowing a model trained on small-scale networks to generalize to larger, unseen topologies without retraining, outperforming SFT, DRL, and heuristic baselines.

## 내 메모


