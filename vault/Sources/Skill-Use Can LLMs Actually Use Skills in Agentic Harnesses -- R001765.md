---
type: research-source
item_id: 1765
title: "Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?"
source: "arxiv"
published: "2026-08-05T13:29:16Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.04828"
url: "https://arxiv.org/abs/2608.04828v1"
generated_by: codex-research-db
aliases:
  - "Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?"
topics:
  - "self-evolving-harness"
---

# Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?

[원문 열기](https://arxiv.org/abs/2608.04828v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KNZKVHMT`)
- 발행일: 2026-08-05T13:29:16Z
- 저자: Jinyi Han, Yuanjian Xu, Ying Liao, Xinyi Wang, Zishang Jiang, Zixiang Di, Fanyang Lu, Zhichao Hu, Yanghua Xiao
- 식별자: `arxiv:2608.04828`

## 요약·초록

Large language model (LLM) agents increasingly rely on skills, structured documents that specify when to act, which procedure to follow, and which tools are allowed. Existing evaluations mostly judge the quality of a skill or its contribution to task success, leaving unexamined whether an agent can recognize a relevant skill and apply it on its own. We introduce Skill-Use, a benchmark that evaluates skill use under progressive disclosure, where an agent sees only a skill's name and short description and must retrieve the full procedure before following it. Skill-Use separates three facets of skill use. Trigger measures whether the agent invokes the relevant skill, Compliance measures how faithfully it follows the prescribed procedure, and Boundary measures whether it avoids forbidden operations. A Skill-Use (SU) score combines the three and credits execution only after the skill is triggered. Skill-Use pairs 79 real skills with 177 executable tasks across nine domains, each grounded in real files, run in an isolated Docker sandbox, and scored by a trajectory-based rubric. Evaluating eight LLMs under two agent harnesses, we find that reliable skill use remains out of reach, as the strongest configuration reaches an SU of only 0.613. Triggering and procedural compliance fail as independent bottlenecks, and both scores and model rankings shift with the harness, so skill use behaves as a capability conditioned on the harness rather than a fixed property of the model.

## 내 메모


