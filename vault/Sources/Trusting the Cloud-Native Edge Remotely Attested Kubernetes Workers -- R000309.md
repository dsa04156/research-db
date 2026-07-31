---
type: research-source
item_id: 309
title: "Trusting the Cloud-Native Edge: Remotely Attested Kubernetes Workers"
source: "arxiv"
published: "2024-05-16T14:29:28Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/icccn61486.2024.10637515"
url: "https://arxiv.org/abs/2405.10131v1"
generated_by: codex-research-db
aliases:
  - "Trusting the Cloud-Native Edge: Remotely Attested Kubernetes Workers"
topics:
  - "kubernetes"
  - "edge-computing"
---

# Trusting the Cloud-Native Edge: Remotely Attested Kubernetes Workers

[원문 열기](https://arxiv.org/abs/2405.10131v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FG3S97S3`)
- 발행일: 2024-05-16T14:29:28Z
- 저자: Jordi Thijsman, Merlijn Sebrechts, Filip De Turck, Bruno Volckaert
- 식별자: `doi:10.1109/icccn61486.2024.10637515`

## 요약·초록

A Kubernetes cluster typically consists of trusted nodes, running within the confines of a physically secure datacenter. With recent advances in edge orchestration, this is no longer the case. This poses a new challenge: how can we trust a device that an attacker has physical access to? This paper presents an architecture and open-source implementation that securely enrolls edge devices as trusted Kubernetes worker nodes. By providing boot attestation rooted in a hardware Trusted Platform Module, a strong base of trust is provided. A new custom controller directs a modified version of Keylime to cross the cloud-edge gap and securely deliver unique cluster credentials required to enroll an edge worker. The controller dynamically grants and revokes these credentials based on attestation events, preventing a possibly compromised node from accessing sensitive cluster resources. We provide both a qualitative and a quantitative evaluation of the architecture. The qualitative scenarios prove its ability to attest and enroll an edge device with role-based access control (RBAC) permissions that dynamically adjust to attestation events. The quantitative evaluation reflects an average of 10.28 seconds delay incurred on the startup time of the edge node due to attestation for a total average enrollment time of 20.91 seconds. The presented architecture thus provides a strong base of trust, securing a physically exposed edge device and paving the way for a robust and resilient edge computing ecosystem.

## 내 메모


