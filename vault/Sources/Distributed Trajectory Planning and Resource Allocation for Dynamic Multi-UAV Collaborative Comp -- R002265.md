---
type: research-source
item_id: 2265
title: "Distributed Trajectory Planning and Resource Allocation for Dynamic Multi-UAV Collaborative Computing"
source: "arxiv"
published: "2026-08-24T11:32:17Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.23123"
url: "https://arxiv.org/abs/2608.23123v1"
generated_by: codex-research-db
aliases:
  - "Distributed Trajectory Planning and Resource Allocation for Dynamic Multi-UAV Collaborative Computing"
topics:
  - "ai-agents"
  - "edge-computing"
---

# Distributed Trajectory Planning and Resource Allocation for Dynamic Multi-UAV Collaborative Computing

[원문 열기](https://arxiv.org/abs/2608.23123v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-24T11:32:17Z
- 저자: Tiankui Zhang, Wenlong Xu, Tianyi Shi, Xiaoxia Xu, Arumugam Nallanathan
- 식별자: `arxiv:2608.23123`

## 요약·초록

This paper investigates a multiple uncrewed aerial vehicles (UAVs)-enabled distributed mobile edge computing (MEC) framework, where the set of collaborative UAVs dynamically varies over time due to their energy states and service loads. The joint optimization of trajectory planning and resource allocation is formulated as a Stackelberg game, where UAVs and mobile terminals (MTs) are modeled as leaders and followers, respectively. UAVs aim to maximize their benefits by balancing executed workload, energy cost, and resource allocation revenue, while MTs seek to minimize their total overhead, composed of computing delay and resource costs, through offloading and resource-request decisions. A hierarchical joint optimization algorithm is developed within a multi-agent deep reinforcement learning (MADRL) framework to coordinate UAVs and MTs in a distributed manner. At the leader level, UAVs jointly determine their trajectories, task migration ratios, MT-UAV association, and unit computing resource pricing. Each UAV is modeled as an agent in a partially observable Markov decision process, and the agents are jointly trained via multi-agent proximal policy optimization (MAPPO) under the centralized-training-and-decentralized-execution paradigm. At the follower level, MTs determine their optimal task offloading ratios and requested computing resources using a two-stage iterative algorithm. Simulation results demonstrate stable convergence under dynamic UAV participation. Compared to the no-collaboration benchmark, the proposed algorithm improves UAV efficiency by 18.58% through inter-UAV task migration and reduces average MT overhead by 33.77% over the fully offloading scheme. It also outperforms other benchmarks under varying network scales and capabilities by jointly optimizing UAV operations and resource utilization.

## 내 메모
