---
type: research-source
item_id: 2447
title: "ATLAS: Dual-Horizon Diagnostic Evaluation for Industrial Tool-Use Agents"
source: "arxiv"
published: "2026-08-31T12:25:24Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.30685"
url: "https://arxiv.org/abs/2608.30685v1"
generated_by: codex-research-db
aliases:
  - "ATLAS: Dual-Horizon Diagnostic Evaluation for Industrial Tool-Use Agents"
topics:
  - "ai-agents"
---

# ATLAS: Dual-Horizon Diagnostic Evaluation for Industrial Tool-Use Agents

[원문 열기](https://arxiv.org/abs/2608.30685v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`74X3CTCJ`)
- 발행일: 2026-08-31T12:25:24Z
- 저자: Wei Chen, Peilun Zhou, Zhaoyu Hu, Jiajun Chai, Zhongni Hou, Yufei Zhang, Derong Xu, Guojun Yin, Wei Lin, Zhi Zheng, Tong Xu
- 식별자: `arxiv:2608.30685`

## 요약·초록

Large language model (LLM) agents are increasingly deployed in user-facing services that require iterative tool use under dynamic business conditions. Reliable evaluation is essential for sustained improvement: it must reveal capability deficiencies, inform priorities, and assess interventions. Yet industrial agent service unfolds both through the iterative trajectory of a current request and through continued user interaction. Final-outcome assessment can therefore obscure where deficiencies arise and whether later service remains aligned with context from earlier exchanges. We propose ATLAS, a dual-horizon diagnostic evaluation framework for industrial tool-use agents. At the request horizon, trajectory-wise diagnostic signals relate deficiencies to execution locations and capability concerns. At the interaction horizon, user-wise signals assess whether service remains responsive across continued interaction. Together, these views provide structured diagnostic evidence for analyzing execution deficiencies and sustained service behavior. ATLAS instantiates them as executable signals with explicit evidence scopes and decision boundaries. LLM judge interfaces are calibrated against high-confidence references from real business logs; when needed, their decision behavior is distilled into efficient diagnostic models for lower-latency, lower-cost evaluation. The resulting feedback supports policy optimization. We evaluate ATLAS on Meituan Xiaotuan production traffic. Offline experiments assess diagnostic-signal fidelity and replay-based policy improvement, while online A/B experiments show concurrent gains in user engagement, downstream business outcomes, and sampled human-audit quality.

## 내 메모


