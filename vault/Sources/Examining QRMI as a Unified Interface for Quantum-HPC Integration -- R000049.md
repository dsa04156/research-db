---
type: research-source
item_id: 49
title: "Examining QRMI as a Unified Interface for Quantum-HPC Integration"
source: "arxiv"
published: "2026-07-21T21:33:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19591"
url: "https://arxiv.org/abs/2607.19591v1"
generated_by: codex-research-db
aliases:
  - "Examining QRMI as a Unified Interface for Quantum-HPC Integration"
topics:
  - "kubernetes"
---

# Examining QRMI as a Unified Interface for Quantum-HPC Integration

[원문 열기](https://arxiv.org/abs/2607.19591v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FA2S3E6A`)
- 발행일: 2026-07-21T21:33:29Z
- 저자: Thomas Badts, Tim Boyle, Claudio Carvalho, Antonio Córcoles, Andrew Damin, Vadim Elisseev, Jonathan Frassineti, Daniel Gruber, Hiroshi Horii, Eun-Kyung Lee, James Machin, Sara Marzella, Mateusz Meller, Daniel Milroy, Matthieu Moreau, Munetaka Ohtani, Elisabeth Ortega-Carrasco, Doug Oucharek, Yoonho Park, Adarsh Patil, Emre M. Sahin, Gábor Samu, Seetharami Seelam, Amir Shehata, Vanessa Sochat, James Thorne, Oscar Wallis, Aleksander Wennersteen
- 식별자: `arxiv:2607.19591`

## 요약·초록

The efficient and scalable integration of quantum resources into high-performance computing (HPC) environments requires standardized mechanisms for resource management, scheduling, and workflow orchestration across diverse and heterogeneous infrastructures. The Quantum Resource Management Interface (QRMI) addresses this challenge through a thin, vendor-agnostic middleware layer that provides standardized APIs for scheduling, executing, and monitoring quantum workloads while exposing quantum resources as first-class schedulable resources alongside CPUs and GPUs. Although previous work demonstrated QRMI integration with the Slurm workload manager, its applicability across other workload managers remained unexamined. This paper extends the validation of QRMI to a broad range of workload managers, including PBS, LSF, Grid Engine, Kubernetes, and the Flux Framework, encompassing traditional batch schedulers, a cloud-native orchestration platform, and a graph-based scheduler. We examine the integration patterns, implementation requirements, and scheduler-specific considerations associated with each environment and compare QRMI with alternative approaches to quantum resource integration. We demonstrate that QRMI provides a portable and flexible abstraction layer that minimizes scheduler-specific modifications while enabling consistent access to heterogeneous quantum resources across both on-premises and cloud environments.

## 내 메모


