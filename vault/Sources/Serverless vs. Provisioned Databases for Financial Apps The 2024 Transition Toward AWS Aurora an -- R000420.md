---
type: research-source
item_id: 420
title: "Serverless vs. Provisioned Databases for Financial Apps: The 2024 Transition Toward AWS Aurora and PostgreSQL for Zero-Downtime Banking Resilience"
source: "openalex"
published: "2024-06-30"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.22399/ijcesen.4992"
url: "https://doi.org/10.22399/ijcesen.4992"
generated_by: codex-research-db
aliases:
  - "Serverless vs. Provisioned Databases for Financial Apps: The 2024 Transition Toward AWS Aurora and PostgreSQL for Zero-Downtime Banking Resilience"
topics:
  - "cloud-infrastructure"
---

# Serverless vs. Provisioned Databases for Financial Apps: The 2024 Transition Toward AWS Aurora and PostgreSQL for Zero-Downtime Banking Resilience

[원문 열기](https://doi.org/10.22399/ijcesen.4992)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`B5JNJ9FE`)
- 발행일: 2024-06-30
- 저자: Venkateswarlu Boggavarapu
- 식별자: `doi:10.22399/ijcesen.4992`

## 요약·초록

In 2024, the financial services sector underwent a decisive transformation in how mission-critical databases are architected and maintained. Traditional provisioned database systems—long considered the backbone of secure and stable banking—revealed deep limitations when exposed to modern demand patterns characterized by mobile-first usage, real-time fraud pipelines, and global 24/7 service expectations. These provisioned architectures, including fixed-capacity deployments of Amazon RDS and self-managed PostgreSQL, struggle with load volatility, demand unpredictability, and prolonged maintenance windows, often resulting in 45–60 minutes of downtime during major version upgrades, an unacceptable risk in today’s financial landscape. In contrast, Amazon Aurora PostgreSQL, particularly in its Serverless v2 configuration, emerged as the architectural foundation of choice for global institutions such as Goldman Sachs and Capital One. Aurora’s distributed, log-structured storage—replicated across three Availability Zones—along with its quorum-based commit protocol, delivered unmatched fault tolerance and performance gains of up to 3× over standard PostgreSQL. More importantly, capabilities such as Blue/Green Deployments enabled near-zero-downtime upgrades, reducing operational interruptions from nearly an hour to less than 30 seconds. With the rise of Aurora Serverless v2, banks embraced fine-grained, sub-second elasticity through Aurora Capacity Units (ACUs), enabling automatic scaling in response to real-time demand spikes while reducing costs by up to 75% through FinOps-optimized consumption models. This article combines architectural analysis with mathematical modeling and real-world case studies, demonstrating why these technologies form the foundation of Agentic Commerce—a future where autonomous AI agents execute financial decisions and transactions that demand continuously available, elastic, and resilient data backends.

## 내 메모


