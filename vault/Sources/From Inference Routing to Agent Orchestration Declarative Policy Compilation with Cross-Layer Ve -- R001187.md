---
type: research-source
item_id: 1187
title: "From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification"
source: "arxiv"
published: "2026-03-28T15:04:31Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.27299"
url: "https://arxiv.org/abs/2603.27299v1"
generated_by: codex-research-db
aliases:
  - "From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification"
topics:
  - "kubernetes"
---

# From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification

[원문 열기](https://arxiv.org/abs/2603.27299v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MDAHHX76`)
- 발행일: 2026-03-28T15:04:31Z
- 저자: Huamin Chen, Xunzhuo Liu, Bowei He, Xue Liu
- 식별자: `arxiv:2603.27299`

## 요약·초록

The Semantic Router DSL is a non-Turing-complete policy language deployed in production for per-request LLM inference routing: content signals (embedding similarity, PII detection, jailbreak scoring) feed into weighted projections and priority-ordered decision trees that select a model, enforce privacy policies, and produce structured audit traces -- all from a single declarative source file. Prior work established conflict-free compilation for probabilistic predicates and positioned the DSL within the Workload-Router-Pool inference architecture. This paper extends the same language from stateless, per-request routing to multi-step agent workflows -- the full path from inference gateway to agent orchestration to infrastructure deployment. The DSL compiler emits verified decision nodes for orchestration frameworks (LangGraph, OpenClaw), Kubernetes artifacts (NetworkPolicy, Sandbox CRD, ConfigMap), YANG/NETCONF payloads, and protocol-boundary gates (MCP, A2A) -- all from the same source. Because the language is non-Turing-complete, the compiler guarantees exhaustive routing, conflict-free branching, referential integrity, and audit traces structurally coupled to the decision logic. Because signal definitions are shared across targets, a threshold change propagates from inference gateway to agent gate to infrastructure artifact in one compilation step -- eliminating cross-team coordination as the primary source of policy drift. We ground the approach in four pillars -- auditability, cost efficiency, verifiability, and tunability -- and identify the verification boundary at each layer.

## 내 메모


