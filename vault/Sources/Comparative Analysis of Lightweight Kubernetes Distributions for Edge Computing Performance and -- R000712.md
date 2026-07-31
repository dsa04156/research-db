---
type: research-source
item_id: 712
title: "Comparative Analysis of Lightweight Kubernetes Distributions for Edge Computing: Performance and Resource Efficiency"
source: "arxiv"
published: "2025-03-04T20:03:51Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1007/978-3-031-84617-5_7"
url: "https://arxiv.org/abs/2504.03656v1"
generated_by: codex-research-db
aliases:
  - "Comparative Analysis of Lightweight Kubernetes Distributions for Edge Computing: Performance and Resource Efficiency"
topics:
  - "edge-computing"
  - "kubernetes"
---

# Comparative Analysis of Lightweight Kubernetes Distributions for Edge Computing: Performance and Resource Efficiency

[원문 열기](https://arxiv.org/abs/2504.03656v1)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZDQCUEEZ`)
- 발행일: 2025-03-04T20:03:51Z
- 저자: Diyaz Yakubov, David Hästbacka
- 식별자: `doi:10.1007/978-3-031-84617-5_7`

## 요약·초록

Edge computing environments increasingly rely on lightweight container orchestration platforms to manage resource-constrained devices. This paper provides an empirical analysis of five lightweight kubernetes distributions (KD)(k0s, k3s, KubeEdge, OpenYurt, and Kubernetes (k8s)) focusing on their performance and resource efficiency in edge computing scenarios. We evaluated key metrics such as CPU, memory, disk usage, throughput, and latency under varying workloads, utilizing a testbed of Intel NUCs and Raspberry Pi devices. Our results demonstrate significant differences in performance: k3s exhibited the lowest resource consumption, while k0s and k8s excelled in data plane throughput and latency. Under heavy stress scenarios, k3s and k0s accomplished the same workloads faster than the other distributions. OpenYurt offered balanced performance, suitable for hybrid cloud-edge use cases, but was less efficient in terms of resource usage and scalability compared to k0s, k3s and k8s. KubeEdge, although feature-rich for edge environments, exhibited higher resource consumption and lower scalability. These findings offer valuable insights for developers and operators selecting appropriate KD based on specific performance and resource efficiency requirements for edge computing environments.

## 내 메모


