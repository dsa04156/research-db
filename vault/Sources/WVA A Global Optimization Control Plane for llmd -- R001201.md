---
type: research-source
item_id: 1201
title: "WVA: A Global Optimization Control Plane for llmd"
source: "arxiv"
published: "2026-03-10T14:33:23Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.09730"
url: "https://arxiv.org/abs/2603.09730v2"
generated_by: codex-research-db
aliases:
  - "WVA: A Global Optimization Control Plane for llmd"
topics:
  - "kubernetes"
---

# WVA: A Global Optimization Control Plane for llmd

[원문 열기](https://arxiv.org/abs/2603.09730v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`9BSMXDD8`)
- 발행일: 2026-03-10T14:33:23Z
- 저자: Abhishek Malvankar, Lionel Villard, Mohammed Abdi, Tommaso Sgreccia, Evgeny Shindin, Braulio Dumba, Vishakha Ramani, Asser Tantawi, Tamar Eilam
- 식별자: `arxiv:2603.09730`

## 요약·초록

As Large Language Models (LLMs) scale to handle massive concurrent traffic, optimizing the infrastructure required for inference has become a primary challenge. To manage the high cost of GPU resources while ensuring strict service-level objectives (SLOs), operators increasingly deploy models across heterogeneous hardware clusters that multiplex latency-sensitive online requests and throughput-oriented offline requests. However, traditional resource-centric autoscalers like the Kubernetes horizontal pod autoscaler (HPA) do not consider application-specific SLOs, hardware heterogeneity, or internal engine state (like KV cache utilization) globally. This leads to unnecessary scaling, severe resource underutilization, and disrupted stateful inference. To address these limitations, we introduce the Workload Variant Autoscaler (WVA), a specialized control plane co-designed with \texttt{llmd} that tightly couples scaling decisions with the inference server's internal saturation state. By utilizing proactive headroom-based scaling and fragmentation-aware scale-down, our experiments demonstrate that WVA achieves a \textbf{37\% improvement in effective throughput} and a \textbf{10x reduction in request failures} compared to HPA. Furthermore, WVA's cost-aware tiering intrinsically reduces overall power consumption by prioritizing lower-cost, energy-efficient hardware variants over homogeneous scaling on high-end accelerators.

## 내 메모


