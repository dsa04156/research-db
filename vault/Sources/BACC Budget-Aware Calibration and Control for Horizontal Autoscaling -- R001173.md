---
type: research-source
item_id: 1173
title: "BACC: Budget-Aware Calibration and Control for Horizontal Autoscaling"
source: "arxiv"
published: "2026-05-01T16:34:35Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.20575"
url: "https://arxiv.org/abs/2606.20575v1"
generated_by: codex-research-db
aliases:
  - "BACC: Budget-Aware Calibration and Control for Horizontal Autoscaling"
topics:
  - "kubernetes"
---

# BACC: Budget-Aware Calibration and Control for Horizontal Autoscaling

[원문 열기](https://arxiv.org/abs/2606.20575v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DGPNG32B`)
- 발행일: 2026-05-01T16:34:35Z
- 저자: Fan Liu, Guanqi Li, Behrooz Farkiani, Patrick Crowley
- 식별자: `arxiv:2606.20575`

## 요약·초록

Cloud services must continuously adapt replica counts to fluctuating demand while respecting fixed-period reliability budgets. Many horizontal autoscalers either react to instantaneous utilization or provision against a fixed predictive risk target. These policies do not explicitly account for how much of the period-level violation budget has already been consumed, so they can be overly conservative when the budget is healthy and insufficiently conservative when the budget is being depleted. We present BACC, a model-agnostic framework for budget-aware horizontal autoscaling. BACC separates three concerns that are often entangled in prior systems: workload prediction, online uncertainty calibration, and budget-paced capacity control. It wraps an arbitrary forecaster with Adaptive Conformal Inference (ACI) to calibrate workload uncertainty online, then uses a proportional--integral controller to adjust provisioning aggressiveness based on the observed pace of budget consumption. We instantiate BACC for CPU-threshold-based horizontal autoscaling in Kubernetes and evaluate it through trace-driven simulation and cluster replay experiments. Across five Azure Functions traces, three compliance levels, and two forecasting backends, BACC tracks the requested violation target closely, achieving mean absolute compliance gaps of 0.44 and 0.42 percentage points with ARIMA and Chronos, respectively. The Kubernetes experiments further show that the same controller improves CPU-threshold compliance over native HPA under deployment effects such as measurement delay and replica readiness.

## 내 메모


