---
type: research-source
item_id: 2755
title: "AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems"
source: "arxiv"
published: "2026-09-08T11:07:04Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.08572"
url: "https://arxiv.org/abs/2609.08572v1"
generated_by: codex-research-db
aliases:
  - "AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems"
topics:
  - "ai-agents"
---

# AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems

[원문 열기](https://arxiv.org/abs/2609.08572v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZR5XIKI2`)
- 발행일: 2026-09-08T11:07:04Z
- 저자: Jaewon Chu, Jinwoo Seo, Jaewon Cho, Jeehye Na, Yunyang Xiong, Youngdae Kim, Hyunwoo J. Kim
- 식별자: `arxiv:2609.08572`

## 요약·초록

Large language model (LLM)-based multi-agent systems (MAS) achieve strong performance by employing specialized multiple agents, yet their performance depends on the prompt design of each agent. For MAS prompt optimization, textual gradient methods that guide prompt updates using natural-language feedback have emerged as a leading paradigm. In this paper, we identify limitations in two stages of existing textual gradient approaches: gradient extraction and gradient aggregation. In gradient extraction, previous works select a target prompt without verifying whether modifying it resolves the failure, and derive gradients without agent-level supervision over the corresponding agent's intermediate output. In gradient aggregation, individual gradients are randomly grouped and concatenated, often mixing unrelated failure modes and producing prompts that fail to generalize. To address these limitations, we propose \textbf{AgentGrad}, a prompt optimization framework for multi-agent systems based on sequential intervention and semantic textual gradient abstraction. For each failure, sequential intervention modifies the behavior of one agent at a time to identify the target agent whose modification resolves the failure. The modified output of the target agent then serves as agent-level supervision for extracting a fine-grained gradient. Semantic textual gradient abstraction clusters semantically similar gradients to prevent mixing unrelated failure modes, and abstracts each cluster into a generalized gradient that captures the shared corrective pattern. Experimental results show that AgentGrad achieves state-of-the-art performance across five MAS benchmarks and reduces wall-clock optimization time by $2.5\times$ on average compared to the next-fastest baseline.

## 내 메모


