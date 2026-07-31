---
type: research-source
item_id: 1253
title: "Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems"
source: "openalex"
published: "2026-06-01"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.01508"
url: "https://arxiv.org/abs/2606.01508"
generated_by: codex-research-db
aliases:
  - "Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems"
topics:
  - "kubernetes"
  - "ai-agents"
---

# Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems

[원문 열기](https://arxiv.org/abs/2606.01508)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`RQXUCQTA`)
- 발행일: 2026-06-01
- 저자: Ankur Sharma, Deep Shah
- 식별자: `arxiv:2606.01508`

## 요약·초록

Traditional operating systems were designed around deterministic programs, explicit control flow, and human initiated workflows. Their core abstractions processes, threads, system calls, files, and permissions assume bounded behavior and predictable interaction patterns. Agentic AI systems introduce a different execution model: long-lived, goal-directed entities that reason probabilistically, invoke tools dynamically, and adapt behavior based on feedback. While agents can be implemented as user-space applications today, their execution characteristics stress OS boundaries in scheduling, memory and state management, security, observability, and governance. This paper introduces the concept of an Agent Operating System (AOS), a systems architecture that integrates an agentic control plane into existing operating systems or, in some models, subsumes selected OS responsibilities over time. We provide a precise definition of an AOS, explicit assumptions and non-goals, and a structured decomposition of AOS responsibilities into schedulers, context and memory management, tool and capability registries, policy and trust enforcement, and observability and audit. We analyze limitations of classical OS abstractions for agent workloads, propose integration models from user-space runtimes to distributed control planes, and map AOS concepts onto Linux and Windows primitives. We present security and safety implications, including agent specific threat models, and define evaluation criteria that emphasize deterministic enforcement, auditability, and operator comprehensibility. The objective is not to replace operating systems wholesale, but to establish a rigorous systems foundation for agentic computation that remains controllable, accountable, and secure at scale.

## 내 메모


