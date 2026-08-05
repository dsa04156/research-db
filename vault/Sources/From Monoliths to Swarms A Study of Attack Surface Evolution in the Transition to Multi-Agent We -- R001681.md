---
type: research-source
item_id: 1681
title: "From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems"
source: "arxiv"
published: "2026-07-31T18:27:12Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.00202"
url: "https://arxiv.org/abs/2608.00202v1"
generated_by: codex-research-db
aliases:
  - "From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems"
topics:
  - "ai-agents"
---

# From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems

[원문 열기](https://arxiv.org/abs/2608.00202v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`U29H9JWU`)
- 발행일: 2026-07-31T18:27:12Z
- 저자: Yashaswi Malla, Sandra Siby
- 식별자: `arxiv:2608.00202`

## 요약·초록

Large Language Model (LLM)-based web agents are increasingly evolving from single-agent systems (SAS) to multi-agent systems (MAS). While MAS can lead to improved task performance by decomposing complex tasks across specialized sub-agents, such role decomposition introduces new structural attack surfaces that are absent in SAS. This expanded attack surface remains poorly understood and inadequately categorized. To address this, we propose a taxonomy to categorize attack vectors specific to web-based MAS, accounting for vulnerabilities introduced or amplified by the involvement of multiple agents. We further present a test-bed WebMASLab to analyze web agent security against a fully external, web-only adversary. To isolate the effect of architecture, we keep the user task, tool surface, and browser substrate fixed, and compare single- and multi-agent setups. We evaluate three adversarial scenarios, across three conditions (baseline, prompt-hardened, and reasoning-enabled), including a novel MAS-specific Telephone Loop attack that exploits cross-agent delegation to create cyclical task loops. The attack is inert against SAS but compromises MAS when powered by three of the four frontier models evaluated (Claude Sonnet 4.5, GPT-5.2, GPT-5.4), averaging 80% across them at baseline. Only the fourth model, Claude Sonnet 4.6, resists the attack with a 92% detection rate. For the rest, the detection is 0% at baseline, reaching 33% with prompt-hardening for one model. We also show that obvious defenses do not generalize; prompt-hardening collapses one model's ASR from 100% to 8% while providing only modest reduction to the others. Our findings demonstrate that the transition from single- to multi-agent web systems changes the security landscape. Role specialization may not only lead to performance optimization but also introduce new architectural risks that require further study and defenses.

## 내 메모


