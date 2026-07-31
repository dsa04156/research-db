---
type: research-source
item_id: 718
title: "Power- and Fragmentation-aware Online Scheduling for GPU Datacenters"
source: "arxiv"
published: "2024-12-23T11:27:17Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/ccgrid64434.2025.00015"
url: "https://arxiv.org/abs/2412.17484v1"
generated_by: codex-research-db
aliases:
  - "Power- and Fragmentation-aware Online Scheduling for GPU Datacenters"
topics:
  - "kubernetes"
---

# Power- and Fragmentation-aware Online Scheduling for GPU Datacenters

[원문 열기](https://arxiv.org/abs/2412.17484v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DKENZK27`)
- 발행일: 2024-12-23T11:27:17Z
- 저자: Francesco Lettich, Emanuele Carlini, Franco Maria Nardini, Raffaele Perego, Salvatore Trani
- 식별자: `doi:10.1109/ccgrid64434.2025.00015`

## 요약·초록

The rise of Artificial Intelligence and Large Language Models is driving increased GPU usage in data centers for complex training and inference tasks, impacting operational costs, energy demands, and the environmental footprint of large-scale computing infrastructures. This work addresses the online scheduling problem in GPU datacenters, which involves scheduling tasks without knowledge of their future arrivals. We focus on two objectives: minimizing GPU fragmentation and reducing power consumption. GPU fragmentation occurs when partial GPU allocations hinder the efficient use of remaining resources, especially as the datacenter nears full capacity. A recent scheduling policy, Fragmentation Gradient Descent (FGD), leverages a fragmentation metric to address this issue. Reducing power consumption is also crucial due to the significant power demands of GPUs. To this end, we propose PWR, a novel scheduling policy to minimize power usage by selecting power-efficient GPU and CPU combinations. This involves a simplified model for measuring power consumption integrated into a Kubernetes score plugin. Through an extensive experimental evaluation in a simulated cluster, we show how PWR, when combined with FGD, achieves a balanced trade-off between reducing power consumption and minimizing GPU fragmentation.

## 내 메모


