---
type: research-source
item_id: 1168
title: "ADAPT: A Self-Calibrating Proactive Autoscaler for Container Orchestration"
source: "arxiv"
published: "2026-05-15T09:46:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.15788"
url: "https://arxiv.org/abs/2605.15788v1"
generated_by: codex-research-db
aliases:
  - "ADAPT: A Self-Calibrating Proactive Autoscaler for Container Orchestration"
topics:
  - "kubernetes"
---

# ADAPT: A Self-Calibrating Proactive Autoscaler for Container Orchestration

[원문 열기](https://arxiv.org/abs/2605.15788v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZH26ZMK9`)
- 발행일: 2026-05-15T09:46:43Z
- 저자: Himanshu Singh Baghel
- 식별자: `arxiv:2605.15788`

## 요약·초록

Proactive autoscaling for containerized workloads depends on knowing the provisioning delay, i.e., the time between a scaling decision and the moment new capacity is ready to serve traffic. In practice, this cold-start duration can vary substantially across environments and even across consecutive scale-out events. We present ADAPT (Adaptive Duration Approximation for Predictive Timing), an online EWMA estimator that tracks coldstart duration at runtime. ADAPT feeds a dynamic planning horizon, FH-OPT, into a Model Predictive Controller (MPC) that optimizes replica counts over a rolling window. Together, these components form a closed-loop proactive autoscaling design that adapts its lookahead based on measured provisioning delay. Evaluated across three policies (MPC+LSTM, MPC+Prophet, HPA) and six workload archetypes with five random seeds, MPC+LSTM achieves below 5% SLA violation on all workloads, compared with 7-19% for reactive HPA and up to 28.7% for MPC+Prophet on bimodal traffic.

## 내 메모


