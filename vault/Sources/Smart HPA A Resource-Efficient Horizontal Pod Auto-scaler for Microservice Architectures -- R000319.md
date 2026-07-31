---
type: research-source
item_id: 319
title: "Smart HPA: A Resource-Efficient Horizontal Pod Auto-scaler for Microservice Architectures"
source: "arxiv"
published: "2024-02-27T01:22:46Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/icsa59870.2024.00013"
url: "https://arxiv.org/abs/2403.07909v1"
generated_by: codex-research-db
aliases:
  - "Smart HPA: A Resource-Efficient Horizontal Pod Auto-scaler for Microservice Architectures"
topics:
  - "kubernetes"
---

# Smart HPA: A Resource-Efficient Horizontal Pod Auto-scaler for Microservice Architectures

[원문 열기](https://arxiv.org/abs/2403.07909v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SDRT65TK`)
- 발행일: 2024-02-27T01:22:46Z
- 저자: Hussain Ahmad, Christoph Treude, Markus Wagner, Claudia Szabo
- 식별자: `doi:10.1109/icsa59870.2024.00013`

## 요약·초록

Microservice architectures have gained prominence in both academia and industry, offering enhanced agility, reusability, and scalability. To simplify scaling operations in microservice architectures, container orchestration platforms such as Kubernetes feature Horizontal Pod Auto-scalers (HPAs) designed to adjust the resources of microservices to accommodate fluctuating workloads. However, existing HPAs are not suitable for resource-constrained environments, as they make scaling decisions based on the individual resource capacities of microservices, leading to service unavailability and performance degradation. Furthermore, HPA architectures exhibit several issues, including inefficient data processing and a lack of coordinated scaling operations. To address these concerns, we propose Smart HPA, a flexible resource-efficient horizontal pod auto-scaler. It features a hierarchical architecture that integrates both centralized and decentralized architectural styles to leverage their respective strengths while addressing their limitations. We introduce resource-efficient heuristics that empower Smart HPA to exchange resources among microservices, facilitating effective auto-scaling of microservices in resource-constrained environments. Our experimental results show that Smart HPA outperforms the Kubernetes baseline HPA by reducing resource overutilization, overprovisioning, and underprovisioning while increasing resource allocation to microservice applications.

## 내 메모


