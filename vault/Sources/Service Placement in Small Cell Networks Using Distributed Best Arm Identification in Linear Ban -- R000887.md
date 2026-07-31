---
type: research-source
item_id: 887
title: "Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits"
source: "arxiv"
published: "2025-06-22T12:45:01Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2506.22480"
url: "https://arxiv.org/abs/2506.22480v2"
generated_by: codex-research-db
aliases:
  - "Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits"
topics:
  - "edge-computing"
---

# Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits

[원문 열기](https://arxiv.org/abs/2506.22480v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`W9X7UUST`)
- 발행일: 2025-06-22T12:45:01Z
- 저자: Mariam Yahya, Aydin Sezgin, Setareh Maghsudi
- 식별자: `arxiv:2506.22480`

## 요약·초록

As users in small cell networks increasingly rely on computation-intensive services, cloud-based access often results in high latency. Multi-access edge computing (MEC) mitigates this by bringing computational resources closer to end users, with small base stations (SBSs) serving as edge servers to enable low-latency service delivery. However, limited edge capacity makes it challenging to decide which services to deploy locally versus in the cloud, especially under unknown service demand and dynamic network conditions. To tackle this problem, we model service demand as a linear function of service attributes and formulate the service placement task as a linear bandit problem, where SBSs act as agents and services as arms. The goal is to identify the service that, when placed at the edge, offers the greatest reduction in total user delay compared to cloud deployment. We propose a distributed and adaptive multi-agent best-arm identification (BAI) algorithm under a fixed-confidence setting, where SBSs collaborate to accelerate learning. Simulations show that our algorithm identifies the optimal service with the desired confidence and achieves near-optimal speedup, as the number of learning rounds decreases proportionally with the number of SBSs. We also provide theoretical analysis of the algorithm's sample complexity and communication overhead.

## 내 메모


