---
type: research-source
item_id: 1627
title: "AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration"
source: "arxiv"
published: "2026-07-30T16:07:32Z"
first_seen: "2026-07-31"
review_status: "pending"
canonical_key: "arxiv:2607.28430"
url: "https://arxiv.org/abs/2607.28430v1"
generated_by: codex-research-db
aliases:
  - "AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration

[원문 열기](https://arxiv.org/abs/2607.28430v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-31|2026-07-31]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8GQVAEUW`)
- 발행일: 2026-07-30T16:07:32Z
- 저자: Xinxing Ren, Qianbo Zang, Ziyan Wang, Caelum Forder, Suman Deb, Peter Carroll, Zekun Guo
- 식별자: `arxiv:2607.28430`

## 요약·초록

Understanding large codebases is a long-horizon task for Large Language Model (LLM) agents: answering a single question can require building and running the software, tracing execution across files, and synthesizing evidence over tens of minutes. On SWE-Atlas QnA, a benchmark of long-horizon questions over production repositories, a single Claude Code agent (Opus 4.6) resolves only 32.3% of tasks. Dividing the work among agents with clean contexts mitigates this limitation. However, the subtasks of code comprehension are interdependent. One agent's findings can rewrite another's task, so agents must coordinate during execution, not only at phase boundaries. Existing multi-agent systems support such exchange only between phases, through staged handoffs or synchronized rounds. Communication and work remain mutually exclusive. A discovery made mid-execution cannot be shared until the next boundary. We present AgentRadio, an asynchronous message-passing layer that equips coding-agent harnesses with three primitives: threads, messages, and waiting for mentions. The last runs as a background task, surfacing teammates' messages without interrupting foreground work, so each agent remains passively aware of its peers and folds new findings into its ongoing task. Under a five-phase protocol of division of labor and negotiation, four agents organized by AgentRadio resolve 62.1% of tasks, 29.8 points above a single agent and above Claude Code with the newer Opus 4.8 (57.2%). Rubric-level analysis shows the gain growing with task difficulty, consistent with mid-course correction as the underlying mechanism. Our code is available at https://github.com/Coral-Protocol/AgentRadio.

## 내 메모


