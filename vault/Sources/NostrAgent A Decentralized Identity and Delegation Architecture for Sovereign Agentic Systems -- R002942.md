---
type: research-source
item_id: 2942
title: "NostrAgent: A Decentralized Identity and Delegation Architecture for Sovereign Agentic Systems"
source: "arxiv"
published: "2026-09-19T10:49:54Z"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "arxiv:2609.22944"
url: "https://arxiv.org/abs/2609.22944v1"
generated_by: codex-research-db
aliases:
  - "NostrAgent: A Decentralized Identity and Delegation Architecture for Sovereign Agentic Systems"
topics:
  - "ai-agents"
---

# NostrAgent: A Decentralized Identity and Delegation Architecture for Sovereign Agentic Systems

[원문 열기](https://arxiv.org/abs/2609.22944v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`E83UVVXS`)
- 발행일: 2026-09-19T10:49:54Z
- 저자: Oliver Aleksander Larsen, Mahyar Tourchi Moghaddam
- 식별자: `arxiv:2609.22944`

## 요약·초록

Autonomous AI agents increasingly act across organizational boundaries on behalf of human operators: they invoke third-party services, delegate subtasks to other agents, and pay for metered resources. Deploying such agents safely requires five capabilities that today live in separate systems: persistent identity, scoped delegation, peer trust, discovery, and payment. Existing approaches root these in centralized authorities or cover only subsets, so authority, trust, and payment fracture exactly where autonomy needs continuity: when a key rotates or a delegation must be revoked. We present NostrAgent, a decentralized architecture that unifies all five over Nostr relays using three custom event kinds: Kind 38100 identity declarations authenticated by BIP340 Schnorr signatures with pre-rotation commitments, Kind 38101 scoped delegation chains whose every hop verifiably narrows granted capabilities, and Kind 38102 peer attestations forming a Sybil-deterrent trust graph, with Lightning HTTP 402 (L402) binding payment to agent identity. Identity remains operator-sovereign without any registration authority; relays are substitutable transport rather than a trust root; and every authorization decision is replayable offline from signed events. We evaluate a Python prototype with a mixed-method design: ATAM quality analysis with a two-round mini-Delphi panel, STRIDE threat modeling across three trust boundaries, eleven benchmarks with non-parametric statistics, and 19 failure modes. Results show sub-millisecond offline verification, linear delegation-chain scaling, and Lightning-settled L402 at 157 ms median on regtest. 17 of 19 failure modes pass empirically, one is bounded analytically, and one is disclosed as an architectural limitation. NostrAgent demonstrates an auditable prototype substrate for trustworthy agentic systems without centralized trust roots.

## 내 메모
