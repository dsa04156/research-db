---
type: research-source
item_id: 71
title: "Scalable Cloud-Native Architectures for Real-Time Payment Processing Systems"
source: "openalex"
published: "2026-07-11"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.58425/ajt.v5i8.577"
url: "https://doi.org/10.58425/ajt.v5i8.577"
generated_by: codex-research-db
aliases:
  - "Scalable Cloud-Native Architectures for Real-Time Payment Processing Systems"
topics:
  - "kubernetes"
---

# Scalable Cloud-Native Architectures for Real-Time Payment Processing Systems

[원문 열기](https://doi.org/10.58425/ajt.v5i8.577)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`WW9HSEJ4`)
- 발행일: 2026-07-11
- 저자: Midhun Michael Nelavala
- 식별자: `doi:10.58425/ajt.v5i8.577`

## 요약·초록

Aim: This study aimed to design and evaluate a cloud-native reference architecture for real-time payment processing that integrates microservices, event-driven communication, infrastructure-as-code, and federated AIOps to improve scalability, resilience, regulatory compliance, and operational efficiency. The novelty of the study is the federated three-tier integration model that combines ITIL-aligned governance, DevOps continuous delivery, and AIOps-driven anomaly detection within a single payment-specific reference architecture. Methods: A mixed-methods design was employed, combining a structured synthesis of peer-reviewed and industry literature with quantitative benchmarking of instrumented cloud-native reference deployments. The deployments were scaled from 1 to 128 service replicas across two public clouds and an on-premise environment and were evaluated against a representative monolithic baseline. Results: The findings show that the proposed cloud-native architecture reduced end-to-end p99 latency from approximately 850 ms in the monolithic baseline to approximately 180 ms, representing a 4.7× improvement. Sustained throughput scaled near-linearly to 78,000 transactions per second across 128 service replicas, compared with approximately 3,800 transactions per second in the baseline. Federated AIOps reduced Mean Time to Detect (MTTD) by 60% and Mean Time to Resolve (MTTR) by 50%, while alert volume and false-positive rates decreased by 70% and 82%, respectively. The architecture achieved 99.99% availability, with a Recovery Time Objective (RTO) of less than five minutes and a Recovery Point Objective (RPO) of less than 30 seconds across multi-region active-active deployments. The study also identifies operational complexity, multi-cloud cost overhead, and managed-service vendor lock-in as key limitations. Conclusion: The findings indicate that cloud-native architectures can substantially improve the scalability, operational resilience, and regulatory readiness of real-time payment systems compared with conventional monolithic designs. Recommendation: Financial institutions planning payment modernization should consider a phased adoption of cloud-native architectures supported by integrated governance, automation, and observability practices. The proposed framework should also be validated across diverse production payment environments.

## 내 메모


