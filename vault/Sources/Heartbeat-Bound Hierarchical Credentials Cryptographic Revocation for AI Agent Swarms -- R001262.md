---
type: research-source
item_id: 1262
title: "Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms"
source: "openalex"
published: "2026-05-20"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.20704"
url: "https://arxiv.org/abs/2605.20704"
generated_by: codex-research-db
aliases:
  - "Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms"
topics:
  - "ai-agents"
  - "kubernetes"
---

# Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms

[원문 열기](https://arxiv.org/abs/2605.20704)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`J3VMJWKK`)
- 발행일: 2026-05-20
- 저자: Saurabh Deochake
- 식별자: `arxiv:2605.20704`

## 요약·초록

Autonomous AI agents that spawn sub-agent swarms create a safety gap: existing credential revocation mechanisms, OAuth~2.0 introspection, OCSP, and W3C Status Lists, require network connectivity to a central authority, leaving ``zombie agents'' executing privileged operations for minutes to hours after operator shutdown. We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs. Verifiers enforce freshness using only a cached public key and local clock; no network round-trip is required. When heartbeat generation ceases, all descendant credentials become unusable within a deterministically bounded window $W_z \le W_{\max} + Δ_h + ε$, conditional on bounded clock skew and parent keys held in secure enclaves. Evaluation at the protocol layer and with real LLM-backed agent swarms (GPT-4o-mini) demonstrates a 90$\times$ reduction in the zombie window over OAuth~2.0, 0.26~ms full authentication in Rust, 18,000+ verifications per second under concurrent HTTP load, and stable per-verification latency from 10 to 10,000 agents. Real-agent experiments show 0.71\% end-to-end overhead on tool calls, zero post-revocation tool calls under prompt injection that bypasses application-layer guardrails, and cascading revocation across a 49-agent four-level hierarchy within the theoretical bound.

## 내 메모


