---
type: research-source
item_id: 691
title: "Sharpening Kubernetes Audit Logs with Context Awareness"
source: "arxiv"
published: "2025-06-19T14:02:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1016/j.comnet.2025.111890"
url: "https://arxiv.org/abs/2506.16328v3"
generated_by: codex-research-db
aliases:
  - "Sharpening Kubernetes Audit Logs with Context Awareness"
topics:
  - "kubernetes"
---

# Sharpening Kubernetes Audit Logs with Context Awareness

[원문 열기](https://arxiv.org/abs/2506.16328v3)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`9X2X7I7F`)
- 발행일: 2025-06-19T14:02:22Z
- 저자: Matteo Franzil, Valentino Armani, Luis Augusto Dias Knob, Domenico Siracusa
- 식별자: `doi:10.1016/j.comnet.2025.111890`

## 요약·초록

Kubernetes has emerged as the de facto orchestrator of microservices, providing scalability and extensibility to a highly dynamic environment. It builds an intricate and deeply connected system that requires extensive monitoring capabilities to be properly managed. To this account, K8s natively offers audit logs, a powerful feature for tracking API interactions in the cluster. Audit logs provide a detailed and chronological record of all activities in the system. Unfortunately, K8s auditing suffers from several practical limitations: it generates large volumes of data continuously, as all components within the cluster interact and respond to user actions. Moreover, each action can trigger a cascade of secondary events dispersed across the log, with little to no explicit linkage, making it difficult to reconstruct the context behind user-initiated operations. In this paper, we introduce K8NTEXT, a novel approach for streamlining K8s audit logs by reconstructing contexts, i.e., grouping actions performed by actors on the cluster with the subsequent events these actions cause. Correlated API calls are automatically identified, labeled, and consistently grouped using a combination of inference rules and a Machine Learning model, largely simplifying data consumption. We evaluate K8NTEXT's performance, scalability, and expressiveness both in systematic tests and with a series of use cases. We show that it consistently provides accurate context reconstruction, even for complex operations involving 50, 100 or more correlated actions, achieving over 95 percent accuracy across the entire spectrum, from simple to highly composite actions.

## 내 메모


