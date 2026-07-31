---
type: research-source
item_id: 418
title: "Blueprinting the Cloud: Unifying and Automatically Optimizing Cloud Data Infrastructures with BRAD"
source: "openalex"
published: "2024-07-01"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.14778/3681954.3682026"
url: "https://doi.org/10.14778/3681954.3682026"
generated_by: codex-research-db
aliases:
  - "Blueprinting the Cloud: Unifying and Automatically Optimizing Cloud Data Infrastructures with BRAD"
topics:
  - "cloud-infrastructure"
---

# Blueprinting the Cloud: Unifying and Automatically Optimizing Cloud Data Infrastructures with BRAD

[원문 열기](https://doi.org/10.14778/3681954.3682026)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`GPHTZZ37`)
- 발행일: 2024-07-01
- 저자: Geoffrey X. Yu, Ziniu Wu, Ferdi Kossmann, Tianyu Li, Markos Markakis, Amadou Ngom, Samuel Madden, Tim Kraska
- 식별자: `doi:10.14778/3681954.3682026`

## 요약·초록

Modern organizations manage their data with a wide variety of specialized cloud database engines (e.g., Aurora, BigQuery, etc.). However, designing and managing such infrastructures is hard. Developers must consider many possible designs with non-obvious performance consequences; moreover, current software abstractions tightly couple applications to specific systems (e.g., with engine-specific clients), making it difficult to change after initial deployment. A better solution would virtualize cloud data management, allowing developers to declaratively specify their workload requirements and rely on automated solutions to design and manage the physical realization. In this paper, we present a technique called blueprint planning that achieves this vision. The key idea is to project data infrastructure design decisions into a unified design space (blueprints). We then systematically search over candidate blueprints using cost-based optimization, leveraging learned models to predict the utility of a blueprint on the workload. We use this technique to build BRAD, the first cloud data virtualization system. BRAD users issue queries to a single SQL interface that can be backed by multiple cloud database services. BRAD automatically selects the most suitable engine for each query, provisions and manages resources to minimize costs, and evolves the infrastructure to adapt to workload shifts. Our evaluation shows that BRAD meet user-defined performance targets and improve cost-savings by 1.6--13× compared to serverless auto-scaling or HTAP systems.

## 내 메모


