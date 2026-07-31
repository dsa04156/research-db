---
type: research-source
item_id: 317
title: "Enabling 5G QoS configuration capabilities for IoT applications on container orchestration platform"
source: "arxiv"
published: "2024-03-08T21:38:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/cloudcom59040.2023.00023"
url: "https://arxiv.org/abs/2403.05686v1"
generated_by: codex-research-db
aliases:
  - "Enabling 5G QoS configuration capabilities for IoT applications on container orchestration platform"
topics:
  - "kubernetes"
---

# Enabling 5G QoS configuration capabilities for IoT applications on container orchestration platform

[원문 열기](https://arxiv.org/abs/2403.05686v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`624PCNVX`)
- 발행일: 2024-03-08T21:38:43Z
- 저자: Yu Liu, Aitor Hernandez Herranz
- 식별자: `doi:10.1109/cloudcom59040.2023.00023`

## 요약·초록

Container orchestration platform is the foundation of modern cloud infrastructure. In recent years, container orchestration platform has been evolving to cross the boundary of device, edge, and cloud. More and more IoT applications such as robotics and XR have been deployed across the device-cloud continuum through the container orchestration platform, e.g., the Kubernetes (K8s) framework. Meanwhile, the rapid expansion of advanced communication technologies like 5G has endorsed the revolution in IoT applications as more network resource is available for critical IoT use cases. This paper aims to integrate network configuration capabilities provided by a 5G Network Exposure Function (NEF) into the K8s framework which is used to simplify application deployment in an orchestration in the device-cloud continuum. Specifically, a Linux fwmark-based network Quality of Service (QoS) configuration method is proposed to expose the QoS information from an overlay network that is used by the container orchestration platform to the underlay network. A Container Network Interface (CNI) plugin-based implementation is demonstrated to perform QoS configuration for the 5G network. The proposed solution is validated with an existing localization and mapping application to verify the feasibility. The proposed solution has the following benefits: (1) The solution is a Kubernetes-native approach which adopts the CNI plugin mechanism. (2) The solution can expose the QoS information from an overlay network to an underlay network in a non-intrusive manner. (3) No packet manipulation is required to greatly reduce the overhead for packet processing. (4) It extends the K8s bandwidth limit feature from on-node to the access network. (5) It is compatible with the 5G infrastructure without any alteration or adding extra complexity.

## 내 메모


