---
type: research-source
item_id: 800
title: "Litmus: Fair Pricing for Serverless Computing"
source: "arxiv"
published: "2024-08-01T17:21:26Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3622781.3674181"
url: "https://arxiv.org/abs/2408.00731v1"
generated_by: codex-research-db
aliases:
  - "Litmus: Fair Pricing for Serverless Computing"
topics:
  - "cloud-infrastructure"
---

# Litmus: Fair Pricing for Serverless Computing

[원문 열기](https://arxiv.org/abs/2408.00731v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5U2RDHS9`)
- 발행일: 2024-08-01T17:21:26Z
- 저자: Qi Pei, Yipeng Wang, Seunghee Shin
- 식별자: `doi:10.1145/3622781.3674181`

## 요약·초록

Serverless computing has emerged as a market-dominant paradigm in modern cloud computing, benefiting both cloud providers and tenants. While service providers can optimize their machine utilization, tenants only need to pay for the resources they use. To maximize resource utilization, these serverless systems co-run numerous short-lived functions, bearing frequent system condition shifts. When the system gets overcrowded, a tenant's function may suffer from disturbing slowdowns. Ironically, tenants also incur higher costs during these slowdowns, as commercial serverless platforms determine costs proportional to their execution times. This paper argues that cloud providers should compensate tenants for losses incurred when the server is over-provisioned. However, estimating tenants' losses is challenging without pre-profiled information about their functions. Prior studies have indicated that assessing tenant losses leads to heavy overheads. As a solution, this paper introduces a new pricing model that offers discounts based on the machine's state while presuming the tenant's loss under that state. To monitor the machine state accurately, Litmus pricing frequently conducts Litmus tests, an effective and lightweight solution for measuring system congestion. Our experiments show that Litmus pricing can accurately gauge the impact of system congestion and offer nearly ideal prices, with only a 0.2% price difference on average, in a heavily congested system.

## 내 메모


