---
type: research-source
item_id: 2911
title: "X-TRAIL-RAN: an explainable and scalable O-RAN framework for QoS-aware radio resource control in 5G/6G networks"
source: "openalex"
published: "2026-09-15"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-71044-w"
url: "https://doi.org/10.1038/s41598-026-71044-w"
generated_by: codex-research-db
aliases:
  - "X-TRAIL-RAN: an explainable and scalable O-RAN framework for QoS-aware radio resource control in 5G/6G networks"
topics:
  - "kubernetes"
---

# X-TRAIL-RAN: an explainable and scalable O-RAN framework for QoS-aware radio resource control in 5G/6G networks

[원문 열기](https://doi.org/10.1038/s41598-026-71044-w)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`S7ATD2KF`)
- 발행일: 2026-09-15
- 저자: Walaa Alayed, Hassam Tahir, Waqar Ul Hassan
- 식별자: `doi:10.1038/s41598-026-71044-w`

## 요약·초록

Open Radio Access Network (O-RAN) is becoming a key enabling architecture for programmable, intelligent, and service-aware radio access control in future 5G/6G networks. However, practical O-RAN decision frameworks still face three major limitations: limited scalability under increasing user equipment and telemetry loads, high orchestration overhead, and weak operator visibility into why a radio resource control action is selected. This paper proposes X-TRAIL-RAN, an explainable and scalable O-RAN framework for QoS-aware radio resource control. The proposed framework models RAN control as a multi-objective decision problem that jointly considers radio quality, cell-load state, throughput behavior, delay sensitivity, packet stability, service priority, mobility risk, and operator policy constraints. Unlike conventional black-box xApp decision pipelines, X-TRAIL-RAN generates structured explanation records for each control event, including selected action, selected serving configuration, ranked decision factors, local attribution weights, confidence score, and operator-readable rationale. The framework is implemented through a Kubernetes-native service decomposition that separates telemetry ingestion, near-real-time control, QoS-aware decision logic, XAI generation, scenario execution, and monitoring. Evaluation across representative eMBB, URLLC, mMTC, mixed-service, and policy-constrained RAN scenarios demonstrates that the proposed framework supports service-dependent control behavior while maintaining interpretable and computationally feasible decision outputs. The results show normalized control utilities between 0.79 and 0.88, QoS satisfaction between 0.86 and 0.93, and decision-plus-XAI latency between 28.4 and 44.7 ms across the evaluated scenarios. A separate scalability study from 25 to 400 concurrent UEs shows median control-loop latency increasing from 27.6 to 54.9 ms, with 95th-percentile latency remaining at 66.2 ms for the largest evaluated workload. By integrating QoS optimization, explainable decision intelligence, and scalable orchestration, X-TRAIL-RAN provides an applied engineering foundation for trustworthy autonomous RAN control in future O-RAN-enabled 5G/6G systems.

## 내 메모


