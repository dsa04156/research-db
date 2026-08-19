---
type: research-source
item_id: 2112
title: "OpScale: Operator-level Provisioning and Autoscaling for LLM Serving"
source: "openalex"
published: "2026-08-13"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.13499"
url: "https://arxiv.org/abs/2608.13499"
generated_by: codex-research-db
aliases:
  - "OpScale: Operator-level Provisioning and Autoscaling for LLM Serving"
topics:
  - "kubernetes"
---

# OpScale: Operator-level Provisioning and Autoscaling for LLM Serving

[원문 열기](https://arxiv.org/abs/2608.13499)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-08-13
- 저자: Xingqi Cui, Chieh-Jan Mike Liang, Ziang Tang, Jiarong Xing, Haoran Qiu
- 식별자: `arxiv:2608.13499`

## 요약·초록

Achieving cost efficiency while meeting strict user-facing SLOs (e.g., time-to-first-token) remains a fundamental challenge for cloud GPU clusters serving large language models (LLMs). Autoscaling is the key mechanism for cluster resource management, yet a basic system design question is open for serving LLMs: what should be the unit of scaling? Existing approaches primarily treat the entire model as a monolithic scaling unit--simple but unable to capture the fine-grained dynamics of inference workloads. As a result, such coarse-grained scaling often leads to either SLO violations under bursty demand or significant GPU under-utilization. Our characterization reveals substantial operator heterogeneity, exposing operator-level elasticity as a viable scaling primitive. We present OpScale, a practical operator-level orchestration framework of profiling, provisioning, placement, and runtime serving. OpScale is designed to tackle the high complexity and the space explosion problem, arising from operating at this finer granularity. Evaluated with production traces on up to 40 A100s and 24 GB200s, OpScale attains SLOs with up to 36.3% fewer GPUs and 28% less power, or achieves 44% higher throughput under fixed cost budgets.

## 내 메모


