---
type: research-source
item_id: 709
title: "Enable Time-Sensitive Applications in Kubernetes with Container Network Interface Plugin Agnostic Metadata Proxy"
source: "arxiv"
published: "2025-03-17T07:16:31Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2503.12878"
url: "https://arxiv.org/abs/2503.12878v1"
generated_by: codex-research-db
aliases:
  - "Enable Time-Sensitive Applications in Kubernetes with Container Network Interface Plugin Agnostic Metadata Proxy"
topics:
  - "kubernetes"
---

# Enable Time-Sensitive Applications in Kubernetes with Container Network Interface Plugin Agnostic Metadata Proxy

[원문 열기](https://arxiv.org/abs/2503.12878v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NIU72Q3S`)
- 발행일: 2025-03-17T07:16:31Z
- 저자: Ferenc Orosi, Ferenc Fejes
- 식별자: `arxiv:2503.12878`

## 요약·초록

Application deployment in cloud environment is dominated by Kubernetes-orchestrated microservices. Provides a secure environment, networking, storage, isolation, scheduling, and many other abstractions that can be easily extended to meet our needs. Time-Sensitive Applications (TSAs) have special requirements for compute and network. Deploying TSAs in Kubernetes is challenging because the networking implemented by Container Network Interface (CNI) plugins is not aware of the traffic characteristic required by Time-Sensitive Network. Even if a network interface supports TSN features (e.g.: Scheduled Traffic) and a modified CNI plugin is aware of this interface, the pod network isolation built on top of Linux deletes the metadata required for TSN protocols to work with. We propose TSN metadata proxy, a simple architecture that allows any TSA microservice to use the TSN capabilities of the physical NIC, without any modification. This architecture is tightly integrated with the Kubernetes networking model, works with popular CNI plugins, and supports services such as ClusterIP, NodePort, or LoadBalancer without additional configuration. Unlike former proposals, this architecture does not require either bypassing the Linux kernel network stack, direct access to the physical NIC, escalated privileges for the TSA microservice, or even modification of the TSA.

## 내 메모


