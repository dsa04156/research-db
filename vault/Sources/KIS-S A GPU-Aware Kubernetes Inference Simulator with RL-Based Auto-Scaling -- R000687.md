---
type: research-source
item_id: 687
title: "KIS-S: A GPU-Aware Kubernetes Inference Simulator with RL-Based Auto-Scaling"
source: "arxiv"
published: "2025-07-10T17:10:51Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.07932"
url: "https://arxiv.org/abs/2507.07932v1"
generated_by: codex-research-db
aliases:
  - "KIS-S: A GPU-Aware Kubernetes Inference Simulator with RL-Based Auto-Scaling"
topics:
  - "kubernetes"
---

# KIS-S: A GPU-Aware Kubernetes Inference Simulator with RL-Based Auto-Scaling

[원문 열기](https://arxiv.org/abs/2507.07932v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZAXM4W4Q`)
- 발행일: 2025-07-10T17:10:51Z
- 저자: Guilin Zhang, Wulan Guo, Ziqi Tan, Qiang Guan, Hailong Jiang
- 식별자: `arxiv:2507.07932`

## 요약·초록

Autoscaling GPU inference workloads in Kubernetes remains challenging due to the reactive and threshold-based nature of default mechanisms such as the Horizontal Pod Autoscaler (HPA), which struggle under dynamic and bursty traffic patterns and lack integration with GPU-level metrics. We present KIS-S, a unified framework that combines KISim, a GPU-aware Kubernetes Inference Simulator, with KIScaler, a Proximal Policy Optimization (PPO)-based autoscaler. KIScaler learns latency-aware and resource-efficient scaling policies entirely in simulation, and is directly deployed without retraining. Experiments across four traffic patterns show that KIScaler improves average reward by 75.2%, reduces P95 latency up to 6.7x over CPU baselines, and generalizes without retraining. Our work bridges the gap between reactive autoscaling and intelligent orchestration for scalable GPU-accelerated environments.

## 내 메모


