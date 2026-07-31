---
type: research-source
item_id: 940
title: "GraphEdge: Dynamic Graph Partition and Task Scheduling for GNNs Computing in Edge Network"
source: "arxiv"
published: "2025-04-22T13:45:13Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2504.15905"
url: "https://arxiv.org/abs/2504.15905v1"
generated_by: codex-research-db
aliases:
  - "GraphEdge: Dynamic Graph Partition and Task Scheduling for GNNs Computing in Edge Network"
topics:
  - "edge-computing"
---

# GraphEdge: Dynamic Graph Partition and Task Scheduling for GNNs Computing in Edge Network

[원문 열기](https://arxiv.org/abs/2504.15905v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NB2GH8M2`)
- 발행일: 2025-04-22T13:45:13Z
- 저자: Wenjing Xiao, Chenglong Shi, Miaojiang Chen, Zhiquan Liu, Min Chen, H. Herbert Song
- 식별자: `arxiv:2504.15905`

## 요약·초록

With the exponential growth of Internet of Things (IoT) devices, edge computing (EC) is gradually playing an important role in providing cost-effective services. However, existing approaches struggle to perform well in graph-structured scenarios where user data is correlated, such as traffic flow prediction and social relationship recommender systems. In particular, graph neural network (GNN)-based approaches lead to expensive server communication cost. To address this problem, we propose GraphEdge, an efficient GNN-based EC architecture. It considers the EC system of GNN tasks, where there are associations between users and it needs to take into account the task data of its neighbors when processing the tasks of a user. Specifically, the architecture first perceives the user topology and represents their data associations as a graph layout at each time step. Then the graph layout is optimized by calling our proposed hierarchical traversal graph cut algorithm (HiCut), which cuts the graph layout into multiple weakly associated subgraphs based on the aggregation characteristics of GNN, and the communication cost between different subgraphs during GNN inference is minimized. Finally, based on the optimized graph layout, our proposed deep reinforcement learning (DRL) based graph offloading algorithm (DRLGO) is executed to obtain the optimal offloading strategy for the tasks of users, the offloading strategy is subgraph-based, it tries to offload user tasks in a subgraph to the same edge server as possible while minimizing the task processing time and energy consumption of the EC system. Experimental results show the good effectiveness and dynamic adaptation of our proposed architecture and it also performs well even in dynamic scenarios.

## 내 메모


