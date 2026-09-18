---
type: research-source
item_id: 2926
title: "Ermes: a Stateful Serverless Platform for the Edge-to-Cloud Continuum"
source: "kurate"
published: "2026-09-16T16:59:33Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.18924"
url: "http://arxiv.org/abs/2609.18924v1"
generated_by: codex-research-db
aliases:
  - "Ermes: a Stateful Serverless Platform for the Edge-to-Cloud Continuum"
topics:
  - "cloud-infrastructure"
---

# Ermes: a Stateful Serverless Platform for the Edge-to-Cloud Continuum

[원문 열기](http://arxiv.org/abs/2609.18924v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- Zotero: created (`4C5BVRP4`)
- 발행일: 2026-09-16T16:59:33Z
- 저자: Matteo Cenzato, Dario d'Abate, Arianna Dragoni, Giacomo Orsenigo, Luca Tosetti, Matteo Briscini, Alessandro Margara
- 식별자: `arxiv:2609.18924`

## 요약·초록

Function-as-a-Service (FaaS) is a widely adopted paradigm to simplify application deployment across the edge-to-cloud continuum. However, its stateless nature forces functions to retrieve their state from external, typically cloud-centric, data stores, reintroducing the very latency that edge computing aims to eliminate. This issue is further exacerbated by location-agnostic schedulers and rigid, one-size-fits-all consistency models that fail to capture the diverse requirements of edge applications. In this paper, we propose Ermes, a distributed platform that natively integrates state management into the FaaS paradigm, enabling the joint distribution of computational workloads and application state across the edge-to-cloud continuum. Ermes organizes application state into logical units, termed collections, and employs a distributed coordination algorithm that jointly maps collections and functions onto the available nodes seeking to minimize the latency perceived by the clients. In addition, it supports fine-grained replication and per-collection consistency levels, ranging from sequential to eventual consistency, leaving developers the choice of how to resolve the trade-off between consistency and performance. The experimental evaluation shows that Ermes quickly turns remote state accesses into local ones and sustains low latency as the workload grows, and as clients move across the edge.

## 내 메모


