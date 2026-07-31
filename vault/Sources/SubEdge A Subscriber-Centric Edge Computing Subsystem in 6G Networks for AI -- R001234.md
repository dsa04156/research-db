---
type: research-source
item_id: 1234
title: "SubEdge: A Subscriber-Centric Edge Computing Subsystem in 6G Networks for AI"
source: "openalex"
published: "2026-06-29"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.30554"
url: "https://arxiv.org/abs/2606.30554"
generated_by: codex-research-db
aliases:
  - "SubEdge: A Subscriber-Centric Edge Computing Subsystem in 6G Networks for AI"
topics:
  - "edge-computing"
---

# SubEdge: A Subscriber-Centric Edge Computing Subsystem in 6G Networks for AI

[원문 열기](https://arxiv.org/abs/2606.30554)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`Q69W6SI9`)
- 발행일: 2026-06-29
- 저자: Abdirazak Ali Asir Rage, Riccardo Pozza, Rahim Tafazolli
- 식별자: `arxiv:2606.30554`

## 요약·초록

Beyond traditional connectivity, 6G is envisioned to transform mobile networks into a distributed fabric that provides native integrated communication, computing, and intelligence services. AI-native terminals (e.g., robots, autonomous vehicles, and smart glasses) require real-time inference from individualised, manufacturer-specific models that cannot be executed on-board nor shared across subscribers, making per-subscriber edge compute the necessary complement to per-subscriber connectivity. Existing Network for AI (Net4AI) architectures provision compute for application providers through shared deployments and do not address per-subscriber provisioning. This paper proposes SubEdge, a Net4AI subsystem that provisions integrated communication and compute resources on a per-subscriber basis, ensuring the coupled migration of both dimensions to maintain service continuity during mobility. SubEdge contributes the computing context--a per-subscriber data structure binding a Subscription Permanent Identifier (SUPI) to its inference container, edge node, and service entitlement--and a mobility-event-driven mechanism that simultaneously migrates the subscriber's compute instance and its traffic-routing policy when the serving cell changes. SubEdge operates as an Application Function over existing Network Exposure Function (NEF) APIs with zero 3GPP core modifications. Experimental evaluation on a real-world testbed shows that SubEdge's mobility-driven joint communication-and-compute migration reduces 95th-percentile latency from 22.9 ms to 12.2 ms with zero packet loss across six mobility events, sustains 99.92% frame delivery for an end-to-end 30 fps inference workload, and completes 1,560 migration operations across batches of up to 50 simultaneously migrating subscribers with 100% success.

## 내 메모


