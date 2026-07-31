---
type: research-source
item_id: 707
title: "HeteroPod: XPU-Accelerated Infrastructure Offloading for Commodity Cloud-Native Applications"
source: "arxiv"
published: "2025-03-31T11:11:16Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2503.23952"
url: "https://arxiv.org/abs/2503.23952v1"
generated_by: codex-research-db
aliases:
  - "HeteroPod: XPU-Accelerated Infrastructure Offloading for Commodity Cloud-Native Applications"
topics:
  - "kubernetes"
---

# HeteroPod: XPU-Accelerated Infrastructure Offloading for Commodity Cloud-Native Applications

[원문 열기](https://arxiv.org/abs/2503.23952v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SDH7MVRQ`)
- 발행일: 2025-03-31T11:11:16Z
- 저자: Bicheng Yang, Jingkai He, Dong Du, Yubin Xia, Haibo Chen
- 식별자: `arxiv:2503.23952`

## 요약·초록

Cloud-native systems increasingly rely on infrastructure services (e.g., service meshes, monitoring agents), which compete for resources with user applications, degrading performance and scalability. We propose HeteroPod, a new abstraction that offloads these services to Data Processing Units (DPUs) to enforce strict isolation while reducing host resource contention and operational costs. To realize HeteroPod, we introduce HeteroNet, a cross-PU (XPU) network system featuring: (1) split network namespace, a unified network abstraction for processes spanning CPU and DPU, and (2) elastic and efficient XPU networking, a communication mechanism achieving shared-memory performance without pinned resource overhead and polling costs. By leveraging HeteroNet and the compositional nature of cloud-native workloads, HeteroPod can optimally offload infrastructure containers to DPUs. We implement HeteroNet based on Linux, and implement a cloud-native system called HeteroK8s based on Kubernetes. We evaluate the systems using NVIDIA Bluefield-2 DPUs and CXL-based DPUs (simulated with real CXL memory devices). The results show that HeteroK8s effectively supports complex (unmodified) commodity cloud-native applications (up to 1 million LoC) and provides up to 31.9x better latency and 64x less resource consumption (compared with kernel-bypass design), 60% better end-to-end latency, and 55% higher scalability compared with SOTA systems.

## 내 메모


