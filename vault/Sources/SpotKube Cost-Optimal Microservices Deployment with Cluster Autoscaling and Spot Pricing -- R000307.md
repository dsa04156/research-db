---
type: research-source
item_id: 307
title: "SpotKube: Cost-Optimal Microservices Deployment with Cluster Autoscaling and Spot Pricing"
source: "arxiv"
published: "2024-05-20T18:14:31Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/cloudcom62794.2024.00026"
url: "https://arxiv.org/abs/2405.12311v2"
generated_by: codex-research-db
aliases:
  - "SpotKube: Cost-Optimal Microservices Deployment with Cluster Autoscaling and Spot Pricing"
topics:
  - "kubernetes"
---

# SpotKube: Cost-Optimal Microservices Deployment with Cluster Autoscaling and Spot Pricing

[원문 열기](https://arxiv.org/abs/2405.12311v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2C2QTG4F`)
- 발행일: 2024-05-20T18:14:31Z
- 저자: Dasith Edirisinghe, Kavinda Rajapakse, Pasindu Abeysinghe, Sunimal Rathnayake
- 식별자: `doi:10.1109/cloudcom62794.2024.00026`

## 요약·초록

Microservices architecture, known for its agility and efficiency, is an ideal framework for cloud-based software development and deployment. When integrated with containerization and orchestration systems, resource management becomes more streamlined. However, cloud computing costs remain a critical concern, necessitating effective strategies to minimize expenses without compromising performance. Cloud platforms like AWS offer transient pricing options, such as Spot Pricing, to reduce operational costs. However, unpredictable demand and abrupt termination of spot VMs introduce challenges. By leveraging containerization and intelligent orchestration, microservices deployment costs can be optimized while maintaining performance requirements. We present SpotKube, an open-source, Kubernetes-based solution that employs a genetic algorithm for cost optimization. Designed to dynamically scale clusters for microservice applications on public clouds using spot pricing, SpotKube analyzes application characteristics to recommend optimal resource allocations. This ensures cost-effective deployments without sacrificing performance. Its elastic cluster autoscaler adapts to changing demands, gracefully managing node terminations to minimize disruptions in system availability.Evaluations conducted using real-world public cloud setups demonstrate SpotKube's superior performance and cost efficiency compared to alternative optimization strategies.

## 내 메모


