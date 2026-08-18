---
type: research-source
item_id: 2012
title: "Accountability Without a Trusted Center: A Federated Governance Testbed for Multi-Principal AI Agents"
source: "openalex"
published: "2026-08-14"
first_seen: "2026-08-18"
review_status: "pending"
canonical_key: "doi:10.5281/zenodo.21930162"
url: "https://doi.org/10.5281/zenodo.21930162"
generated_by: codex-research-db
aliases:
  - "Accountability Without a Trusted Center: A Federated Governance Testbed for Multi-Principal AI Agents"
topics:
  - "ai-agents"
---

# Accountability Without a Trusted Center: A Federated Governance Testbed for Multi-Principal AI Agents

[원문 열기](https://doi.org/10.5281/zenodo.21930162)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-18|2026-08-18]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`GV5HHXTD`)
- 발행일: 2026-08-14
- 저자: Kenny Wang
- 식별자: `doi:10.5281/zenodo.21930162`

## 요약·초록

AI agents are moving from isolated assistants into populations of tool-using systems that delegate, persist, clone, and act across shared infrastructure — built and operated by different principals who do not trust one another and share no central controller. Safety-relevant questions in this setting are relational: which process acted, who authorized it, what delegation chain led to it, and which control boundary committed the external effect. Current agent infrastructure answers these questions poorly: agents are identified by session IDs, labels, and credentials that do not survive restart, cloning, copied memory, delegation, or compromise, and existing controls typically assume a single privileged deployer — an assumption that fails by construction in a multi-principal world, and one that independent work has begun to characterize directly: Yang et al. formalize multi-user agent interaction as a multi-principal decision problem and find frontier models unable to hold stable prioritization across conflicting principals. We present the design and pre-registered evaluation plan for an open testbed in which each principal runs its own governance instance and cross-principal interactions are mediated by verifiable attestations rather than a trusted center. The benchmark compares four control regimes — prompt-only, log-only, federated runtime governance, and a centralized-governor reference ceiling — so that the price of decentralization is measured rather than assumed. We report preliminary evidence from a live deployment: per-principal credential self-proof, cross-principal attestation, credential-theft impersonation refused at a closed resume surface, and forged lineage held provisional rather than trusted. All thresholds, kill conditions, and negative results are pre-registered; the testbed, scenarios, traces, and metric scripts will be released openly.

## 내 메모


