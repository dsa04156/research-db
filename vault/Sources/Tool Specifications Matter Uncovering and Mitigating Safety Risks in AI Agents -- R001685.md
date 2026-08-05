---
type: research-source
item_id: 1685
title: "Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents"
source: "arxiv"
published: "2026-07-31T10:25:04Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2607.29254"
url: "https://arxiv.org/abs/2607.29254v1"
generated_by: codex-research-db
aliases:
  - "Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents"
topics:
  - "ai-agents"
---

# Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents

[원문 열기](https://arxiv.org/abs/2607.29254v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3UTQNZUM`)
- 발행일: 2026-07-31T10:25:04Z
- 저자: Minghui Pan, Jiayuxuan Yang, Yuanyuan Yuan, Yu Jiang, Zhenpeng Chen
- 식별자: `arxiv:2607.29254`

## 요약·초록

AI agents extend large language models (LLMs) with external tools, enabling them to perform complex tasks and translate model outputs into consequential real-world actions. Yet LLMs often become substantially less safe when deployed as agents, and the source of this degradation remains poorly understood. In this paper, we identify schema-formatted tool specifications as a primary source of agent safety degradation and show, through white-box representation analysis, that they weaken the model's internal refusal signals and contribute to unsafe tool execution. Building on this finding, we propose SafeKeep, an inference-time safeguard that decouples safety judgment from tool execution: it assesses requests using flattened textual tool specifications while retaining the original schema-formatted specifications for execution. Across two representative benchmarks and four LLMs, including both white-box and black-box models, SafeKeep increases the average refusal rate for harmful requests from 23.8% to 70.6% and reduces the average attack success rate under observation-level prompt injection from 25.6% to 2.5%. It also outperforms existing safeguards and preserves task-handling capability. We release the code and data at https://github.com/snowcatsmoking/SafeKeep .

## 내 메모


