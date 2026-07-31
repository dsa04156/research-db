---
type: research-source
item_id: 1181
title: "Context Kubernetes: Declarative Orchestration of Enterprise Knowledge for Agentic AI Systems"
source: "arxiv"
published: "2026-04-13T15:35:55Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.11623"
url: "https://arxiv.org/abs/2604.11623v3"
generated_by: codex-research-db
aliases:
  - "Context Kubernetes: Declarative Orchestration of Enterprise Knowledge for Agentic AI Systems"
topics:
  - "kubernetes"
  - "ai-agents"
---

# Context Kubernetes: Declarative Orchestration of Enterprise Knowledge for Agentic AI Systems

[원문 열기](https://arxiv.org/abs/2604.11623v3)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`D4RG265N`)
- 발행일: 2026-04-13T15:35:55Z
- 저자: Charafeddine Mouzouni
- 식별자: `arxiv:2604.11623`

## 요약·초록

We introduce Context Kubernetes, an architecture for orchestrating enterprise knowledge in agentic AI systems, with a prototype implementation and eight experiments. The core observation is that delivering the right knowledge, to the right agent, with the right permissions, at the right freshness -- across an entire organization -- is structurally analogous to the container orchestration problem Kubernetes solved a decade ago. We formalize six core abstractions, a YAML-based declarative manifest for knowledge-architecture-as-code, a reconciliation loop, and a three-tier agent permission model where agent authority is always a strict subset of human authority. On synthetic seed data, we compare four governance baselines of increasing strength: ungoverned RAG, ACL-filtered retrieval, RBAC-aware routing, and the full architecture. Each layer contributes a different capability: ACL filtering eliminates cross-domain leaks, intent routing reduces noise by 19 percentage points, and only the three-tier model blocks all five tested attack scenarios -- the one attack RBAC misses is an agent sending confidential pricing via email, which RBAC cannot distinguish from ordinary email. TLA+ model-checking verifies safety properties across 4.6 million reachable states with zero violations. A survey of four major platforms (Microsoft, Salesforce, AWS, Google) documents that none architecturally isolates agent approval channels. We identify four properties that make context orchestration harder than container orchestration, and argue these make the solution more valuable.

## 내 메모


