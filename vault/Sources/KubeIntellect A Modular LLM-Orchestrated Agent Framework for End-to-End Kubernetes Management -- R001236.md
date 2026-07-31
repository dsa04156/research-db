---
type: research-source
item_id: 1236
title: "KubeIntellect: A Modular LLM-Orchestrated Agent Framework for End-to-End Kubernetes Management"
source: "openalex"
published: "2026-06-27"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1007/s10723-026-09837-6"
url: "https://doi.org/10.1007/s10723-026-09837-6"
generated_by: codex-research-db
aliases:
  - "KubeIntellect: A Modular LLM-Orchestrated Agent Framework for End-to-End Kubernetes Management"
topics:
  - "kubernetes"
---

# KubeIntellect: A Modular LLM-Orchestrated Agent Framework for End-to-End Kubernetes Management

[원문 열기](https://doi.org/10.1007/s10723-026-09837-6)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`IP6R6ZN7`)
- 발행일: 2026-06-27
- 저자: Mohsen Seyedkazemi Ardebili, Andrea Bartolini
- 식별자: `doi:10.1007/s10723-026-09837-6`

## 요약·초록

Abstract Kubernetes has become the foundation of modern cloud-native infrastructure, yet its operational complexity remains a persistent barrier. Administrators must navigate a vast API surface, manage heterogeneous workloads, and coordinate tasks across disconnected tools—often requiring precise commands, declarative configuration files, and deep domain expertise. This paper presents KubeIntellect , a Large Language Model (LLM)-powered system for end-to-end Kubernetes management through natural language. KubeIntellect spans all major categories of Kubernetes operations—read, write, delete, exec, access control, and lifecycle management—through a supervisor-coordinated set of domain-specialized agents, with human-in-the-loop (HITL) confirmation on all mutating operations. Operations outside the static tool set are handled by the Code Generator Agent, which synthesizes, validates, and registers new Kubernetes tools at runtime. The Code Generator Agent executes synthesized tools in an in-process Python REPL rather than a separate process or container; process-level isolation between synthesized code and the host runtime is therefore not enforced, and a defense-in-depth model comprising static analysis, API-call validation, and mandatory human-in-the-loop review constitutes the primary mitigation. Migration to pod-level isolation is a planned hardening step. Evaluation on a live four-node Kubernetes cluster (170 pods across 18 namespaces) shows: a 75% pass rate (12/16; 95% CI: 51%–91%; mean rubric score 31.2/40) on a 16-scenario controlled fault-injection corpus scored on an 8-dimension LLM-judge rubric; a +25 percentage-point improvement over a tool-less GPT-4o baseline on the same scenarios (75% vs. 50%); a 93% query resolution rate (186/200) with an 81.8% synthesis success rate (63/77 novel tool requests) on a 200-query operational corpus; and end-to-end latency in the 7–10 s range at a mean API cost of $0.036/query for read-only workloads and $0.039/query overall. A reproducible demo environment is available on a public managed-Kubernetes service, with a local single-node option for readers without cloud access. These results demonstrate that domain-specific multi-agent orchestration, structured HITL confirmation, and runtime tool synthesis together yield substantially higher task completion than general-purpose LLM reasoning on Kubernetes operations.

## 내 메모


