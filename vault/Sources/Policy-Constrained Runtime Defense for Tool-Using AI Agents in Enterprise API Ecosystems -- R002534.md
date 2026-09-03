---
type: research-source
item_id: 2534
title: "Policy-Constrained Runtime Defense for Tool-Using AI Agents in Enterprise API Ecosystems"
source: "openalex"
published: "2026-09-01"
first_seen: "2026-09-03"
review_status: "pending"
canonical_key: "doi:10.63412/ss28se48"
url: "https://doi.org/10.63412/ss28se48"
generated_by: codex-research-db
aliases:
  - "Policy-Constrained Runtime Defense for Tool-Using AI Agents in Enterprise API Ecosystems"
topics:
  - "ai-agents"
---

# Policy-Constrained Runtime Defense for Tool-Using AI Agents in Enterprise API Ecosystems

[원문 열기](https://doi.org/10.63412/ss28se48)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-03|2026-09-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`4F7TQFZV`)
- 발행일: 2026-09-01
- 저자: Swapneswar Ray
- 식별자: `doi:10.63412/ss28se48`

## 요약·초록

Tool-using AI agents can invoke internal APIs, retrieve documents, update records, and coordinate enterprise workflows. These capabilities create a runtime security problem: an agent may select an unauthorized tool, hallucinate an endpoint, follow malicious instructions embedded in retrieved context, rely on poisoned memory, retry unsafe operations, or submit a schema-valid but policy-violating payload. This paper presents a policy-constrained runtime enforcement framework that intercepts each proposed action before execution and classifies it as allow, deny, or escalate. We implement a deterministic trace-driven simulator with five service domains, six user roles, six threat classes, benign and adversarial tasks, and four defense configurations. The evaluation isolates enforcement effectiveness by replaying identical seeded action traces across all configurations. Across 8,000 controlled workflow executions, the framework reduces adversarial attack success from 100.0% for an unconstrained agent, 72.2% for prompt-only controls, and 18.5% for static gateway rules to 0.2%. It achieves a 99.9% overall safe-outcome rate, 100.0% benign safe completion under simulated reviewer approval, a 4.8% benign false-positive rate, and a 24.9 ms median enforcement latency. Ablation results show that registry validation, authorization, retry governance, and intent checking directly reduce attack success. Payload inspection addresses schema-valid semantic misuse, while context-integrity and escalation controls provide defense-in-depth and operational-governance benefits. The framework provides a structured basis for controlled evaluation of policy-constrained runtime enforcement across tool-using enterprise agents.

## 내 메모


