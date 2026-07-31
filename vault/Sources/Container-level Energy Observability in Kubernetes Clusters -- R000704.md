---
type: research-source
item_id: 704
title: "Container-level Energy Observability in Kubernetes Clusters"
source: "arxiv"
published: "2025-04-14T20:50:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2504.10702"
url: "https://arxiv.org/abs/2504.10702v1"
generated_by: codex-research-db
aliases:
  - "Container-level Energy Observability in Kubernetes Clusters"
topics:
  - "kubernetes"
---

# Container-level Energy Observability in Kubernetes Clusters

[원문 열기](https://arxiv.org/abs/2504.10702v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VS4UGPIX`)
- 발행일: 2025-04-14T20:50:34Z
- 저자: Bjorn Pijnacker, Brian Setz, Vasilios Andrikopoulos
- 식별자: `arxiv:2504.10702`

## 요약·초록

Kubernetes has been for a number of years the default cloud orchestrator solution across multiple application and research domains. As such, optimizing the energy efficiency of Kubernetes-deployed workloads is of primary interest towards controlling operational expenses by reducing energy consumption at data center level and allocated resources at application level. A lot of research in this direction aims on reducing the total energy usage of Kubernetes clusters without establishing an understanding of their workloads, i.e. the applications deployed on the cluster. This means that there are untapped potential improvements in energy efficiency that can be achieved through, for example, application refactoring or deployment optimization. For all these cases a prerequisite is establishing fine-grained observability down to the level of individual containers and their power draw over time. A state-of-the-art tool approved by the Cloud-Native Computing Foundation, Kepler, aims to provide this functionality, but has not been assessed for its accuracy and therefore fitness for purpose. In this work we start by developing an experimental procedure to this goal, and we conclude that the reported energy usage metrics provided by Kepler are not at a satisfactory level. As a reaction to this, we develop KubeWatt as an alternative to Kepler for specific use case scenarios, and demonstrate its higher accuracy through the same experimental procedure as we used for Kepler.

## 내 메모


