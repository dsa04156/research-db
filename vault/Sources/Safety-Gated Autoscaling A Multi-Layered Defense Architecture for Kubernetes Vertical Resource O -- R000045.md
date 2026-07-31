---
type: research-source
item_id: 45
title: "Safety-Gated Autoscaling: A Multi-Layered Defense Architecture for Kubernetes Vertical Resource Optimization"
source: "arxiv"
published: "2026-07-29T06:06:15Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26503"
url: "https://arxiv.org/abs/2607.26503v1"
generated_by: codex-research-db
aliases:
  - "Safety-Gated Autoscaling: A Multi-Layered Defense Architecture for Kubernetes Vertical Resource Optimization"
topics:
  - "kubernetes"
---

# Safety-Gated Autoscaling: A Multi-Layered Defense Architecture for Kubernetes Vertical Resource Optimization

[원문 열기](https://arxiv.org/abs/2607.26503v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KEPDCSGA`)
- 발행일: 2026-07-29T06:06:15Z
- 저자: Azra Karakaya, Erva Şengül, Ahmet Kaplan
- 식별자: `arxiv:2607.26503`

## 요약·초록

Kubernetes is the standard platform for orchestrating containerized applications, yet resource management remains difficult. To stay safe, engineers over-provision CPU and memory, leaving reserved but unused capacity that is the main source of wasted cost. The built-in Horizontal and Vertical Pod Autoscalers are reactive: they act only after a threshold is crossed, which causes lag, over-provisioning, and can mask software defects by granting a leaking workload more memory. Predictive autoscalers focus on improving forecasting accuracy or run inside proprietary infrastructure, and anomaly detection is used only to alert, never to block a harmful action. The Intelligent Cluster Optimizer is an open-source Kubernetes operator that right-sizes container workloads with safety as a first-class concern. Its central contribution is a five-layer safety pipeline where a memory-leak detector, based on linear regression with R^2 scoring, acts as a blocking gate: if a leak is detected the recommendation is rejected, so the optimizer never hides a bug by enlarging a broken container. The pipeline combines SLA monitoring, a circuit breaker, HPA/PDB conflict detection, and a policy engine, with rollback and dry-run mode for human approval. Recommendations are produced by percentile analysis and Holt-Winters forecasting, balanced through multi-objective Pareto optimization at the per-container level. We validated the system with 1118 automated tests at 80.3% coverage and a live deployment on Google Kubernetes Engine, where right-sizing produced estimated cost savings of 20--40% in what-if projections and the leak gate reached 83% detection accuracy.

## 내 메모


