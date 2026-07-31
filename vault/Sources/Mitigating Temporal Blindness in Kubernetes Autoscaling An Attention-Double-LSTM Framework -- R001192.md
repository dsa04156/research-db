---
type: research-source
item_id: 1192
title: "Mitigating Temporal Blindness in Kubernetes Autoscaling: An Attention-Double-LSTM Framework"
source: "arxiv"
published: "2026-03-21T10:03:53Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.28790"
url: "https://arxiv.org/abs/2603.28790v1"
generated_by: codex-research-db
aliases:
  - "Mitigating Temporal Blindness in Kubernetes Autoscaling: An Attention-Double-LSTM Framework"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
  - "edge-computing"
---

# Mitigating Temporal Blindness in Kubernetes Autoscaling: An Attention-Double-LSTM Framework

[원문 열기](https://arxiv.org/abs/2603.28790v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`EZRZHN4Z`)
- 발행일: 2026-03-21T10:03:53Z
- 저자: Faraz Shaikh, Gianluca Reali, Mauro Femminella
- 식별자: `arxiv:2603.28790`

## 요약·초록

In the emerging landscape of edge computing, the stochastic and bursty nature of serverless workloads presents a critical challenge for autonomous resource orchestration. Traditional reactive controllers, such as the Kubernetes Horizontal Pod Autoscaler (HPA), suffer from inherent reaction latency, leading to Service Level Objective (SLO) violations during traffic spikes and resource flapping during ramp-downs. While Deep Reinforcement Learning (DRL) offers a pathway toward proactive management, standard agents suffer from temporal blindness, an inability to effectively capture long-term dependencies in non-Markovian edge environments. To bridge this gap, we propose a novel stability-aware autoscaling framework unifying workload forecasting and control via an Attention-Enhanced Double-Stacked LSTM architecture integrated within a Proximal Policy Optimization (PPO) agent. Unlike shallow recurrent models, our approach employs a deep temporal attention mechanism to selectively weight historical states, effectively filtering high-frequency noise while retaining critical precursors of demand shifts. We validate the framework on a heterogeneous cluster using real-world Azure Functions traces. Comparative analysis against industry-standard HPA, stateless Double DQN, and a single-layer LSTM ablation demonstrates that our approach reduces 90th percentile latency by approximately 29% while simultaneously decreasing replica churn by 39%, relative to the single-layer LSTM baseline. These results confirm that mitigating temporal blindness through deep attentive memory is a prerequisite for reliable, low-jitter autoscaling in production edge environments.

## 내 메모


