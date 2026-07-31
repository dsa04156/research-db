---
type: research-source
item_id: 1288
title: "A Poly-Log Approximation for Transaction Scheduling in Fog-Cloud Computing and Beyond"
source: "arxiv"
published: "2025-11-12T22:13:46Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2511.09776"
url: "https://arxiv.org/abs/2511.09776v1"
generated_by: codex-research-db
aliases:
  - "A Poly-Log Approximation for Transaction Scheduling in Fog-Cloud Computing and Beyond"
topics:
  - "cloud-infrastructure"
---

# A Poly-Log Approximation for Transaction Scheduling in Fog-Cloud Computing and Beyond

[원문 열기](https://arxiv.org/abs/2511.09776v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`QK4QRSPH`)
- 발행일: 2025-11-12T22:13:46Z
- 저자: Ramesh Adhikari, Costas Busch, Pavan Poudel
- 식별자: `arxiv:2511.09776`

## 요약·초록

Transaction scheduling is crucial to efficiently allocate shared resources in a conflict-free manner in distributed systems. We investigate the efficient scheduling of transactions in a network of fog-cloud computing model, where transactions and their associated shared objects can move within the network. The schedule may require objects to move to transaction nodes, or the transactions to move to the object nodes. Moreover, the schedule may determine intermediate nodes where both objects and transactions meet. Our goal is to minimize the total combined cost of the schedule. We focus on networks of constant doubling dimension, which appear frequently in practice. We consider a batch problem where an arbitrary set of nodes has transactions that need to be scheduled. First, we consider a single shared object required by all the transactions and present a scheduling algorithm that gives an $O(\log n \cdot \log D)$ approximation of the optimal schedule, where $n$ is the number of nodes and $D$ is the diameter of the network. Later, we consider transactions accessing multiple shared objects (at most $k$ objects per transaction) and provide a scheduling algorithm that gives an $O(k \cdot \log n \cdot \log D)$ approximation. We also provide a fully distributed version of the scheduling algorithms where the nodes do not need global knowledge of transactions.

## 내 메모


