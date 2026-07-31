---
type: research-source
item_id: 511
title: "Towards Multi-agent Reinforcement Learning based Traffic Signal Control through Spatio-temporal Hypergraphs"
source: "arxiv"
published: "2024-04-17T02:46:18Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/tmc.2025.3556243"
url: "https://arxiv.org/abs/2404.11014v2"
generated_by: codex-research-db
aliases:
  - "Towards Multi-agent Reinforcement Learning based Traffic Signal Control through Spatio-temporal Hypergraphs"
topics:
  - "ai-agents"
  - "edge-computing"
---

# Towards Multi-agent Reinforcement Learning based Traffic Signal Control through Spatio-temporal Hypergraphs

[원문 열기](https://arxiv.org/abs/2404.11014v2)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`AQZUQGNQ`)
- 발행일: 2024-04-17T02:46:18Z
- 저자: Kang Wang, Zhishu Shen, Zhen Lei, Tiehua Zhang
- 식별자: `doi:10.1109/tmc.2025.3556243`

## 요약·초록

Traffic signal control systems (TSCSs) are integral to intelligent traffic management, fostering efficient vehicle flow. Traditional approaches often simplify road networks into standard graphs, which results in a failure to consider the dynamic nature of traffic data at neighboring intersections, thereby neglecting higher-order interconnections necessary for real-time control. To address this, we propose a novel TSCS framework to realize intelligent traffic control. This framework collaborates with multiple neighboring edge computing servers to collect traffic information across the road network. To elevate the efficiency of traffic signal control, we have crafted a multi-agent soft actor-critic (MA-SAC) reinforcement learning algorithm. Within this algorithm, individual agents are deployed at each intersection with a mandate to optimize traffic flow across the road network collectively. Furthermore, we introduce hypergraph learning into the critic network of MA-SAC to enable the spatio-temporal interactions from multiple intersections in the road network. This method fuses hypergraph and spatio-temporal graph structures to encode traffic data and capture the complex spatio-temporal correlations between multiple intersections. Our empirical evaluation, tested on varied datasets, demonstrates the superiority of our framework in minimizing average vehicle travel times and sustaining high-throughput performance. This work facilitates the development of more intelligent urban traffic management solutions. We release the code to support the reproducibility of this work at https://github.com/Edun-Eyes/TSC

## 내 메모


