---
type: research-source
item_id: 777
title: "Unlocking True Elasticity for the Cloud-Native Era with Dandelion"
source: "arxiv"
published: "2025-05-02T21:53:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3731569.3764803"
url: "https://arxiv.org/abs/2505.01603v2"
generated_by: codex-research-db
aliases:
  - "Unlocking True Elasticity for the Cloud-Native Era with Dandelion"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Unlocking True Elasticity for the Cloud-Native Era with Dandelion

[원문 열기](https://arxiv.org/abs/2505.01603v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TUNCH6N7`)
- 발행일: 2025-05-02T21:53:29Z
- 저자: Tom Kuchler, Pinghe Li, Yazhuo Zhang, Lazar Cvetković, Boris Goranov, Tobias Stocker, Leon Thomm, Simone Kalbermatter, Tim Notter, Andrea Lattuada, Ana Klimovic
- 식별자: `doi:10.1145/3731569.3764803`

## 요약·초록

Elasticity is fundamental to cloud computing, as it enables quickly allocating resources to match the demand of each workload as it arrives, rather than pre-provisioning resources to meet performance objectives. However, even serverless platforms -- which boot sandboxes in 10s to 100s of milliseconds -- are not sufficiently elastic to avoid over-provisioning expensive resources. Today's FaaS platforms rely on pre-provisioning many idle sandboxes in memory to reduce the occurrence of slow, cold starts. A key obstacle for high elasticity is booting a guest OS and configuring features like networking in sandboxes, which are required to expose an isolated POSIX-like interface to user functions. Our key insight is that redesigning the interface for applications in the cloud-native era enables co-designing a much more efficient and elastic execution system. Now is a good time to rethink cloud abstractions as developers are building applications to be cloud-native. Cloud-native applications typically consist of user-provided compute logic interacting with cloud services (for storage, AI inference, query processing, etc) exposed over REST APIs. Hence, we propose Dandelion, an elastic cloud platform with a declarative programming model that expresses applications as DAGs of pure compute functions and higher-level communication functions. Dandelion can securely execute untrusted user compute functions in lightweight sandboxes that cold start in hundreds of microseconds, since pure functions do not rely on extra software environments such as a guest OS. Dandelion makes it practical to boot a sandbox on-demand for each request, decreasing performance variability by two to three orders of magnitude compared to Firecracker and reducing committed memory by 96% on average when running the Azure Functions trace.

## 내 메모


