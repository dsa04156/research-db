---
type: research-source
item_id: 344
title: "Reinforcement Learning-based Task Scheduling for Heterogeneous Computing in End-Edge-Cloud Environment"
source: "openalex"
published: "2024-07-01"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.21203/rs.3.rs-4568055/v1"
url: "http://dx.doi.org/10.21203/rs.3.rs-4568055/v1"
generated_by: codex-research-db
aliases:
  - "Reinforcement Learning-based Task Scheduling for Heterogeneous Computing in End-Edge-Cloud Environment"
topics:
  - "kubernetes"
---

# Reinforcement Learning-based Task Scheduling for Heterogeneous Computing in End-Edge-Cloud Environment

[원문 열기](http://dx.doi.org/10.21203/rs.3.rs-4568055/v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`TUGEJBJP`)
- 발행일: 2024-07-01
- 저자: Wangbo Shen, Weiwei Lin, Wentai Wu, Haijie Wu, Keqin Li
- 식별자: `doi:10.21203/rs.3.rs-4568055/v1`

## 요약·초록

<title>Abstract</title> The End-Edge-Cloud (EEC) computing framework can offer low-latency, high-quality services to users of diverse demands by leveraging pervasive resources. However, the inherent disparities in task requirements and the strong heterogeneity of computational resources in these systems make it non-trivial for scheduler design, particularly in high load scenarios (e.g. burst of tasks). This also complicates the adaptation of traditional cloud-oriented schedulers considering their limited support of heterogeneous processors and accelerators (e.g., CPUs, GPUs and NPUs). In light of this, we first present a system framework for task scheduling in the EEC architecture. In the framework we adopt a reinforcement learning (RL)-based scheduler tailored for reducing task completion time and waiting time. Our method integrates task characteristics and environmental constraints within matrices, based on which an adapted Q-Learning agent is employed for decision making. We then introduce the implementation of our framework that features Kubernetes and Rancher-based coordination with extended support for heterogeneous processing units. Experimentally we built a real-world EEC testbed comprising PC, Atlas 200 DK, and Raspberry PI devices. Evaluation results of our algorithm demonstrate a 278\% enhancement in performance compared to existing algorithms in the context of burst-arrival task queues, which underscores the efficacy of our solution in realistic scenarios.

## 내 메모


