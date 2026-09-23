---
type: research-source
item_id: 2962
title: "A Kubernetes-Native Request Router for Quality-Aware Inference Serving in the Computing Continuum"
source: "arxiv"
published: "2026-09-17T14:45:21Z"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "arxiv:2609.20497"
url: "https://arxiv.org/abs/2609.20497v1"
generated_by: codex-research-db
aliases:
  - "A Kubernetes-Native Request Router for Quality-Aware Inference Serving in the Computing Continuum"
topics:
  - "kubernetes"
---

# A Kubernetes-Native Request Router for Quality-Aware Inference Serving in the Computing Continuum

[원문 열기](https://arxiv.org/abs/2609.20497v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`75FN42HW`)
- 발행일: 2026-09-17T14:45:21Z
- 저자: Ignjat Karanovic, Pantelis A. Frangoudis, Ivan Čilić, Ivana Podnar Žarko, Schahram Dustdar
- 식별자: `arxiv:2609.20497`

## 요약·초록

We introduce Adaptive Score-based Routing Balancer (ASRB), a dynamic, score-based request routing mechanism for Kubernetes-based service deployments over the computing continuum. ASRB jointly considers infrastructure-level information, response time measurements, and application-level quality indicators, with a particular focus on serving Machine Learning (ML) workloads. For these workloads, ASRB balances requests over service instances deployed in the continuum, following service provider-defined policies encoded as weighted combinations of QoS criteria to flexibly address latency-accuracy trade-offs. To drive routing decisions and swiftly adapt to changes in the operating environment, ASRB monitors a range of runtime metrics across multiple system layers. To deal with the associated monitoring overhead, particularly important for large-scale deployments, it selectively and adaptively controls monitoring intensity without sacrificing on routing quality. ASRB is implemented without requiring any modifications to Kubernetes, making it straightforward to deploy and operate in existing cluster environments. Our testbed experiments demonstrate the versatility of ASRB: When tuned for latency reduction, it achieves at least 10 ms lower mean response time compared with latency-oriented state-of-the-art routing mechanisms, while it achieves higher accuracy when this is prioritized through specific configurations, thus enabling flexible and operator-controllable trade-offs. At the same time, it attains reduced failure rates, higher responsiveness to changes in the operating environment, and up to ~70% less monitoring cost than relevant state-of-the-art solutions, at the potential expense of only a modest latency penalty in some configurations.

## 내 메모
