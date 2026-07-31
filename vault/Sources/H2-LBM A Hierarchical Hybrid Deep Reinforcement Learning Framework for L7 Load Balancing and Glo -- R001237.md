---
type: research-source
item_id: 1237
title: "H2-LBM: A Hierarchical Hybrid Deep Reinforcement Learning Framework for L7 Load Balancing and Global Traffic Scheduling in Multi-Cloud LLM Serving"
source: "openalex"
published: "2026-06-25"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.66238/fsrma98"
url: "https://doi.org/10.66238/fsrma98"
generated_by: codex-research-db
aliases:
  - "H2-LBM: A Hierarchical Hybrid Deep Reinforcement Learning Framework for L7 Load Balancing and Global Traffic Scheduling in Multi-Cloud LLM Serving"
topics:
  - "cloud-infrastructure"
  - "kubernetes"
---

# H2-LBM: A Hierarchical Hybrid Deep Reinforcement Learning Framework for L7 Load Balancing and Global Traffic Scheduling in Multi-Cloud LLM Serving

[원문 열기](https://doi.org/10.66238/fsrma98)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`CDZ6FKRB`)
- 발행일: 2026-06-25
- 저자: Chengde Xu, Chongye Wang, Zeyu Li
- 식별자: `doi:10.66238/fsrma98`

## 요약·초록

Large Language Model (LLM) inference services are increasingly deployed across multi-cloud infrastructures to support latency-sensitive applications such as conversational AI, intelligent search, and real-time analytics. However, the coexistence of heterogeneous computing resources, geographically distributed data centers, and highly dynamic request patterns poses significant challenges to efficient L7 load balancing and global traffic scheduling. In particular, traditional rule-based or heuristic-driven approaches fail to capture the semantic variability of LLM workloads, including token length diversity and non-linear inference latency, leading to suboptimal resource utilization and degraded tail latency performance. To address these issues, this paper proposes H2-LBM, a hierarchical hybrid deep reinforcement learning framework designed for multi-cloud LLM serving environments. The framework decomposes the scheduling problem into two coordinated levels: a global scheduler based on Proximal Policy Optimization (PPO) for cross-cloud traffic allocation, and a local scheduler based on Double Dueling Deep Q-Network (D3QN) for fine-grained L7 request dispatching. By incorporating semantic-aware state representations and a multi-objective reward function that jointly optimizes latency, throughput, and resource efficiency, H2-LBM enables adaptive and scalable decision-making under dynamic workloads. Experimental results on a multi-cloud Kubernetes testbed show that H2-LBM reduces P99 latency by 21.5%–29.2% compared with strong baselines such as Kubernetes HPA across moderate and burst workloads. Specifically, P99 latency decreases from 360 ms to 255 ms under moderate load and from 650 ms to 510 ms under high load. These results consistently validate the effectiveness of H2-LBM in improving latency stability and system efficiency for large-scale LLM inference services.

## 내 메모


