---
type: research-source
item_id: 1113
title: "Toward cryptographically verifiable authorization for autonomous AI agents: A security hypothesis, preliminary formal model, and proof-of-concept implementation"
source: "arxiv"
published: "2026-07-23T13:55:02Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.21325"
url: "https://arxiv.org/abs/2607.21325v1"
generated_by: codex-research-db
aliases:
  - "Toward cryptographically verifiable authorization for autonomous AI agents: A security hypothesis, preliminary formal model, and proof-of-concept implementation"
topics:
  - "ai-agents"
---

# Toward cryptographically verifiable authorization for autonomous AI agents: A security hypothesis, preliminary formal model, and proof-of-concept implementation

[원문 열기](https://arxiv.org/abs/2607.21325v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`S7JGW8I3`)
- 발행일: 2026-07-23T13:55:02Z
- 저자: M. Llambí-Morillas, D. Fernández-Fernández
- 식별자: `arxiv:2607.21325`

## 요약·초록

Autonomous AI agents increasingly execute actions, invoke tools, and operate on protected resources with limited human oversight. Existing authentication and authorization mechanisms establish identity and delegate authority, but do not inherently provide cryptographic evidence that a concrete request issued by a specific agent satisfies the applicable policy in a specific execution context. This paper hypothesizes that agent authorization can be formalized as a cryptographically verifiable relation, denoted $R_{CVA}$, that jointly binds an agent principal, a concrete authorization request, an execution context, and the satisfaction of an applicable policy, while selectively preserving the confidentiality of private authorization attributes. We introduce a preliminary formal abstraction for Cryptographically Verifiable Agent Authorization (CVA), define a compact set of candidate security properties including authorization soundness, principal binding, request binding, policy binding, and replay resistance, and provide an executable zero-knowledge proof of concept that instantiates selected elements of the model over a Groth16 zk-SNARK construction. We further identify and formalize the structural separation among identity binding, authorization-request binding, and runtime execution binding as a central open problem in the design of secure agentic systems (a distinction {not explicitly addressed by} current agentic security frameworks) and present a falsifiable research agenda for its resolution.

## 내 메모


