---
type: research-source
item_id: 752
title: "Scalable Cloud-Native Architecture for Automated Anomaly Detection and Intelligent Response in Kubernetes and AKS Platforms"
source: "openalex"
published: "2025-06-17"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.62643/ijerst.2025.v21.n2.3146"
url: "https://doi.org/10.62643/ijerst.2025.v21.n2.3146"
generated_by: codex-research-db
aliases:
  - "Scalable Cloud-Native Architecture for Automated Anomaly Detection and Intelligent Response in Kubernetes and AKS Platforms"
topics:
  - "kubernetes"
---

# Scalable Cloud-Native Architecture for Automated Anomaly Detection and Intelligent Response in Kubernetes and AKS Platforms

[원문 열기](https://doi.org/10.62643/ijerst.2025.v21.n2.3146)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`QPJE88XH`)
- 발행일: 2025-06-17
- 저자: Hing-Yan Lee
- 식별자: `doi:10.62643/ijerst.2025.v21.n2.3146`

## 요약·초록

The rapid adoption of cloud-native architectures and platforms like Kubernetes and Azure Kubernetes Service (AKS) has introduced unprecedented scalability, but it has also brought immense complexity to system observability. Traditional, static threshold-based monitoring tools are increasingly inadequate for managing highly dynamic, ephemeral microservices, frequently resulting in alert fatigue and prolonged Mean Time to Resolution (MTTR) during critical outages. To address the limitations of reactive, human-in-the-loop engineering operations, this paper proposes a novel, highly scalable cloudnative architecture that seamlessly integrates deep learning-based anomaly detection directly with an automated Kubernetes response engine. Our approach employs a dual-model machine learning pipeline—combining Long Short-Term Memory (LSTM) networks for predictive time-series forecasting and Isolation Forests for real-time outlier detection—embedded within the AKS control plane via custom operators. Upon detecting an anomaly, the system autonomously triggers predefined, RBAC-compliant remediation policies, such as dynamic horizontal scaling or targeted pod restarts. Empirical evaluations within a simulated production environment demonstrate that the proposed architecture achieves a 0.92 F1-score in detection accuracy and slashes remediation times from several minutes to mere seconds. These findings prove that the marginal increase in computational monitoring overhead is decisively outweighed by profound improvements in system reliability and autonomous self-healing capabilities.

## 내 메모


