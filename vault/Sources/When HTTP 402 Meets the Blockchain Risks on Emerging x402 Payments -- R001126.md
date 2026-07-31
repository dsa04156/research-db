---
type: research-source
item_id: 1126
title: "When HTTP 402 Meets the Blockchain: Risks on Emerging x402 Payments"
source: "arxiv"
published: "2026-07-21T19:45:13Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19545"
url: "https://arxiv.org/abs/2607.19545v1"
generated_by: codex-research-db
aliases:
  - "When HTTP 402 Meets the Blockchain: Risks on Emerging x402 Payments"
topics:
  - "ai-agents"
---

# When HTTP 402 Meets the Blockchain: Risks on Emerging x402 Payments

[원문 열기](https://arxiv.org/abs/2607.19545v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`E2HC2TFS`)
- 발행일: 2026-07-21T19:45:13Z
- 저자: Qinying Wang, Yong Yang, Yuan Chen, Shouling Ji, Mathias Payer
- 식별자: `arxiv:2607.19545`

## 요약·초록

x402 is an emerging payment protocol for Web APIs and autonomous AI agents. x402 extends HTTP 402 with a payment negotiation flow and delegates payment proof verification and on-chain settlement to third-party facilitators. As a result, facilitators serve as a shared payment infrastructure for many independent merchants. This centralizes trust and validation in one component, so a single flaw can affect many services. Despite rapid adoption by major vendors and economically meaningful mainnet activity, the security posture of real-world x402 deployments remains poorly characterized. We present the first systematic study of authorization correctness and execution safety in current facilitator-mediated x402 deployments in the wild, identifying eight security rules for facilitators as critical payment infrastructure. Based on our analysis of rule violations, we derive four new attack vectors, including Free Shopping, Asset Theft, Service Denial, and Gas Abuse. These attacks exploit weaknesses in the real-world facilitator and server implementations and cause severe harm, including direct financial loss to merchants, theft of facilitator-held assets, unbounded sponsor-paid gas/fees, and disruption of payment services. To assess the security of x402 deployments at scale, we propose a semi-automated black-box tool and apply it to 15 major x402 facilitators collectively used by over 60K sellers and 360K buyers. Alarmingly, we find violations in all evaluated facilitators. We responsibly disclosed our findings to the affected parties, who acknowledged the issues and adopted mitigations, including changes by Coinbase. Finally, we complement our controlled testing with an empirical measurement of over 119 million recent Base and Solana transactions, quantifying x402 adoption, facilitator centralization, and ecosystem-level risk indicators.

## 내 메모


