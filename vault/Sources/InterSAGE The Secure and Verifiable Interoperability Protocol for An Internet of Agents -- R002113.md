---
type: research-source
item_id: 2113
title: "InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents"
source: "openalex"
published: "2026-08-13"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2608.13030"
url: "https://arxiv.org/abs/2608.13030"
generated_by: codex-research-db
aliases:
  - "InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents"
topics:
  - "kubernetes"
---

# InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents

[원문 열기](https://arxiv.org/abs/2608.13030)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-08-13
- 저자: Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Zhuotao Liu
- 식별자: `doi:10.48550/arxiv.2608.13030`

## 요약·초록

The emerging Internet of Agents enables LLM-powered agents to discover peers, invoke tools, and delegate tasks across organizational boundaries. Existing protocols increasingly define how agents exchange messages, but not how an agent proves its identity, authorization, advertised capabilities, or accountability after delegation. We present InterSAGE, a trust-native protocol suite that supplies this missing security substrate alongside, rather than in place of, communication protocols. InterSAGE comprises four layers: Persistent Identity, Discovery, Trust Negotiation, and Accountability. Its four core primitives are: (1) Agent Identity Cards that bind developer, code package, operator, and deployment context; (2) capability-aware discovery using DID-bound Verifiable Credential manifests; (3) trust negotiation combining monotonic capability attenuation with two-tier access control; and (4) kernel-mediated cryptographic audit trails that bind usage, delegation, and execution traces to agent identity without a consensus ledger. InterSAGE is designed to complement MCP, A2A, ANP, and AG-UI, allowing communication protocols to evolve independently while keeping trust semantics explicit, portable, and verifiable. We compare InterSAGE with more than 50 efforts spanning agent protocols, decentralized identity, OAuth/OIDC extensions, zero-trust governance, delegation, and audit architectures. We show that no prior architecture jointly enforces persistent identity, capability-aware discovery, trust negotiation, and accountability as a unified four-layer trust substrate for secure agent interoperability.

## 내 메모


