---
type: research-source
item_id: 1724
title: "LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks"
source: "arxiv"
published: "2026-08-03T09:32:21Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01964"
url: "https://arxiv.org/abs/2608.01964v1"
generated_by: codex-research-db
aliases:
  - "LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks

[원문 열기](https://arxiv.org/abs/2608.01964v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`AEX63UCX`)
- 발행일: 2026-08-03T09:32:21Z
- 저자: Ziyu Ma, Hailang Huang, Shun Zou, Yong Wang, Shidong Yang, Yiming Hu, Fei Wei, XiangXiang Chu
- 식별자: `arxiv:2608.01964`

## 요약·초록

Large language model (LLM) agents increasingly undertake long-horizon tasks that require sustained reasoning, tool use, and revision across many interdependent steps. However, existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making the state difficult to track and allowing incorrect self-assessments to propagate into later decisions. We reformulate long-horizon execution as a task-state management problem and propose LongHorizon-Harness, which maintains the task state explicitly outside execution and updates it only with facts independently verified from the environment. Its Manage-Execute-Audit(MEA) loop uses a manager to maintain the task state and determine the next subtask, a fresh-context executor to perform it, and a read-only auditor to verify the resulting environment state before the next round. A lightweight AgentAdapter supports interchangeable model and harness backends without modifying their native agent loops. LongHorizon-Harness improves Qwen~3.7-Plus from 51.8% to 80.7% on WeaveBench, from 69.7% to 77.2% on Terminal-Bench~2.1, and from 2.8% to 8.3% on OSWorld~2.0. It also raises Claude Opus~4.7 from 20.0% to 34.3% on an OSWorld2.0 subset, demonstrating consistent gains across models, harnesses, and interaction domains.

## 내 메모


