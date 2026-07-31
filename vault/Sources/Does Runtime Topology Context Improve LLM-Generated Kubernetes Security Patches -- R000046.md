---
type: research-source
item_id: 46
title: "Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?"
source: "arxiv"
published: "2026-07-28T17:12:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25995"
url: "https://arxiv.org/abs/2607.25995v1"
generated_by: codex-research-db
aliases:
  - "Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?"
topics:
  - "kubernetes"
---

# Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?

[원문 열기](https://arxiv.org/abs/2607.25995v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5489VZZV`)
- 발행일: 2026-07-28T17:12:12Z
- 저자: Farooq Shaikh
- 식별자: `arxiv:2607.25995`

## 요약·초록

Kubernetes is central to the cloud-native ecosystem, orchestrating containerised workloads. Recent work suggests that large language models (LLMs) can automate cluster security remediation, generating configuration patches from Kubernetes Security Posture Management (KSPM) findings without human authoring. Such systems, however, prompt the model with each finding in isolation from the live service call graph, assuming general hardening knowledge suffices. This assumption breaks down whenever a patch must preserve a runtime service dependency invisible to the model: an otherwise compliant fix then carries a destructive functional blast radius, crashing downstream callers or silently severing call edges across the cluster. Whether live cluster context improves patch correctness has not been measured under controlled conditions across multiple dependency classes. We introduce KuTIE (Kubernetes Topology Intelligence Engine), which builds a live cluster context from Istio call edges, Trivy KSPM findings, and the service-account bindings a workload reads, and conditions LLM patch generation on it. It is evaluated on VulnCare, a purpose-built 36-deployment, four-namespace healthcare cluster with 31 injectable findings across seven dependency classes, each labelled by topology dependence against cluster ground truth. Across 248 trials, topology context raises topology-dependent patch correctness from 11.1% to 78.0% ($Δ= 0.669$), a gap that holds for every model and for six of seven classes, from credential and network-policy ($Δ= 0.95$) to role-based access control ($Δ= 0.31$); a topology-independent control exhibits no such effect ($Δ= 0.0$), isolating the result from generic prompt enrichment. Supplying the live service-call graph and the service-account bindings it exposes thus improves remediation of topology-dependent findings well beyond scanner-only context.

## 내 메모


