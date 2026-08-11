---
type: research-source
item_id: 1882
title: "A Kubernetes Scheduler Plugin for Cluster-Wide Placement Optimisation"
source: "arxiv"
published: "2026-08-07T09:05:43Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.06987"
url: "https://arxiv.org/abs/2608.06987v1"
generated_by: codex-research-db
aliases:
  - "A Kubernetes Scheduler Plugin for Cluster-Wide Placement Optimisation"
topics:
  - "kubernetes"
---

# A Kubernetes Scheduler Plugin for Cluster-Wide Placement Optimisation

[원문 열기](https://arxiv.org/abs/2608.06987v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-07T09:05:43Z
- 저자: Henrik Daniel Christensen, Saverio Giallorenzo, Jacopo Mauro
- 식별자: `arxiv:2608.06987`

## 요약·초록

The default scheduler of Kubernetes, the state-of-the-art container orchestrator, uses fast, local placement decisions. Unfortunately, this design leads to resource fragmentation, reduced cluster usage, and overprovisioning. External solvers can compute global placement plans, but enforcing these plans in upstream clusters is hard. Kubernetes provides no native cross-node preemption, uncoordinated concurrent scheduling leads to inconsistencies, and replacing the default scheduler would sever deployments from upstream cycles. We present OPSche, an open-source Kubernetes Scheduling Framework plugin where external solvers can drive cluster-wide placement decisions in concert with the default scheduler. OPSche atomically validates and enforces solver-produced plans through coordinated framework hooks and supports three trigger modes: scheduling-failure, periodic, and stable-queue -- resp. triggered when a workload cannot be placed, at fixed time intervals, when the set of pending workloads stabilises. Each mode has a blocking variant for a finer tuning of placement quality, latency, and disruption. We pair OPSche with a constraint-based optimisation solver, showing its feasibility across a broad set of cluster configurations and reporting improvements of resource usage by up to 3.0% and scheduling latency by more than a second.

## 내 메모


