---
type: research-source
item_id: 793
title: "Komet: A Serverless Platform for Low-Earth Orbit Edge Services"
source: "arxiv"
published: "2024-10-08T12:20:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3698038.3698517"
url: "https://arxiv.org/abs/2410.05973v1"
generated_by: codex-research-db
aliases:
  - "Komet: A Serverless Platform for Low-Earth Orbit Edge Services"
topics:
  - "cloud-infrastructure"
  - "edge-computing"
---

# Komet: A Serverless Platform for Low-Earth Orbit Edge Services

[원문 열기](https://arxiv.org/abs/2410.05973v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3FSI4BKH`)
- 발행일: 2024-10-08T12:20:41Z
- 저자: Tobias Pfandzelter, David Bermbach
- 식별자: `doi:10.1145/3698038.3698517`

## 요약·초록

Low-Earth orbit satellite networks can provide global broadband Internet access using constellations of thousands of satellites. Integrating edge computing resources in such networks can enable global low-latency access to compute services, supporting end users in rural areas, remote industrial applications, or the IoT. To achieve this, resources must be carefully allocated to various services from multiple tenants. Moreover, applications must navigate the dynamic nature of satellite networks, where orbital mechanics necessitate frequent client hand-offs. Therefore, managing applications on the low-Earth orbit edge will require the right platform abstractions. We introduce Komet, a serverless platform for low-Earth orbit edge computing. Komet integrates Function-as-a-Service compute with data replication, enabling on-demand elastic edge resource allocation and frequent service migration against satellite orbital trajectories to keep services deployed in the same geographic region. We implement Komet as a proof-of-concept prototype and demonstrate how its abstractions can be used to build low-Earth orbit edge applications with high availability despite constant mobility. Further, we propose simple heuristics for service migration scheduling in different application scenarios and evaluate them in simulation based on our experiment traces, showing the trade-off between selecting an optimal satellite server at every instance and minimizing service migration frequency.

## 내 메모


