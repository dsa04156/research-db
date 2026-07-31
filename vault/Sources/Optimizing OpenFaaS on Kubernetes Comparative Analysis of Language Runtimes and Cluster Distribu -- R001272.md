---
type: research-source
item_id: 1272
title: "Optimizing OpenFaaS on Kubernetes: Comparative Analysis of Language Runtimes and Cluster Distributions"
source: "arxiv"
published: "2026-04-07T06:38:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.05496"
url: "https://arxiv.org/abs/2604.05496v1"
generated_by: codex-research-db
aliases:
  - "Optimizing OpenFaaS on Kubernetes: Comparative Analysis of Language Runtimes and Cluster Distributions"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Optimizing OpenFaaS on Kubernetes: Comparative Analysis of Language Runtimes and Cluster Distributions

[원문 열기](https://arxiv.org/abs/2604.05496v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`A23BNGW5`)
- 발행일: 2026-04-07T06:38:29Z
- 저자: Ehsan Ataie, Mohammadreza Pooshani, Hossein Aqasizade
- 식별자: `arxiv:2604.05496`

## 요약·초록

Serverless computing, particularly Function-as-a-Service (FaaS), has revolutionized cloud computing by abstracting infrastructure management and enabling dynamic resource allocation. This paper examines the performance and compatibility of OpenFaaS, an open-source serverless platform, when deployed on various Kubernetes distributions, including Kubeadm, K3s, MicroK8s, and K0s. Moreover, leveraging the CloudLab infrastructure, this study examines the impact of Python, Go, and Node$.$js programming languages on the performance of Kubernetes-enabled OpenFaaS, specifically when these languages are used to develop functions deployed on the platform. The performance is evaluated and analyzed under various levels of concurrent invocations using several usage-level metrics, such as throughput and CPU usage, as well as responsiveness metrics, such as delay. According to our findings, Go consistently outperforms Python and Node$.$js in terms of throughput and CPU usage, making it the ideal runtime for serverless applications. Among the Kubernetes distributions, K3s and Kubeadm exhibit superior performance, with Kubeadm maintaining low latency and efficient CPU usage, and K3s demonstrating high throughput. This study provides valuable insights into optimizing the Kubernetes-enabled OpenFaaS platform, highlighting the strengths and trade-offs of different Kubernetes distributions and language runtimes.

## 내 메모


