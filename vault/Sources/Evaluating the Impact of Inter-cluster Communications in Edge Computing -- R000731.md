---
type: research-source
item_id: 731
title: "Evaluating the Impact of Inter-cluster Communications in Edge Computing"
source: "arxiv"
published: "2024-09-14T03:02:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2409.09278"
url: "https://arxiv.org/abs/2409.09278v3"
generated_by: codex-research-db
aliases:
  - "Evaluating the Impact of Inter-cluster Communications in Edge Computing"
topics:
  - "edge-computing"
  - "kubernetes"
---

# Evaluating the Impact of Inter-cluster Communications in Edge Computing

[원문 열기](https://arxiv.org/abs/2409.09278v3)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`68N5SG26`)
- 발행일: 2024-09-14T03:02:32Z
- 저자: Marc Michalke, Iulisloi Zacarias, Admela Jukan, Kfir Toledo, Etai Lev-Ran
- 식별자: `arxiv:2409.09278`

## 요약·초록

Distributed applications based on micro-services in edge computing are becoming increasingly popular due to the rapid evolution of mobile networks. While Kubernetes is the default framework when it comes to orchestrating and managing micro-service-based applications in mobile networks, the requirement to run applications between multiple sites at cloud and edge poses new challenges. Since Kubernetes does not natively provide tools to abstract inter-cluster communications at the application level, inter-cluster communication in edge computing is becoming increasingly critical to the application performance. In this paper, we evaluate for the first time the impact of inter-cluster communication on edge computing performance by using three prominent, open source inter-cluster communication projects and tools, i.e., Submariner, ClusterLink and Skupper. We develop a fully open-source testbed that integrates these tools in a modular fashion, and experimentally benchmark sample applications, including the ML class of applications, on their performance running in the multi-cluster edge computing system under varying networking conditions. We experimentally analyze two classes of envisioned mobile applications, i.e., a) industrial automation, b) vehicle decision drive assist. Our results show that ClusterLink performs best out of the three tools in scenarios with increased payloads, regardless of the underlying networking conditions or transmission direction between clusters. It is closely followed by Skupper, unless request and reply both transport significant amounts of data. Finally, when requesting smaller amounts of data from a service, Submariner slightly outperforms Skupper and ClusterLink regardless of the inter-node networking conditions.

## 내 메모


