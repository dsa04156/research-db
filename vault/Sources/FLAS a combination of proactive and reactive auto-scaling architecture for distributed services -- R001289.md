---
type: research-source
item_id: 1289
title: "FLAS: a combination of proactive and reactive auto-scaling architecture for distributed services"
source: "arxiv"
published: "2025-10-23T09:38:07Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1016/j.future.2020.12.025"
url: "https://arxiv.org/abs/2510.20388v1"
generated_by: codex-research-db
aliases:
  - "FLAS: a combination of proactive and reactive auto-scaling architecture for distributed services"
topics:
  - "cloud-infrastructure"
---

# FLAS: a combination of proactive and reactive auto-scaling architecture for distributed services

[원문 열기](https://arxiv.org/abs/2510.20388v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`B7MBJGFZ`)
- 발행일: 2025-10-23T09:38:07Z
- 저자: Víctor Rampérez, Javier Soriano, David Lizcano, Juan A. Lara
- 식별자: `doi:10.1016/j.future.2020.12.025`

## 요약·초록

Cloud computing has established itself as the support for the vast majority of emerging technologies, mainly due to the characteristic of elasticity it offers. Auto-scalers are the systems that enable this elasticity by acquiring and releasing resources on demand to ensure an agreed service level. In this article we present FLAS (Forecasted Load Auto-Scaling), an auto-scaler for distributed services that combines the advantages of proactive and reactive approaches according to the situation to decide the optimal scaling actions in every moment. The main novelties introduced by FLAS are (i) a predictive model of the high-level metrics trend which allows to anticipate changes in the relevant SLA parameters (e.g. performance metrics such as response time or throughput) and (ii) a reactive contingency system based on the estimation of high-level metrics from resource use metrics, reducing the necessary instrumentation (less invasive) and allowing it to be adapted agnostically to different applications. We provide a FLAS implementation for the use case of a content-based publish-subscribe middleware (E-SilboPS) that is the cornerstone of an event-driven architecture. To the best of our knowledge, this is the first auto-scaling system for content-based publish-subscribe distributed systems (although it is generic enough to fit any distributed service). Through an evaluation based on several test cases recreating not only the expected contexts of use, but also the worst possible scenarios (following the Boundary-Value Analysis or BVA test methodology), we have validated our approach and demonstrated the effectiveness of our solution by ensuring compliance with performance requirements over 99% of the time.

## 내 메모


