---
type: research-source
item_id: 1174
title: "Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent Discovery, Identity, and Governance in Kubernetes"
source: "arxiv"
published: "2026-04-29T01:24:27Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.26997"
url: "https://arxiv.org/abs/2604.26997v1"
generated_by: codex-research-db
aliases:
  - "Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent Discovery, Identity, and Governance in Kubernetes"
topics:
  - "ai-agents"
  - "kubernetes"
---

# Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent Discovery, Identity, and Governance in Kubernetes

[원문 열기](https://arxiv.org/abs/2604.26997v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`G6KCFSE9`)
- 발행일: 2026-04-29T01:24:27Z
- 저자: Akshay Mittal, Elyson De La Cruz
- 식별자: `arxiv:2604.26997`

## 요약·초록

Autonomous AI agent ecosystems require stronger mechanisms for secure discovery, identity verification, capability attestation, and policy governance. Current deployments frequently lack (1) uniform agent discovery, (2) cryptographic agent authentication, (3) capability proofs that protect secrets, and (4) enforceable policy controls. This paper presents an implementation-oriented proof of concept for the Agent Name Service (ANS), a DNS-inspired trust layer for AI agent discovery and interoperability in Kubernetes, grounded in the ANS protocol specification~\cite{huang2025ans}. The implementation uses Decentralized Identifiers (DIDs), Verifiable Credentials (VCs), policy-as-code enforcement with Open Policy Agent (OPA), and Kubernetes-native integration patterns (CRDs, admission controls, service mesh integration). In a demo research environment (3-node cluster, 50-agent workflow simulation), we observe sub-10ms response in demonstrated service paths and full success for scripted demo deployment scenarios. We explicitly scope these findings as proof-of-concept evidence rather than production certification. We further provide a threat model, assumptions, and limitations to separate implemented evidence from protocol-defined and roadmap capabilities. The result is an evidence-grounded pathway from ANS protocol concepts to reproducible engineering practice for secure multi-agent systems.

## 내 메모


