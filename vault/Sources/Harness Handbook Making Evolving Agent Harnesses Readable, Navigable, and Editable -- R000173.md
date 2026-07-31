---
type: research-source
item_id: 173
title: "Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable"
source: "arxiv"
published: "2026-07-23"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.13285"
url: "https://arxiv.org/abs/2607.13285"
generated_by: codex-research-db
aliases:
  - "Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable"
topics:
  - "self-evolving-harness"
  - "ai-agents"
---

# Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable

[원문 열기](https://arxiv.org/abs/2607.13285)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KKHA4MW9`)
- 발행일: 2026-07-23
- 저자: Ruhan Wang, Yucheng Shi, Zongxia Li, Zhongzhi Li, Yue Yu, Junyao Yang, Kishan Panaganti, Haitao Mi, Dongruo Zhou, Leoweiliang
- 식별자: `arxiv:2607.13285`

## 요약·초록

The capability of a modern AI agent depends not only on its foundation model but also on its harness, which constructs prompts, manages state, invokes tools, and coordinates execution. As models, APIs, environments, and requirements evolve, the harness must be continually modified. Before such a change can be made, a developer or coding agent must identify all code locations that implement the target behavior. This is difficult because production harnesses are large, tightly coupled, and behaviorally distributed, while modification requests describe what the system should do and repositories are organized by files and modules. Code search, repository indexing, and long-context processing ease inspection, but still leave this behavior-to-code mapping to be recovered by hand. Behavior localization is therefore a central bottleneck in harness evolution. We introduce the Harness Handbook, a behavior-centric representation synthesized automatically from a harness codebase via static analysis and LLM-assisted structuring, linking each behavior to its corresponding source. We also introduce Behavior-Guided Progressive Disclosure (BGPD), which guides agents from high-level behaviors to relevant implementation details and verifies candidate locations against the current source. On diverse modification requests from two open-source harnesses, Handbook-Assisted planning improves behavior localization and edit-plan quality while using fewer planner tokens, with the largest gains on scattered sites, rarely executed paths, and cross-module interactions. Evolving complex agentic systems thus depends not only on generating edits, but also on determining where those edits should be made.

## 내 메모


