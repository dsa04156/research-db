---
type: research-source
item_id: 729
title: "A House United Within Itself: SLO-Awareness for On-Premises Containerized ML Inference Clusters via Faro"
source: "arxiv"
published: "2024-09-29T00:02:39Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3689031.3696071"
url: "https://arxiv.org/abs/2409.19488v1"
generated_by: codex-research-db
aliases:
  - "A House United Within Itself: SLO-Awareness for On-Premises Containerized ML Inference Clusters via Faro"
topics:
  - "kubernetes"
---

# A House United Within Itself: SLO-Awareness for On-Premises Containerized ML Inference Clusters via Faro

[원문 열기](https://arxiv.org/abs/2409.19488v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DT4DE8XG`)
- 발행일: 2024-09-29T00:02:39Z
- 저자: Beomyeol Jeon, Chen Wang, Diana Arroyo, Alaa Youssef, Indranil Gupta
- 식별자: `doi:10.1145/3689031.3696071`

## 요약·초록

This paper tackles the challenge of running multiple ML inference jobs (models) under time-varying workloads, on a constrained on-premises production cluster. Our system Faro takes in latency Service Level Objectives (SLOs) for each job, auto-distills them into utility functions, "sloppifies" these utility functions to make them amenable to mathematical optimization, automatically predicts workload via probabilistic prediction, and dynamically makes implicit cross-job resource allocations, in order to satisfy cluster-wide objectives, e.g., total utility, fairness, and other hybrid variants. A major challenge Faro tackles is that using precise utilities and high-fidelity predictors, can be too slow (and in a sense too precise!) for the fast adaptation we require. Faro's solution is to "sloppify" (relax) its multiple design components to achieve fast adaptation without overly degrading solution quality. Faro is implemented in a stack consisting of Ray Serve running atop a Kubernetes cluster. Trace-driven cluster deployments show that Faro achieves 2.3$\times$-23$\times$ lower SLO violations compared to state-of-the-art systems.

## 내 메모


