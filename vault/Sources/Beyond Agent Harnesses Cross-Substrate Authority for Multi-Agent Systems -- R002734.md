---
type: research-source
item_id: 2734
title: "Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems"
source: "arxiv"
published: "2026-09-08T09:11:53Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.08472"
url: "https://arxiv.org/abs/2609.08472v1"
generated_by: codex-research-db
aliases:
  - "Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2609.08472v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DP6S76R8`)
- 발행일: 2026-09-08T09:11:53Z
- 저자: Yang Li, Sergey Volkov, Hai Liu, Zongsi Xu, Xiyu Chen, Tuo Zhou, Dian Shao, Hao Sun, Ye Lu
- 식별자: `arxiv:2609.08472`

## 요약·초록

Agentic systems persist model-visible memory while mutating workspaces, while a runtime, registry, or approval service may hold authority state outside both. Identical final files can then require opposite safe actions. We call this the cross-substrate authority gap: decision- relevant authorization information resides outside the planner-visible workspace or memory state. Across two controlled mini-benchmark families, three experiments compare planner-observation augmentation with an execution-time authority check using real Git lineage, durably recorded agent execution attempts, deterministic oracles, and two model routes. Experiment 1 is a 128-cell controlled evidence ablation: authority-blind candidate evidence obtains 0/32 final semantic success, while raw receipts and a typed relation both obtain 32/32. The missing authority fact accounts for the gain; typed packaging provides no observed planning-accuracy gain over equal raw information. Experiment 2 uses 96 planning calls: workspace-visible evidence yields 12/16 unsafe publication decisions, and planning with the typed relation remains unreliable (15/32 first actions correct; 11/32 invalid or absent). Experiment 3 replays the same 32 fixed model-generated first-action intents with zero additional model calls; a deterministic execution guard prevents all six unsafe intents from becoming effects and permits all 12 valid authorized publish intents. These results position authority enforcement at the mutation boundary as the operational endpoint of memory governance.

## 내 메모


