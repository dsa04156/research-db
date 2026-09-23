---
type: research-source
item_id: 2969
title: "Graph neural network-based service migration decision in vehicular networks"
source: "openalex"
published: "2026-09-19"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-71909-0"
url: "https://doi.org/10.1038/s41598-026-71909-0"
generated_by: codex-research-db
aliases:
  - "Graph neural network-based service migration decision in vehicular networks"
topics:
  - "edge-computing"
---

# Graph neural network-based service migration decision in vehicular networks

[원문 열기](https://doi.org/10.1038/s41598-026-71909-0)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`DPXS5MZM`)
- 발행일: 2026-09-19
- 저자: L. Wang, Xianfeng Zheng, Liang Liu, Hao Feng, Wenwei Li, Huan Liu
- 식별자: `doi:10.1038/s41598-026-71909-0`

## 요약·초록

Abstract The rapid development of the Internet of Vehicles (IoV) has led to an exponential increase in the number of latency sensitive and computationally intensive tasks. Due to the limitations of onboard computing resources in vehicles, offloading these tasks generated during vehicle operation to a remote cloud for processing inevitably leads to significant transmission delays. By combining the IoV with Mobile Edge Computing (MEC), these latency sensitive and computationally intensive tasks can be processed in MEC server to reduce energy consumption of vehicles and the transmission delay of tasks. However, due to the small coverage area of MEC servers and the mobility of vehicles, it may cause vehicles using MEC services to leave the coverage area of current MEC servers, resulting in service interruptions. How to dynamically migrate tasks for ensuring service continuity is a great challenge. In this paper, we study service migration strategies in dynamic and complex IoV MEC environments. We first model the service migration strategies as a multi-objective optimization problem that minimizes the weighted sum of latency and energy consumption. We then transform the problem into a Markov Decision Process (MDP). To capture time-varying server loads and link-state features over the physical RSU graph, a Graph Convolutional Network (GCN) is employed to extract features from the network topology and node information in the vehicular edge network, and a graph convolutional neural network-based deep reinforcement learning task migration decision algorithm (Gr-MiD) is proposed to make service migration decisions based on task details. Simulation results in a small synthetic intra-zone IoV-MEC setting demonstrate that the Gr-MiD algorithm outperforms existing comparative algorithms, achieving an 8.04% reduction in average task delay and a 15.82% reduction in average task energy consumption compared to the DQN baseline under peak-load conditions.

## 내 메모
