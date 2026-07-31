---
type: research-source
item_id: 1097
title: "Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture"
source: "arxiv"
published: "2026-07-24T16:08:03Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.22445"
url: "https://arxiv.org/abs/2607.22445v1"
generated_by: codex-research-db
aliases:
  - "Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture"
topics:
  - "ai-agents"
---

# Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture

[원문 열기](https://arxiv.org/abs/2607.22445v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`WU2H36ZC`)
- 발행일: 2026-07-24T16:08:03Z
- 저자: Halil Burak Noyan
- 식별자: `arxiv:2607.22445`

## 요약·초록

Enterprise AI agents are typically granted static credential sets at configuration time, holding every tool the role might need for every task they perform. This persistent over-privilege expands the attack surface. We argue that capability scoping must follow a dynamic least-privilege principle and be treated as a prevention mechanism before a detection one. A credential that does not exist in an agent's context cannot be misused regardless of the agent's reasoning or evasion sophistication. We outline a three-source architecture instantiating this principle: role-based ceilings, a task-context classifier, and policy-derived combination prohibitions creating a layered proactive defense against LLM agent misalignment and misuse cases. The architecture supports both enforcing and observe-only deployment; the latter records agent permission requests inconsistent with task context, producing a behavioral signal usable in misalignment research. As a first step toward evaluating this architecture, we contribute a synthetic dataset of 600 enterprise task prompts grounded in a multi-department company policy, labeled with minimum required permissions across a 15-permission tool-based taxonomy that maps directly to deployable credentials or enforceable guardrails. The dataset is constructed via a two-pass pipeline that separates prompt generation from permission labeling to avoid circularity, and is validated against a 60-record/688 decisions human-reviewed sample (Cohen's $κ= 0.917$ pre-review and $κ= 0.967$ post-review). Iterating between dataset and policy reduced ceiling violations from 46 to 3, a 93% reduction. This shows that synthetic prompt generation can drive policy refinement when the two are developed together. The dataset, environment specification, and generation pipeline are released to support evaluation of dynamic scoping mechanisms.

## 내 메모


