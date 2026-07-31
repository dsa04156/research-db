---
type: research-source
item_id: 16
title: "StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents"
source: "arxiv"
published: "2026-07-24T14:17:03Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.22798"
url: "https://arxiv.org/abs/2607.22798v1"
generated_by: codex-research-db
aliases:
  - "StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents"
topics:
  - "self-evolving-harness"
---

# StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents

[원문 열기](https://arxiv.org/abs/2607.22798v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`EBA7UAW2`)
- 발행일: 2026-07-24T14:17:03Z
- 저자: Yan Yang, Xiangru Jian, Ziyang Luo, Zirui Zhao, Yutong Dai, Ziji Shi, Hanshu Yan, Jun Hao Liew, Silvio Savarese, Junnan Li
- 식별자: `arxiv:2607.22798`

## 요약·초록

Computer-use agents are usually improved by strengthening perception: better models for reading a screenshot and choosing where to click. Yet a screenshot is only a lossy rendering of the underlying program state, e.g., the files, application backends, and DOM that hold the task data. Different states can produce the same pixels, while code can inspect and modify that state directly. StateAct is a code-first, multi-agent harness built around this distinction. Its main agent works directly with program state by using code, while a dedicated GUI subagent handles screenshot-and-click interaction on the few subgoals that need it, just 28 of 108 tasks and 1.1% of main-agent steps. The same direct access to program state also supports verification: an independent finish gate double-checks the saved result for structural failures, e.g., output that is missing, unsaved, or written to the wrong path. To stay on track over hundreds of steps, the main agent hands subgoals to fresh subagents, keeping its own context focused. On OSWorld 2.0, StateAct lifts Claude Opus 4.8 from 20.6% to 26.9% on binary success, and from 54.8% to 61.6% on partial success, at ~ 9x lower cost per task than the same model driven by screenshots alone; a code-only variant with no GUI subagent reaches only 45.9% partial, below that screenshot-based baseline's 54.8%. In general, grounding action, verification, and memory in state, what we call state-grounding, shifts the main bottleneck from perception toward reasoning: failures depend more on what the agent thinks than on what it sees.

## 내 메모


