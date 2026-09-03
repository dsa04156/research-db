---
type: research-source
item_id: 2536
title: "Serverless edge intelligence for SLA-aware function placement and resource slicing in wireless networks"
source: "openalex"
published: "2026-09-01"
first_seen: "2026-09-03"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-69441-2"
url: "https://doi.org/10.1038/s41598-026-69441-2"
generated_by: codex-research-db
aliases:
  - "Serverless edge intelligence for SLA-aware function placement and resource slicing in wireless networks"
topics:
  - "cloud-infrastructure"
---

# Serverless edge intelligence for SLA-aware function placement and resource slicing in wireless networks

[원문 열기](https://doi.org/10.1038/s41598-026-69441-2)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-03|2026-09-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`3PXFN62Z`)
- 발행일: 2026-09-01
- 저자: Amin Mohajer, Abbas Mirzaei, Babak Nouri-Moghaddam, Ali Ghaffari, Maryam Bavaghar, Xavier Fernando
- 식별자: `doi:10.1038/s41598-026-69441-2`

## 요약·초록

Wireless edge networks must support delay-sensitive services under fluctuating traffic, interference, heterogeneous SLA priorities, and limited radio, computing, and memory resources. This paper proposes Serverless-PRONTO, an SLA-aware orchestration framework that jointly controls serverless function placement, task offloading, bandwidth allocation, CPU slicing, and warm-instance management. The system model captures uplink and downlink transmission, queueing, execution, cold-start initialization, and memory occupied by retained function instances. To solve the resulting dynamic, partially observable, mixed discrete-continuous problem, Serverless-PRONTO combines a physics-aware sparse graph encoder with multi-agent TD3 under centralized training and decentralized execution. The encoder represents inter-node coupling through channel, interference, distance, queue, resource, function-demand, and cold-start features, while top- \(\:K\) attention limits signaling. An SLA-risk mechanism prioritizes requests according to urgency, queue state, service class, and cold-start probability. A sequential feasibility projection converts raw actor outputs into valid placement, bandwidth, CPU, and memory decisions. Simulations against four serverless and edge-orchestration baselines under varying traffic loads and network sizes show higher SLA satisfaction, lower end-to-end delay and cold-start ratio, and more stable scalability, demonstrating the benefit of jointly coordinating wireless resources and serverless runtime states.

## 내 메모


