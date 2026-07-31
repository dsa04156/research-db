---
type: research-source
item_id: 1219
title: "Secure and Governed API Gateway Architectures for Multi-Cluster Cloud Environments"
source: "arxiv"
published: "2025-12-29T12:01:33Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.23774"
url: "https://arxiv.org/abs/2512.23774v1"
generated_by: codex-research-db
aliases:
  - "Secure and Governed API Gateway Architectures for Multi-Cluster Cloud Environments"
topics:
  - "kubernetes"
---

# Secure and Governed API Gateway Architectures for Multi-Cluster Cloud Environments

[원문 열기](https://arxiv.org/abs/2512.23774v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`WRM5FXH3`)
- 발행일: 2025-12-29T12:01:33Z
- 저자: Vinoth Punniyamoorthy, Kabilan Kannan, Akshay Deshpande, Lokesh Butra, Akash Kumar Agarwal, Adithya Parthasarathy, Suhas Malempati, Bikesh Kumar
- 식별자: `arxiv:2512.23774`

## 요약·초록

API gateways serve as critical enforcement points for security, governance, and traffic management in cloud-native systems. As organizations increasingly adopt multi-cluster and hybrid cloud deployments, maintaining consistent policy enforcement, predictable performance, and operational stability across heterogeneous gateway environments becomes challenging. Existing approaches typically manage security, governance, and performance as loosely coupled concerns, leading to configuration drift, delayed policy propagation, and unstable runtime behavior under dynamic workloads. This paper presents a governance-aware, intent-driven architecture for coordinated API gateway management in multi-cluster cloud environments. The proposed approach expresses security, governance, and performance objectives as high-level declarative intents, which are systematically translated into enforceable gateway configurations and continuously validated through policy verification and telemetry-driven feedback. By decoupling intent specification from enforcement while enabling bounded, policy-compliant adaptation, the architecture supports heterogeneous gateway implementations without compromising governance guarantees or service-level objectives. A prototype implementation across multiple Kubernetes clusters demonstrates the effectiveness of the proposed design. Experimental results show up to a 42% reduction in policy drift, a 31% improvement in configuration propagation time, and sustained p95 latency overhead below 6% under variable workloads, compared to manual and declarative baseline approaches. These results indicate that governance-aware, intent-driven gateway orchestration provides a scalable and reliable foundation for secure, consistent, and performance-predictable cloud-native platforms.

## 내 메모


