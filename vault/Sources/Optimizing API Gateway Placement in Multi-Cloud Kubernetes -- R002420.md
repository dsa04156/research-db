---
type: research-source
item_id: 2420
title: "Optimizing API Gateway Placement in Multi-Cloud Kubernetes"
source: "kurate"
published: "2026-08-27T03:31:24Z"
first_seen: "2026-08-31"
review_status: "pending"
canonical_key: "arxiv:2608.26573"
url: "http://arxiv.org/abs/2608.26573v1"
generated_by: codex-research-db
aliases:
  - "Optimizing API Gateway Placement in Multi-Cloud Kubernetes"
topics:
  - "kubernetes"
---

# Optimizing API Gateway Placement in Multi-Cloud Kubernetes

[원문 열기](http://arxiv.org/abs/2608.26573v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-31|2026-08-31]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- Zotero: created (`4FXEBZ82`)
- 발행일: 2026-08-27T03:31:24Z
- 저자: Vinoth Punniyamoorthy, Murali Shankar Dulam, Aswathnarayan Muthukrishnan Kirubakaran, Akshay Deshpande, Nachiappan Chockalingam, Bikesh Kumar, Naga Surya Pasupuleti, Narender Reddy Bitla
- 식별자: `arxiv:2608.26573`

## 요약·초록

The use of API gateways within geographically distributed multi-cloud Kubernetes clusters poses a tradeoff between infrastructure cost, computational resources, and network latencies. We present an optimization formulation that addresses API gateway placement as a capacitated facility location problem that jointly determines which candidate clusters to activate, how many gateway replicas to deploy, and how regional traffic should be distributed across the selected clusters. The formulation imposes an upper bound on estimated client-to-cluster network round-trip latency, excluding gateway processing, queuing, and backendservice latency, and incorporates a utilization headroom factor for gateway replica capacity. We present both a mixed-integer linear programming (MILP) formulation and a constructive greedy heuristic that ranks candidates according to incremental cost, comprising cluster-activation and marginal replica costs, per unit of assignable capacity while explicitly accounting for already committed load. Both formulations are applied to deterministic, seed-controlled, geography-based synthetic instances. For each problem size, 30 instances are generated with random seeds to analyze their performance. The greedy algorithm achieves an optimality gap of 3.2% to 4.7% to the MILP optimal solution, with a maximum observed gap of 25.0% for one particular instance, and a speedup of approximately 660x to 3,490x for 3 to 12 candidate clusters. In a canonical 10-candidate, 10-demand region instance, MILP-optimal deployment saves 24.2% in terms of monthly cost compared to the full-replication baseline. On the other hand, selecting the single cheapest candidate yields savings of 24.8% compared to the MILP optimum but does not satisfy the latency requirement for 3 out of 10 demand regions.

## 내 메모


