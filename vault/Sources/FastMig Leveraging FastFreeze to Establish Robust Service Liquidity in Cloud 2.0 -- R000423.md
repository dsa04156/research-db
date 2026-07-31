---
type: research-source
item_id: 423
title: "FastMig: Leveraging FastFreeze to Establish Robust Service Liquidity in Cloud 2.0"
source: "openalex"
published: "2024-06-29"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2407.00313"
url: "http://arxiv.org/abs/2407.00313"
generated_by: codex-research-db
aliases:
  - "FastMig: Leveraging FastFreeze to Establish Robust Service Liquidity in Cloud 2.0"
topics:
  - "cloud-infrastructure"
---

# FastMig: Leveraging FastFreeze to Establish Robust Service Liquidity in Cloud 2.0

[원문 열기](http://arxiv.org/abs/2407.00313)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`SZHZ54QH`)
- 발행일: 2024-06-29
- 저자: Sorawit Manatura, Thanawat Chanikaphon, Chantana Chantrapornchai, Mohsen Amini Salehi
- 식별자: `doi:10.48550/arxiv.2407.00313`

## 요약·초록

Service liquidity across edge-to-cloud or multi-cloud will serve as the cornerstone of the next generation of cloud computing systems (Cloud 2.0). Provided that cloud-based services are predominantly containerized, an efficient and robust live container migration solution is required to accomplish service liquidity. In a nod to this growing requirement, in this research, we leverage FastFreeze, a popular platform for process checkpoint/restore within a container, and promote it to be a robust solution for end-to-end live migration of containerized services. In particular, we develop a new platform, called FastMig that proactively controls the checkpoint/restore operations of FastFreeze, thereby, allowing for robust live migration of containerized services via standard HTTP interfaces. The proposed platform introduces post-checkpointing and pre-restoration operations to enhance migration robustness. Notably, the pre-restoration operation includes containerized service startup options, enabling warm restoration and reducing the migration downtime. In addition, we develop a method to make FastFreeze robust against failures that commonly happen during the migration and even during the normal operation of a containerized service. Experimental results under real-world settings show that the migration downtime of a containerized service can be reduced by 30X compared to the situation where the original FastFreeze was deployed for the migration. Moreover, we demonstrate that FastMig and warm restoration method together can significantly mitigate the container startup overhead. Importantly, these improvements are achieved without any significant performance reduction and only incurs a small resource usage overhead, compared to the bare (\ie non-FastFreeze) containerized services.

## 내 메모


