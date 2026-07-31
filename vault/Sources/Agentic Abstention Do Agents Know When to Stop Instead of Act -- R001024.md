---
type: research-source
item_id: 1024
title: "Agentic Abstention: Do Agents Know When to Stop Instead of Act?"
source: "arxiv"
published: "2026-06-27T04:49:37Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.28733"
url: "https://arxiv.org/abs/2606.28733v1"
generated_by: codex-research-db
aliases:
  - "Agentic Abstention: Do Agents Know When to Stop Instead of Act?"
topics:
  - "self-evolving-harness"
---

# Agentic Abstention: Do Agents Know When to Stop Instead of Act?

[원문 열기](https://arxiv.org/abs/2606.28733v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`I5JXQRFU`)
- 발행일: 2026-06-27T04:49:37Z
- 저자: Han Luo, Bingbing Wen, Lucy Lu Wang
- 식별자: `arxiv:2606.28733`

## 요약·초록

LLM agents are expected to act over multiple turns, using search, browsing interfaces, and terminal tools to complete user goals. Yet not every goal is well specified or achievable in the available environment. In such cases, a reliable agent should recognize that further interaction is unlikely to help and abstain from additional tool calls. We define Agentic Abstention, the problem of deciding when an agent should stop acting under uncertainty. Unlike standard LLM abstention, which is usually evaluated as a single-turn answer-or-abstain decision, agentic abstention is a sequential decision problem: an agent can answer, abstain, or gather more information at each turn, and the need to abstain may only become clear after interacting with the environment. We study this problem across web shopping, terminal environments, and question answering, evaluating 13 LLM-as-agent systems and 2 agent scaffolds on more than 28,000 tasks. Our results show that the main challenge is not only whether agents can abstain, but also when they abstain. Some agents never abstain when they should, while others do so only after many unnecessary interactions. This gap is especially large on tasks where the instruction appears feasible until the environment reveals otherwise (e.g., no valid result matches the instruction). We further find that model scale, reasoning, and agent scaffolding affect abstention in different ways, where larger or more capable models sometimes perform worse at timely abstention. Finally, we introduce CONVOLVE, a context engineering method for improving agentic abstention that distills full interaction trajectories into reusable stopping rules. On WebShop, CONVOLVE substantially improves timely abstention without updating model parameters, raising Llama-3.3-70B's timely recall rate from 26.7 to 57.4. Our dataset and code are available at https://lhannnn.github.io/agentic-abstention

## 내 메모


