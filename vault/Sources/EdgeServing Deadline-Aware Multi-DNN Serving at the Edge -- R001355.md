---
type: research-source
item_id: 1355
title: "EdgeServing: Deadline-Aware Multi-DNN Serving at the Edge"
source: "arxiv"
published: "2026-05-07T00:06:24Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.05527"
url: "https://arxiv.org/abs/2605.05527v1"
generated_by: codex-research-db
aliases:
  - "EdgeServing: Deadline-Aware Multi-DNN Serving at the Edge"
topics:
  - "edge-computing"
---

# EdgeServing: Deadline-Aware Multi-DNN Serving at the Edge

[원문 열기](https://arxiv.org/abs/2605.05527v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`G63PP8PA`)
- 발행일: 2026-05-07T00:06:24Z
- 저자: Jiahe Cao, Xiaomeng Li, Qiang Liu, Tao Han, Ning Zhang, Weisong Shi
- 식별자: `arxiv:2605.05527`

## 요약·초록

As edge computing expands, serving multiple deep neural network (DNN) models on a single shared GPU has become a common yet challenging scenario, where each scheduling decision affects the tail latency of all concurrent queues. Existing schedulers rely on local heuristics and fail to capture this global impact, while GPU spatial-sharing approaches sacrifice latency predictability. In this paper, we propose EdgeServing, a deadline-aware multi-DNN serving system for edge devices. EdgeServing adopts time-division GPU sharing with early-exit inference for high inference predictability, and introduces a stability score to quantify how each candidate scheduling decision impacts the future queue status. At runtime, it cohesively selects the model, exit point, and batch size to minimize predicted system-wide SLO impact. Experimental results on multiple hardware platforms show that EdgeServing consistently outperforms representative baselines in both SLO violation ratio and P95 latency, enabled by early-exit mechanism, which expands the scheduling action space under tight latency constraints.

## 내 메모


