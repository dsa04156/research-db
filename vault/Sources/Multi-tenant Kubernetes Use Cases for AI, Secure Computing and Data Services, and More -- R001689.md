---
type: research-source
item_id: 1689
title: "Multi-tenant Kubernetes Use Cases for AI, Secure Computing and Data Services, and More"
source: "arxiv"
published: "2026-08-01T16:24:11Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "doi:10.1145/3837730.3837733"
url: "https://arxiv.org/abs/2608.00742v1"
generated_by: codex-research-db
aliases:
  - "Multi-tenant Kubernetes Use Cases for AI, Secure Computing and Data Services, and More"
topics:
  - "kubernetes"
---

# Multi-tenant Kubernetes Use Cases for AI, Secure Computing and Data Services, and More

[원문 열기](https://arxiv.org/abs/2608.00742v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FJHWM8XT`)
- 발행일: 2026-08-01T16:24:11Z
- 저자: Jake Watson, Sadaf R Alam, Christopher Woods, Abdelwahab Kawafi, Thomas Green, Ian Johnson, Ellis Pires, Jessica R. Jones, Utz-Uwe Haus
- 식별자: `doi:10.1145/3837730.3837733`

## 요약·초록

Kubernetes, as a container orchestration engine, has been widely used in cloud-native ecosystems for several years. In supercomputing ecosystems, especially where bare-metal performance for compute and network devices are considered, the adoption is somewhat limited. However, with the increasing diversity of use cases such as AI, secure and confidential computing for sensitive data, and mixed workload orchestration, a traditional, single-tenant batch computing system does not offer the flexibility and reproducibility to which public cloud users are accustomed. Note that Kubernetes is not considered a replacement for batch scheduling systems, which have powerful features for large-scale MPI jobs with thousands of network end points. Rather, it is a complementary service provided as part of a national AI Research Resource. We evaluate Kubernetes deployment on a Hewlett Packard Enterprise (HPE) Cray EX supercomputerwith HPE Slingshot interconnect, called Isambard-AI, with co-design use cases. One is a Trusted Research Environment used for medical and health sciences. The other combines KubeRay, Ray, and vLLM to provide a distributed, sandboxed, persistent AI model hosting service targeting multi-tenant confidential computing. We discuss challenges and lessons learned, and where further development is needed to offer a production Kubernetes-as-a-Service on HPE Cray EX (and later) platforms.

## 내 메모


