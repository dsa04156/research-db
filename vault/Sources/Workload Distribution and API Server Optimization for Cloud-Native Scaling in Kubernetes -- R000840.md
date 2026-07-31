---
type: research-source
item_id: 840
title: "Workload Distribution and API Server Optimization for Cloud-Native Scaling in Kubernetes"
source: "openalex"
published: "2025-07-08"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.22399/ijcesen.2820"
url: "https://doi.org/10.22399/ijcesen.2820"
generated_by: codex-research-db
aliases:
  - "Workload Distribution and API Server Optimization for Cloud-Native Scaling in Kubernetes"
topics:
  - "kubernetes"
---

# Workload Distribution and API Server Optimization for Cloud-Native Scaling in Kubernetes

[원문 열기](https://doi.org/10.22399/ijcesen.2820)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`9X5HZMDS`)
- 발행일: 2025-07-08
- 저자: Amit Karbhari Mogal, Vaibhav P. Sonaje
- 식별자: `doi:10.22399/ijcesen.2820`

## 요약·초록

The rapid adoption of container orchestration platforms, particularly Kubernetes, has revolutionized the deployment and scalability of cloud-native applications. However, as cluster size and workload complexity increase, Kubernetes often faces performance degradation due to inefficient workload distribution and API server bottlenecks. This paper investigates the architectural and operational limitations that emerge in large-scale Kubernetes deployments, with a focus on API server saturation and imbalance in workload scheduling. Drawing from real-world deployment data and synthetic stress-testing, we analyze the scalability thresholds imposed by the Kubernetes control plane, identifying key inefficiencies in the default scheduler and load distribution strategies.To address these challenges, we propose a novel optimization framework that integrates dynamic workload partitioning, intelligent pod-to-node assignment, and API call reduction techniques. Our method leverages asynchronous state propagation and fine-grained node-labeling to enhance scheduler decisions while introducing minimal latency. Experimental evaluation across clusters of varying sizes demonstrates up to 47% improvement in resource utilization, a 35% reduction in API server load, and faster convergence during scale-out events. These results position the proposed solution as a viable enhancement for production-grade Kubernetes environments operating at scale.

## 내 메모


