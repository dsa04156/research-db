---
type: research-source
item_id: 1207
title: "Token Management in Multi-Tenant AI Inference Platforms"
source: "arxiv"
published: "2026-02-27T22:44:09Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.00356"
url: "https://arxiv.org/abs/2603.00356v1"
generated_by: codex-research-db
aliases:
  - "Token Management in Multi-Tenant AI Inference Platforms"
topics:
  - "kubernetes"
---

# Token Management in Multi-Tenant AI Inference Platforms

[원문 열기](https://arxiv.org/abs/2603.00356v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2H7AZP2F`)
- 발행일: 2026-02-27T22:44:09Z
- 저자: William J. Cunningham
- 식별자: `arxiv:2603.00356`

## 요약·초록

Multi-tenant AI inference platforms must balance resource utilization against service-level guarantees under variable demand. Conventional approaches fail to achieve this balance: dedicated endpoints strand capacity on idle models, while rate limits ignore the heterogeneous cost of inference requests. We introduce \emph{token pools}, a control-plane abstraction that represents inference capacity as explicit entitlements expressed in inference-native units (token throughput, KV cache, concurrency). Unlike rate limits, which govern request admission without regard to execution cost, token pools authorize both admission and autoscaling from the same capacity model, ensuring consistency between what is promised and what is provisioned. The abstraction captures burst modes across multiple dimensions invisible to conventional throttling. Dynamic per-entitlement limits on each burst dimension enable fine-grained control over resource consumption while permitting work-conserving backfill by low-priority traffic. The design supports priority-aware allocation, service tiers with differentiated guarantees, and debt-based fairness mechanisms, all without modifying the underlying inference runtime or cluster scheduler. In experiments on a Kubernetes cluster with vLLM backends, token pools maintain a bounded P99 latency for guaranteed workloads during overload by selectively throttling spot traffic, while a baseline without admission control experiences unbounded latency degradation across all workloads. A second experiment demonstrates debt-based fair-share convergence among elastic workloads with heterogeneous SLO requirements during capacity scarcity.

## 내 메모


