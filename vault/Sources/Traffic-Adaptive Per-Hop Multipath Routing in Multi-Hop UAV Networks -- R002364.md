---
type: research-source
item_id: 2364
title: "Traffic-Adaptive Per-Hop Multipath Routing in Multi-Hop UAV Networks"
source: "arxiv"
published: "2026-08-26T05:17:10Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25383"
url: "https://arxiv.org/abs/2608.25383v1"
generated_by: codex-research-db
aliases:
  - "Traffic-Adaptive Per-Hop Multipath Routing in Multi-Hop UAV Networks"
topics:
  - "edge-computing"
---

# Traffic-Adaptive Per-Hop Multipath Routing in Multi-Hop UAV Networks

[원문 열기](https://arxiv.org/abs/2608.25383v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FMFQJGBM`)
- 발행일: 2026-08-26T05:17:10Z
- 저자: Zhenyu Zhao, Tiankui Zhang, Xiaoxia Xu, Yuanpeng Zheng, Junjie Li, Wenjuan Xing
- 식별자: `arxiv:2608.25383`

## 요약·초록

In uncrewed aerial vehicle (UAV)-relayed mobile edge computing (MEC) networks, computation tasks generate traffic with diverse latency requirements and data sizes. Routing decisions therefore need to adapt to both traffic characteristics and changing network conditions. Compared with single-path routing, multipath routing is better suited to such heterogeneous traffic because it provides multiple forwarding options and enables flexible traffic splitting. However, conventional multipath routing usually splits traffic over predefined end-to-end paths, making it difficult to respond quickly to link fluctuations and topology changes in UAV networks. To address this issue, we propose a traffic-adaptive per-hop multipath routing method for multi-hop UAV networks, in which each UAV dynamically distributes traffic among multiple candidate next hops. We formulate the routing problem to improve the on-time packet delivery ratio while reducing the packet loss ratio, and model it as a decentralized partially observable Markov decision process (Dec-POMDP). To solve this problem, we develop a multi-agent reinforcement learning (MARL) algorithm, termed Multi-Agent Proximal Policy Optimization with Dirichlet Modeling (MAPPO-DM). MAPPO-DM follows the centralized-training-and-decentralized-execution framework and models continuous traffic-splitting actions using a Dirichlet distribution. Simulation results show that MAPPO-DM outperforms the baseline methods and maintains robust performance under various network conditions.

## 내 메모


