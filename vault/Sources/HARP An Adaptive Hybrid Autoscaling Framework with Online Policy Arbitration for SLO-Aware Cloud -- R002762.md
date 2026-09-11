---
type: research-source
item_id: 2762
title: "HARP: An Adaptive Hybrid Autoscaling Framework with Online Policy Arbitration for SLO-Aware Cloud-Native ML Inference"
source: "openalex"
published: "2026-09-07"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "doi:10.54097/8vyfba92"
url: "https://doi.org/10.54097/8vyfba92"
generated_by: codex-research-db
aliases:
  - "HARP: An Adaptive Hybrid Autoscaling Framework with Online Policy Arbitration for SLO-Aware Cloud-Native ML Inference"
topics:
  - "kubernetes"
---

# HARP: An Adaptive Hybrid Autoscaling Framework with Online Policy Arbitration for SLO-Aware Cloud-Native ML Inference

[원문 열기](https://doi.org/10.54097/8vyfba92)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`BWCDJAJH`)
- 발행일: 2026-09-07
- 저자: Yuchen Luo, Zihan Peng, Rui Zhang
- 식별자: `doi:10.54097/8vyfba92`

## 요약·초록

Cloud-native machine learning inference services must hold tail-latency service level objectives (SLOs) while paying for as few replicas as possible. Two families of autoscalers compete for this job: reactive threshold controllers such as the Kubernetes horizontal pod autoscaler, and predictive controllers that provision ahead of demand. Neither family dominates. Which one wins is decided by operating conditions—replica activation delay, the price an operator places on a replica relative to an SLO violation, and the statistical regime of the arriving workload—that are unknown at design time and change during a deployment. We present HARP, an adaptive hybrid framework that treats the choice of control philosophy as an online decision rather than a design-time commitment. HARP maintains a pool of six heterogeneous demand hypotheses, scores every hypothesis at every epoch with a counterfactual shadow loss computed from telemetry a production deployment already collects, and arbitrates among them with a fixed-share Hedge rule that provably tracks the best hypothesis under regime change. Two further mechanisms make the arbitration actionable: an adaptive conformal margin whose coverage target is driven by an SLO error budget, and a risk-averse aggregation that maps the arbiter's belief to a replica count. On three real production traces (AWS ELB request counts, NYC taxi demand and tweet volume) driven by a measured CPU inference profile, HARP cuts SLO violations by 26.8–92.4% against reactive and forecasting baselines. Across 27 operating conditions its worst-case cost regret against the best fixed policy of each condition is 4.4%, versus 42.5% for a strong confidence-aware predictive controller and over 300% for threshold controllers.

## 내 메모


