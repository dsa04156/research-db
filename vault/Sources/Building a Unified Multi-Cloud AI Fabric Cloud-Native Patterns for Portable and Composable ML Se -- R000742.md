---
type: research-source
item_id: 742
title: "Building a Unified Multi-Cloud AI Fabric: Cloud-Native Patterns for Portable and Composable ML Services"
source: "openalex"
published: "2025-07-16"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.37082/ijirmps.v13.i4.232861"
url: "https://doi.org/10.37082/ijirmps.v13.i4.232861"
generated_by: codex-research-db
aliases:
  - "Building a Unified Multi-Cloud AI Fabric: Cloud-Native Patterns for Portable and Composable ML Services"
topics:
  - "kubernetes"
---

# Building a Unified Multi-Cloud AI Fabric: Cloud-Native Patterns for Portable and Composable ML Services

[원문 열기](https://doi.org/10.37082/ijirmps.v13.i4.232861)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`8XQDTDIG`)
- 발행일: 2025-07-16
- 저자: Santosh Pashikanti
- 식별자: `doi:10.37082/ijirmps.v13.i4.232861`

## 요약·초록

Enterprises that build AI/ML platforms at scale are increasingly forced into multi-cloud strategies—sometimes by design (best-of-breed services, regulatory constraints, M&amp;A), sometimes by accident. While Kubernetes and containers promise workload portability, the reality for AI/ML workloads is far more complex: data gravity, GPU scarcity, heterogeneous managed AI services, and fragmented MLOps tooling make “build once, run anywhere” difficult to realize in practice. In this paper, I propose a unified multi-cloud AI fabric: an opinionated but vendor-neutral architecture that standardizes how AI/ML workloads are built, deployed, and operated across AWS, Google Cloud, and Microsoft Azure using containers, Kubernetes, and cloud-native abstraction layers. Building on recent work in cloud-native AI, Kubernetes-based ML platforms (e.g., Kubeflow), and distributed serving frameworks, the fabric defines a layered architecture with consistent patterns for portable training pipelines, composable inference graphs, cross-cloud traffic steering, and policy-driven governance. CNCF+1 I describe system requirements and design principles for such a fabric, including portability, composability, resilience, data locality, GPU efficiency, and security. I then present a reference architecture spanning EKS, AKS, and GKE, and walk through an implementation and case study of a global recommendation and fraud-detection platform. An evaluation compares this fabric against a single-cloud baseline along dimensions of migration effort, time-to-deploy, failover RTO, and cost utilization. Finally, I discuss trade-offs and outline future directions, including AI-native control planes, WASM-based runtimes, and cross-cloud vector databases. My goal is to provide a practical blueprint that other architects and ML platform teams can adapt, rather than yet another theoretical multi-cloud diagram that never survives contact with production.

## 내 메모


