---
type: research-source
item_id: 348
title: "Carbon-Aware Kubernetes Scheduling Using Deep Reinforcement Learning for Mixed Batch and Latency-Sensitive Workloads"
source: "openalex"
published: "2024-06-10"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.15680/ijctece.2024.0703009"
url: "https://doi.org/10.15680/ijctece.2024.0703009"
generated_by: codex-research-db
aliases:
  - "Carbon-Aware Kubernetes Scheduling Using Deep Reinforcement Learning for Mixed Batch and Latency-Sensitive Workloads"
topics:
  - "kubernetes"
---

# Carbon-Aware Kubernetes Scheduling Using Deep Reinforcement Learning for Mixed Batch and Latency-Sensitive Workloads

[원문 열기](https://doi.org/10.15680/ijctece.2024.0703009)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`87FBJRF9`)
- 발행일: 2024-06-10
- 저자: Sreedar Radhakrishnan
- 식별자: `doi:10.15680/ijctece.2024.0703009`

## 요약·초록

Carbon emissions from cloud data centers vary significantly with workload placement owing to regional and temporal differences in carbon electricity intensity. Mainstream Kubernetes schedulers remain entirely agnostic to these differences, systematically missing opportunities for emission reduction. This paper presents a carbon-aware Kubernetes scheduling framework driven by Proximal Policy Optimization (PPO), a deep reinforcement learning algorithm chosen for its stable policy gradient updates under non-stationary carbon signals. The scheduling problem is formulated as a Markov Decision Process in which the agent jointly optimizes carbon efficiency, SLA compliance, and resource utilization. Workloads are classified into latency-sensitive services and delay-tolerant batch jobs, with asymmetric reward weighting that strongly penalizes SLA violations for the former while prioritizing carbon placement for the latter. Large-scale simulation and Azure Kubernetes Service testbed experiments show that the proposed scheduler reduces mean carbon emissions per workload by 28% compared with the default scheduler and by 15% compared with a rule-based carbon-and-SLA-aware heuristic, while holding SLA violation rates below 1.2%. Critically, the PPO scheduler also reduces carbon emission variance by 49% under stochastic conditions, providing more predictable environmental performance than any baseline—a property with direct operational value for sustainability commitments.

## 내 메모


