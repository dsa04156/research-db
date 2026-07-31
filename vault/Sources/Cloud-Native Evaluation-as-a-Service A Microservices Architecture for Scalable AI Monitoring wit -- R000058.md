---
type: research-source
item_id: 58
title: "Cloud-Native Evaluation-as-a-Service: A Microservices Architecture for Scalable AI Monitoring with Conformal Guarantees"
source: "arxiv"
published: "2026-07-04T01:39:59Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.21623"
url: "https://arxiv.org/abs/2607.21623v1"
generated_by: codex-research-db
aliases:
  - "Cloud-Native Evaluation-as-a-Service: A Microservices Architecture for Scalable AI Monitoring with Conformal Guarantees"
topics:
  - "kubernetes"
---

# Cloud-Native Evaluation-as-a-Service: A Microservices Architecture for Scalable AI Monitoring with Conformal Guarantees

[원문 열기](https://arxiv.org/abs/2607.21623v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FQR8BF6P`)
- 발행일: 2026-07-04T01:39:59Z
- 저자: Lei Yang
- 식별자: `arxiv:2607.21623`

## 요약·초록

We present EaaS, a cloud-native reference architecture that operationalizes AI evaluation methods as six stateless Kubernetes microservices: conformal prediction with finite-sample-corrected Adaptive Prediction Sets, calibration assessment, drift detection via RFF-approximated Maximum Mean Discrepancy, fairness monitoring with bootstrap confidence intervals, a DAG-based pipeline orchestrator, and a result storage API. We validate four key methodological concerns. First, empirical coverage is consistent with the marginal conformal guarantee across K=50 random calibration/test splits, with mean coverage within 1.4 percentage points of the nominal target. Second, all four MMLU answer tokens appear in the top-20 logprobs with 0% imputation needed, and simulated imputation at 10% produces less than 1.5% coverage impact. Third, RFF-MMD achieves 100% detection power for mild and severe drift at the median heuristic bandwidth, with Type I error between 5-8.5%. Fourth, fairness monitoring on the UCI Adult Income dataset reveals significant demographic parity disparities by race (DP gap=0.33) with stable alerts across sequential batches. Conformal prediction and calibration services achieve sub-2ms p99 latency at batch size 100; RFF-MMD requires ~500ms suited for periodic batch monitoring. A comparison with four open-source tools suggests that, to the best of our knowledge, no current platform combines conformal-prediction-as-a-service, microservice decomposition, and DAG-based orchestration.

## 내 메모


