---
type: research-source
item_id: 1151
title: "Greenness-Driven Scheduling in Far Edge Kubernetes: A CODECO Evaluation"
source: "arxiv"
published: "2026-06-10T14:31:50Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.12136"
url: "https://arxiv.org/abs/2606.12136v1"
generated_by: codex-research-db
aliases:
  - "Greenness-Driven Scheduling in Far Edge Kubernetes: A CODECO Evaluation"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Greenness-Driven Scheduling in Far Edge Kubernetes: A CODECO Evaluation

[원문 열기](https://arxiv.org/abs/2606.12136v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RTAX4DXH`)
- 발행일: 2026-06-10T14:31:50Z
- 저자: Kaikang Huang, Dalal Ali, Rute C. Sofia
- 식별자: `arxiv:2606.12136`

## 요약·초록

Energy consumption is an increasing concern in IoT-Edge-Cloud infrastructures, where containerized application orchestration must balance performance with sustainability. This paper investigates how the Kubernetes CODECO framework integrates cross-layer energy-awareness into scheduling decisions for containerized applications across the IoT-Edge-Cloud continuum. CODECO monitors energy at both the computational level, via Kepler, and at a network (IP) level, and uses these metrics to define greenness heuristics that guide pod placement decisions through its ILP-based scheduler. The approach is experimentally evaluated on a real-world far Edge testbed composed of ARM-based embedded devices, comparing CODECO against vanilla Kubernetes across multiple scenarios. The results show that CODECO consistently reduces the energy consumption of the cluster, with savings of up to 11.01 mJ in computational energy and 4.14 mJ in network transmission energy consumption at peak load, for a wide set of scenarios which combine different types of injected fault conditions, including CPU stress, asymmetric network delay, and bandwidth contention. A composite greenness score combining both energy dimensions provides a stable and consistent ranking of scheduling strategies across all conditions, demonstrating its suitability as a unified energy indicator for cluster-level orchestration decisions across the IoT-Edge-Cloud continuum.

## 내 메모


