---
type: research-source
item_id: 1107
title: "Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense"
source: "arxiv"
published: "2026-07-23T21:21:01Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.21824"
url: "https://arxiv.org/abs/2607.21824v1"
generated_by: codex-research-db
aliases:
  - "Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense"
topics:
  - "ai-agents"
---

# Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense

[원문 열기](https://arxiv.org/abs/2607.21824v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3MMNB7VB`)
- 발행일: 2026-07-23T21:21:01Z
- 저자: Yedidel Louck
- 식별자: `arxiv:2607.21824`

## 요약·초록

Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users' behalf, and they already handle real money. Their security has so far been studied almost entirely at the level of the AI model, through prompt injection and misalignment. We show that the more consequential risks lie one layer down, in the protocol between agents and commerce services. There, vulnerabilities are structural : exploitation is deterministic and ndependent of which model an agent runs, so no model improvement removes them. Across three leading platforms we identify 33 such vulnerabilities, each succeeding deterministically regardless of the deployed model, at a 100% attack-success rate (ASR) wherever live-measured. The same failure modes recur across independently built codebases, a systemic pattern rather than isolated bugs. Three of them chain into an end-to-end payment hijack. We contribute a taxonomy separating these structural attacks from model-dependent semantic ones. We also build two artifacts: AIP-Bench (Agent Interaction Protocol Benchmark), to our knowledge the first deterministic benchmark for agentic commerce security, and PCAT (Protocol-level Commerce Agent Trust), a platform-agnostic defense that drives the structural attack-success rate to zero for four of the five structural classes (RC-1, RC-2, RC-4, RC-5), with RC-3 (observable credential channels) reduced to warn-only, without modifying any platform. Agentic commerce must be secured at the protocol layer, not only the model.

## 내 메모


