---
type: research-source
item_id: 318
title: "Kubernetes in Action: Exploring the Performance of Kubernetes Distributions in the Cloud"
source: "arxiv"
published: "2024-03-03T07:55:13Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2403.01429"
url: "https://arxiv.org/abs/2403.01429v1"
generated_by: codex-research-db
aliases:
  - "Kubernetes in Action: Exploring the Performance of Kubernetes Distributions in the Cloud"
topics:
  - "kubernetes"
---

# Kubernetes in Action: Exploring the Performance of Kubernetes Distributions in the Cloud

[원문 열기](https://arxiv.org/abs/2403.01429v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZE4973CC`)
- 발행일: 2024-03-03T07:55:13Z
- 저자: Hossein Aqasizade, Ehsan Ataie, Mostafa Bastam
- 식별자: `arxiv:2403.01429`

## 요약·초록

Kubernetes has emerged as a leading open-source platform for container orchestration, allowing organizations to efficiently manage and deploy containerized applications at scale. This paper investigates the performance of four Kubernetes distributions, namely Kubeadm, K3s, MicroK8s, and K0s when running OpenFaaS as a containerized service on a cluster of computing nodes on CloudLab. For this purpose, experiments are conducted to examine the performance of two virtualization modes, namely HVM and PV, supported by Xen as the underlying hypervisor. Moreover, two container runtimes that are integrated with Kubernetes, namely Docker, and Containerd, are examined to assess their performance on both disk-intensive and CPU-intensive workloads. After determining the appropriate underlying Xen mode and container runtime, the Kubernetes distributions are set up and their performance is measured using various metrics, such as request rate, CPU utilization, and scaling behavior.

## 내 메모


