---
type: research-source
item_id: 2752
title: "Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course"
source: "arxiv"
published: "2026-09-08T14:53:43Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.08832"
url: "https://arxiv.org/abs/2609.08832v1"
generated_by: codex-research-db
aliases:
  - "Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course"
topics:
  - "self-evolving-harness"
  - "ai-agents"
---

# Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course

[원문 열기](https://arxiv.org/abs/2609.08832v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-08T14:53:43Z
- 저자: Evelyn Duesterwald, Benjamin Elder, Lilian Ngweta, Shashanka Ubaru, Malgorzata Zimon
- 식별자: `arxiv:2609.08832`

## 요약·초록

Large language model (LLM)-powered agents can be accurate on average yet unreliable in production, a discrepancy that has been observed but remains largely unaddressed. When given the same task five times, a ReAct agent on the AppWorld benchmark using GPT-4.1 succeeds in all five runs only 53% of the time, even though its per-run pass rate averages 77%. We call this 24-point shortfall the consistency gap, and we argue that addressing it is a precondition for trustworthy AI agent deployment. We present a self-evolving agent framework that reduces this gap by identifying unstable, low-consistency steps in agent trajectories and converting them into episodic memory the agent can draw on in future runs. At its core is a Consistency Analyzer that pinpoints where and why a trajectory is likely to flip across executions, and a Guideline Generator that converts the diagnosis into targeted guidelines, committed to memory and injected into future agent executions on similar tasks. On AppWorld with ReAct/GPT-4.1, our framework raises the fraction of tasks that succeed in all five runs by +16 points on same-task evaluation and +13 points on similar-task generalization.

## 내 메모


