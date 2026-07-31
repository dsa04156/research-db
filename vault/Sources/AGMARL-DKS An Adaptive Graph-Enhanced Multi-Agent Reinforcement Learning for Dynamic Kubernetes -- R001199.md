---
type: research-source
item_id: 1199
title: "AGMARL-DKS: An Adaptive Graph-Enhanced Multi-Agent Reinforcement Learning for Dynamic Kubernetes Scheduling"
source: "arxiv"
published: "2026-03-12T15:09:48Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.12031"
url: "https://arxiv.org/abs/2603.12031v2"
generated_by: codex-research-db
aliases:
  - "AGMARL-DKS: An Adaptive Graph-Enhanced Multi-Agent Reinforcement Learning for Dynamic Kubernetes Scheduling"
topics:
  - "kubernetes"
  - "ai-agents"
---

# AGMARL-DKS: An Adaptive Graph-Enhanced Multi-Agent Reinforcement Learning for Dynamic Kubernetes Scheduling

[원문 열기](https://arxiv.org/abs/2603.12031v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3FFJ326F`)
- 발행일: 2026-03-12T15:09:48Z
- 저자: Hamed Hamzeh
- 식별자: `arxiv:2603.12031`

## 요약·초록

State-of-the-art cloud-native applications require intelligent schedulers that can effectively balance system stability, resource utilisation, and associated costs. While Kubernetes provides feasibility-based placement by default, recent research efforts have explored the use of reinforcement learning (RL) for more intelligent scheduling decisions. However, current RL-based schedulers have three major limitations. First, most of these schedulers use monolithic centralised agents, which are non-scalable for large heterogeneous clusters. Second, the ones that use multi-objective reward functions assume simple, static, linear combinations of the objectives. Third, no previous work has produced a stress-aware scheduler that can react adaptively to dynamic conditions. To address these gaps in current research, we propose the Adaptive Graph-enhanced Multi-Agent Reinforcement Learning Dynamic Kubernetes Scheduler (AGMARL-DKS). AGMARL-DKS addresses these gaps by introducing three major innovations. First, we construct a scalable solution by treating the scheduling challenge as a cooperative multi-agent problem, where every cluster node operates as an agent, employing centralised training methods before decentralised execution. Second, to be context-aware and yet decentralised, we use a Graph Neural Network (GNN) to build a state representation of the global cluster context at each agent. This represents an improvement over methods that rely solely on local observations. Finally, to make trade-offs between these objectives, we use a stress-aware lexicographical ordering policy instead of a simple, static linear weighting of these objectives. The evaluations in Google Kubernetes Engine (GKE) reveal that AGMARL-DKS significantly outperforms the default scheduler in terms of fault tolerance, utilisation, and cost, especially in scheduling batch and mission-critical workloads.

## 내 메모


