---
type: research-source
item_id: 2337
title: "Beyond Executable Models: The Pufibara Agent Harness and the Modelica Agent Workflow Benchmark for Physical System Modeling"
source: "arxiv"
published: "2026-08-24T11:50:07Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.23653"
url: "https://arxiv.org/abs/2608.23653v1"
generated_by: codex-research-db
aliases:
  - "Beyond Executable Models: The Pufibara Agent Harness and the Modelica Agent Workflow Benchmark for Physical System Modeling"
topics:
  - "self-evolving-harness"
  - "ai-agents"
---

# Beyond Executable Models: The Pufibara Agent Harness and the Modelica Agent Workflow Benchmark for Physical System Modeling

[원문 열기](https://arxiv.org/abs/2608.23653v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5FWRE4DV`)
- 발행일: 2026-08-24T11:50:07Z
- 저자: Zizhe Wang
- 식별자: `arxiv:2608.23653`

## 요약·초록

AI agents are increasingly used for simulation-driven engineering. Physical system modeling presents different requirements from general-purpose code generation in software engineering, because correctness depends not only on syntax and executability but also on physical consistency and scenario-dependent behavior. We study this challenge in Modelica, an equation-based modeling language in which a model may compile and simulate while still violating its intended physics or engineering requirements. Across successive revisions, an agent may lose track of requirements or rely on simulation evidence produced by an outdated candidate. To address this challenge, we present Pufibara, an agent harness that maintains persistent engineering state across revisions, associates execution and simulation evidence with the candidate that produced it, and makes submission an explicit agent action. To evaluate end-to-end Modelica agent workflows, we also propose a source-grounded method for constructing realistic and independently evaluable tasks. We use this method to build the 232-task Modelica Agent Workflow Benchmark, spanning Model Repair, Model Generation, and Model Tuning. Each submitted candidate is scored by a benchmark-owned evaluator outside the agent loop. We compare Pufibara with Claude Code as complete harnesses under two matched large language model (LLM) backends. With DeepSeek v4 Flash, Pufibara passes 202 tasks, compared with 185 for Claude Code. With Claude Sonnet 5, Pufibara passes 202 tasks, compared with 187 for Claude Code. Under the repository-reported token accounting, Pufibara records 76.4%-82.5% lower logical-token totals. Its sequential runtime is 6.1%-58.4% lower. These findings show that, even under matched LLM backends, complete agent harnesses can differ substantially in both task success and resource use for physical system modeling.

## 내 메모


