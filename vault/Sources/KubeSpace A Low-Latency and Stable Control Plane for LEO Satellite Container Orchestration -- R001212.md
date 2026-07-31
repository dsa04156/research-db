---
type: research-source
item_id: 1212
title: "KubeSpace: A Low-Latency and Stable Control Plane for LEO Satellite Container Orchestration"
source: "arxiv"
published: "2026-01-29T08:18:27Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2601.21383"
url: "https://arxiv.org/abs/2601.21383v1"
generated_by: codex-research-db
aliases:
  - "KubeSpace: A Low-Latency and Stable Control Plane for LEO Satellite Container Orchestration"
topics:
  - "kubernetes"
---

# KubeSpace: A Low-Latency and Stable Control Plane for LEO Satellite Container Orchestration

[원문 열기](https://arxiv.org/abs/2601.21383v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RUMZF4FK`)
- 발행일: 2026-01-29T08:18:27Z
- 저자: Zhiyuan Zhao, Jiasheng Wu, Shaojie Su, Wenjun Zhu, Yue Gao
- 식별자: `arxiv:2601.21383`

## 요약·초록

Low Earth orbit (LEO) satellites play a pivotal role in global connectivity-delivering high-speed Internet, cellular coverage, and massive IoT support. With ever-growing onboard computing and storage resources, LEO satellites herald a new cloud paradigm: space cloud computing. While container or chestration platforms (e.g., Kubernetes) excel in terrestrial data centers, they are ill-suited to LEO satellite networks, featuring geographic dispersion and frequent handovers. Those features bring high latency and intermittent management, leading to control plane failure in container orchestration. To address this, we propose KubeSpace, a low-latency and stable control plane specifically designed for container orchestration on LEO satellites. KubeSpace combines two key innovations: a distributed ground-control-node architecture that binds each satellite to its nearest controller for uninterrupted management, and an orbit-aware placement with dynamic assignment strategy that further minimizes communication latency and handover frequency. Extensive experiments based on real satellite traces demonstrate that compared to existing solutions, KubeSpace reduces the average management latency of satellite nodes by 59% without any management interruption time.

## 내 메모


