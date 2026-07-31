---
type: research-source
item_id: 1175
title: "C8s: A Confidential Kubernetes Architecture"
source: "arxiv"
published: "2026-04-27T21:42:57Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.26974"
url: "https://arxiv.org/abs/2604.26974v1"
generated_by: codex-research-db
aliases:
  - "C8s: A Confidential Kubernetes Architecture"
topics:
  - "kubernetes"
---

# C8s: A Confidential Kubernetes Architecture

[원문 열기](https://arxiv.org/abs/2604.26974v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`D32UGX3P`)
- 발행일: 2026-04-27T21:42:57Z
- 저자: Amean Asad, Patrick McClurg, João Andrade
- 식별자: `arxiv:2604.26974`

## 요약·초록

This paper presents C8s, a confidential computing architecture for Kubernetes that provides cryptographically rooted confidentiality, integrity, and verifiability guarantees for Kubernetes clusters from infrastructure operators. These guarantees are cryptographically provable to any independent third party verifier. The architecture is built on hardware Trusted Execution Environments (TEEs), specifically AMD SEV-SNP, Intel TDX, and NVIDIA Confidential Computing support, to establish an attestation-rooted trust boundary around confidential VMs. This design is compatible with managed Kubernetes services such as Amazon EKS, Google GKE, and Microsoft AKS, where the control plane cannot be attested. Under this boundary, three groups gain guarantees that are absent from conventional deployments. Data and artifact owners can deploy sensitive workloads and proprietary artifacts on third-party infrastructure without risking exfiltration. Compute providers can offer execution services without revealing workloads to cloud operators. End users can submit requests that remain opaque to all parties except the attested TEE processing them. Representative workloads include AI inference, securing AI model weights, and training or fine-tuning on sensitive data.

## 내 메모


