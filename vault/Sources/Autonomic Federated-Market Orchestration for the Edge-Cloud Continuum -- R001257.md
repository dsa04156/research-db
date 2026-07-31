---
type: research-source
item_id: 1257
title: "Autonomic Federated-Market Orchestration for the Edge-Cloud Continuum"
source: "openalex"
published: "2026-05-26"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.27106"
url: "https://arxiv.org/abs/2605.27106"
generated_by: codex-research-db
aliases:
  - "Autonomic Federated-Market Orchestration for the Edge-Cloud Continuum"
topics:
  - "kubernetes"
---

# Autonomic Federated-Market Orchestration for the Edge-Cloud Continuum

[원문 열기](https://arxiv.org/abs/2605.27106)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`7K3WRR6H`)
- 발행일: 2026-05-26
- 저자: Lauri Lovén, Roberto Morabito, Abhishek Kumar, Susanna Pirttikangas, Jukka Riekki, Sasu Tarkoma
- 식별자: `arxiv:2605.27106`

## 요약·초록

The edge-cloud computing continuum demands self-management mechanisms that scale across autonomous administrative domains while honouring tenant- and operator-specified data sovereignty. We present Neural Pub/Sub, a federated-broker autonomic substrate whose self-organising behaviour emerges from market-based price signals rather than centralised control. Its MAPE-K control loop closes over per-broker health and load monitoring, marginal-cost clearing-price analysis, placement planning over a polymatroidal feasibility region, federated cross-domain dispatch, and shared peer subscription summaries with bounded-staleness price signals. The Plan step is anchored in a Walrasian convergence proposition: under gross-substitutes valuations on tree and series-parallel service-dependency DAGs, decentralised price-based allocation matches the welfare of a centralised oracle. We evaluate the substrate on a 4-VM, 4-domain, 48-worker federated edge-cloud testbed (single data centre, 50 ms emulated WAN) in a 1005-run campaign augmented by a fair-process-count sharded-oracle comparator. The federated market dominates a single-process oracle by 2-4% with 45 of 45 per-seed wins (sign-test p ~ 2.8e-14, Hodges-Lehmann median -39.6 ms); against a four-shard centralised orchestrator at equal process count the gap stays within +/-1.5% across all nine (pipeline, load) cells. Round-robin completion rate collapses 98.8% -> 22.4% -> 3.3% across arrival rates 5/10/15 pps while the market preserves completion; the advantage decomposes into three Walrasian properties (information completeness, admission control, price discovery). Federation withstands broker death and network partition (completion rate >= 98.7% across 75 cells), and sovereignty enforcement adds no measurable runtime overhead across 60 governance-grid runs. Heterogeneous-domain stressors and cross-site WAN deployment remain future work.

## 내 메모


