---
type: research-source
item_id: 2459
title: "Zero-Knowledge Predicate Proofs Between AI Agents: A Measured, Cross-Protocol Gateway and the Source-Integrity Gap"
source: "arxiv"
published: "2026-08-30T23:16:17Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.30083"
url: "https://arxiv.org/abs/2608.30083v1"
generated_by: codex-research-db
aliases:
  - "Zero-Knowledge Predicate Proofs Between AI Agents: A Measured, Cross-Protocol Gateway and the Source-Integrity Gap"
topics:
  - "ai-agents"
  - "kubernetes"
---

# Zero-Knowledge Predicate Proofs Between AI Agents: A Measured, Cross-Protocol Gateway and the Source-Integrity Gap

[원문 열기](https://arxiv.org/abs/2608.30083v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`35VI8G56`)
- 발행일: 2026-08-30T23:16:17Z
- 저자: Ashok Subbabhatta Gopalakrishna
- 식별자: `arxiv:2608.30083`

## 요약·초록

Multi-agent AI platforms move quickly from staging to production, but the way agents establish trust remains rudimentary: an agent either transmits raw data to a peer or accepts that peer's natural-language self-report that a value complies with policy. The first over-shares; the second is unverifiable and is exactly the channel prompt injection attacks. Prevailing responses emphasise identity, visibility, and post-hoc detection, and recent proposals for cryptographically enforced agent policy have been evaluated in simulation rather than execution. We take provable data minimisation between agents from proposal to running system. In our Zero-Knowledge Proof Gateway, agents exchange proofs of governance-defined predicates over private data rather than the data itself, so exposure is prevented by design rather than detected afterwards; because no interoperability protocol can carry such a proof, we propose a slot and implement it on both MCP and Agent2Agent from one endpoint. A 32-bit threshold predicate proves in 6.2 ms and verifies in 1.0 ms with a 608-byte Bulletproofs proof on one commodity vCPU; eleven adversarial experiments and nineteen protocol checks pass; and the system is deployed to Kubernetes with empirically verified network isolation. Our case study proves a retail client order is within its limit without revealing the amount, instantiating the GDPR data-minimisation principle as an enforced technical measure of the kind EU law now names explicitly. We then address the limitation no comparable work resolves: a predicate proof binds a statement to a committed value, never to the system of record. We give a construction fusing an enclave attestation with the proof in both directions, so verifying one artifact certifies jointly that the predicate holds and that the value was read by a specific measured binary, and test it against a mock authority.

## 내 메모


