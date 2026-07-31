---
type: research-source
item_id: 1106
title: "ToolGuardian: Declarative Security for AI Agent-Tool Interactions"
source: "arxiv"
published: "2026-07-23T21:53:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.21835"
url: "https://arxiv.org/abs/2607.21835v1"
generated_by: codex-research-db
aliases:
  - "ToolGuardian: Declarative Security for AI Agent-Tool Interactions"
topics:
  - "ai-agents"
---

# ToolGuardian: Declarative Security for AI Agent-Tool Interactions

[원문 열기](https://arxiv.org/abs/2607.21835v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3C92E2WE`)
- 발행일: 2026-07-23T21:53:34Z
- 저자: Arun Ravindran, Saurabh Deochake
- 식별자: `arxiv:2607.21835`

## 요약·초록

LLM agents increasingly rely on external tools, expanding capability while creating a new security boundary: third-party tools may appear benign at the interface level while embedding unsafe behavior in implementation. Existing defenses rely on weak metadata, collapse characterization and policy judgment into a single decision, or use heuristic/LLM enforcement that lacks deterministic, auditable reasoning over task context and multi-tool composition. This paper presents ToolGuardian, a policy-driven framework for securing agent-tool interactions through pre-admission vetting and task-aware runtime authorization. ToolGuardian uses progressive characterization to convert evidence into structured facts: descriptions capture declared intent, system-call traces expose coarse behavior, mock execution reveals observed effects, and source analysis identifies latent behavior. ToolGuardian's core contribution is an Answer Set Programming (ASP)-based declarative policy layer that reasons explicitly over capabilities, effects, task context, and composition. We compare ASP against heuristic and LLM-based policy realizations using identical inputs and output contracts. We evaluate ToolGuardian on 16 MCP-style tools, including 8 malicious variants derived from real open-source tools, and 20 runtime scenarios. For vetting, ASP reaches a deny-class F1 of 0.86 and 88% accuracy using description, syscall, and observed-effect evidence. For runtime authorization, fully specified realizations classify all scenarios correctly, while ablations show that removing compositional and conformance rules substantially degrades performance.

## 내 메모


