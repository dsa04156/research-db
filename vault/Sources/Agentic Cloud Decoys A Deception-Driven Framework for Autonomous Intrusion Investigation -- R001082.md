---
type: research-source
item_id: 1082
title: "Agentic Cloud Decoys: A Deception-Driven Framework for Autonomous Intrusion Investigation"
source: "arxiv"
published: "2026-07-27T05:05:57Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.24006"
url: "https://arxiv.org/abs/2607.24006v1"
generated_by: codex-research-db
aliases:
  - "Agentic Cloud Decoys: A Deception-Driven Framework for Autonomous Intrusion Investigation"
topics:
  - "kubernetes"
  - "ai-agents"
---

# Agentic Cloud Decoys: A Deception-Driven Framework for Autonomous Intrusion Investigation

[원문 열기](https://arxiv.org/abs/2607.24006v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3N8RAIVB`)
- 발행일: 2026-07-27T05:05:57Z
- 저자: Mohan Manivannan, Dalal Alharthi
- 식별자: `arxiv:2607.24006`

## 요약·초록

Cloud telemetry arrives at a scale that, paradoxically, makes intrusion understanding harder rather than easier. Attackers operate through legitimate identity, federated session tokens, and cloud native APIs indistinguishable from routine administration, and analysts spend an incident reconstructing context the logs already contain. We present Cloud Decoy AI Agent, a framework pairing a high fidelity cloud decoy with an autonomous language model agent that compresses the path from suspicious activity to an analyst ready report. Connecting a decoy to an agent is not a wiring exercise. The unit of investigation is the session rather than the event, and the session key is obscured by the identity layering federated credentials introduce. The agent's evidence horizon must be bounded, since an agent free to query full control plane history inherits the cost and false positive profile deception was meant to remove. And cloud telemetry is partly adversary authored, since object keys and user agent strings are attacker chosen values providers record verbatim, which makes any log to prompt path an indirect prompt injection channel that a decoy widens rather than narrows. We address the first two with a session aggregation operator over a pivot tuple drawn only from provider derived fields, and with dynamic prompt generation, a two stage prompt assembly enforcing a grounding invariant by carrying only fields the agent observed. We identify the third as an unaddressed exposure in this class of system, specify the mitigation it requires, and note our prototype does not implement it. Across ten controlled AWS S3 scenarios, nine were reconstructed completely, no report contained an assertion untraceable to an observed artifact, and latency was four to five minutes. We also state what this evaluation does not establish and name the comparisons that would settle it.

## 내 메모


