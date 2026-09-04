---
type: research-source
item_id: 2586
title: "Iapetus: Content-Aware Hierarchical Scheduling for Collaborative ViT Inference in LEO Satellite Networks"
source: "arxiv"
published: "2026-09-03T03:13:09Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.03318"
url: "https://arxiv.org/abs/2609.03318v1"
generated_by: codex-research-db
aliases:
  - "Iapetus: Content-Aware Hierarchical Scheduling for Collaborative ViT Inference in LEO Satellite Networks"
topics:
  - "edge-computing"
---

# Iapetus: Content-Aware Hierarchical Scheduling for Collaborative ViT Inference in LEO Satellite Networks

[원문 열기](https://arxiv.org/abs/2609.03318v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T03:13:09Z
- 저자: Yan Chen, Yunxiang Zhang, Guanjun Jiang, Haiquan Wang
- 식별자: `arxiv:2609.03318`

## 요약·초록

Collaborative inference pools distributed resources to run compute-intensive Vision Transformers (ViTs) in satellite edge computing. Model partitioning enables such collaboration by assigning consecutive layer groups to different nodes, but the large volume of intermediate activation data incurs substantial transfer overhead that can erase its benefit. Token compression reduces downstream computation and activation transfer, but its quality impact depends on input content, model depth, and earlier pruning decisions, while layer offloading must adapt to time-varying contact and battery conditions. We present \sys, a content-aware hierarchical scheduler that screens constellation-wide options to retain a bounded candidate set, then refines each candidate into a complete token compression and layer offloading trajectory using quality prediction and joint planning. A unified objective balances per-task latency, energy, and quality loss against accumulated workload and battery pressures. We implement \sys on an NVIDIA Jetson AGX Orin hardware-in-the-loop testbed and use its validated execution model for constellation-scale trace replay across multiple ViT workloads and constellation settings. At \(5\)~tasks/s, \sys accomplishes 91.6\% of released tasks, 26.1 percentage points above MARATD3, the strongest baseline, while reducing mean latency and battery draw by 53.0\% and 70.8\%, respectively, and meeting quality targets.

## 내 메모


