---
type: research-source
item_id: 2941
title: "Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems"
source: "arxiv"
published: "2026-09-19T11:06:14Z"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "arxiv:2609.22949"
url: "https://arxiv.org/abs/2609.22949v1"
generated_by: codex-research-db
aliases:
  - "Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems"
topics:
  - "ai-agents"
---

# Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2609.22949v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-19T11:06:14Z
- 저자: Rudrendu Kumar Paul, Sourav Nandy
- 식별자: `arxiv:2609.22949`

## 요약·초록

Existing prompt injection research focuses on single-model chatbot scenarios, where an attacker manipulates one LLM through crafted input. Multi-agent systems amplify this threat through three mechanisms absent from single-model settings: inter-agent message passing creates injection channels invisible to perimeter defenses, shared tool access enables privilege escalation across agent boundaries, and trust propagation allows a compromised agent to influence upstream orchestrators. We construct a threat model enumerating 14 attack vectors across four categories: direct injection via user input (3 vectors), indirect injection via tool outputs (4 vectors), inter-agent injection via message passing (4 vectors), and cascading injection through orchestrator manipulation (3 vectors). Testing all 14 vectors against a 6-agent production-representative system, we find that 67% of agents are vulnerable to at least one scope violation even with system-prompt-level guardrails, and indirect injection via tool outputs succeeds in 43% of attempts. Four architectural defenses reduce overall injection success from 31.2% to 4.2%: message signing with provenance tracking (inter-agent injection down 91%), input/output sanitization at agent boundaries (indirect injection down 78%), privilege-scoped tool access per agent role (privilege escalation eliminated entirely), and anomaly detection on inter-agent communication patterns (84% of cascading attempts caught).

## 내 메모
