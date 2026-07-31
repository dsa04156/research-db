---
type: research-source
item_id: 299
title: "StatuScale: Status-aware and Elastic Scaling Strategy for Microservice Applications"
source: "arxiv"
published: "2024-07-14T12:00:20Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2407.10173"
url: "https://arxiv.org/abs/2407.10173v1"
generated_by: codex-research-db
aliases:
  - "StatuScale: Status-aware and Elastic Scaling Strategy for Microservice Applications"
topics:
  - "kubernetes"
---

# StatuScale: Status-aware and Elastic Scaling Strategy for Microservice Applications

[원문 열기](https://arxiv.org/abs/2407.10173v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`QIXCHI8F`)
- 발행일: 2024-07-14T12:00:20Z
- 저자: Linfeng Wen, Minxian Xu, Sukhpal Singh Gill, Muhammad Hafizhuddin Hilman, Satish Narayana Srirama, Kejiang Ye, Chengzhong Xu
- 식별자: `doi:10.48550/arxiv.2407.10173`

## 요약·초록

Microservice architecture has transformed traditional monolithic applications into lightweight components. Scaling these lightweight microservices is more efficient than scaling servers. However, scaling microservices still faces the challenges resulted from the unexpected spikes or bursts of requests, which are difficult to detect and can degrade performance instantaneously. To address this challenge and ensure the performance of microservice-based applications, we propose a status-aware and elastic scaling framework called StatuScale, which is based on load status detector that can select appropriate elastic scaling strategies for differentiated resource scheduling in vertical scaling. Additionally, StatuScale employs a horizontal scaling controller that utilizes comprehensive evaluation and resource reduction to manage the number of replicas for each microservice. We also present a novel metric named correlation factor to evaluate the resource usage efficiency. Finally, we use Kubernetes, an open-source container orchestration and management platform, and realistic traces from Alibaba to validate our approach. The experimental results have demonstrated that the proposed framework can reduce the average response time in the Sock-Shop application by 8.59% to 12.34%, and in the Hotel-Reservation application by 7.30% to 11.97%, decrease service level objective violations, and offer better performance in resource usage compared to baselines.

## 내 메모


