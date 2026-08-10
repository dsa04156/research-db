---
type: research-source
item_id: 1777
title: "A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems"
source: "arxiv"
published: "2026-08-06T09:26:24Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.05791"
url: "https://arxiv.org/abs/2608.05791v1"
generated_by: codex-research-db
aliases:
  - "A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems"
topics:
  - "ai-agents"
---

# A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems

[원문 열기](https://arxiv.org/abs/2608.05791v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-06T09:26:24Z
- 저자: Zihan Xu, Haolin Tian, Hai Jiang
- 식별자: `arxiv:2608.05791`

## 요약·초록

Large language model (LLM)-driven multi-agent systems typically require multiple model invocations and complex coordination during inference, and their execution strategies directly affect system accuracy, latency, and computational cost. Parallel execution provides a means to improve inference-time efficiency. From the perspective of inference-time execution, this paper models parallelism in multi-agent systems as two distinct levels of decision processes: Replica Parallelism, which explores multiple complete solution paths at the task level, and Structural Parallelism, which enables concurrent execution within a single solution path through task decomposition. However, the roles of different forms of parallelism and their interrelationships still lack systematic study in terms of unified organization and coordination. We therefore propose TIPEX, a controllable execution framework that unifies these two levels of parallelism and coordinates their roles within the inference process under a unified execution semantics while supporting systematic combinations and analyses of different parallel strategies and parameter configurations. Systematic experiments on the GAIA benchmark demonstrate that inference-time parallelism can significantly improve accuracy and reduce end-to-end latency at the cost of increased token consumption. Further analysis shows that Replica and Structural Parallelism exhibit complementary effects across task complexities, with tasks of intermediate difficulty benefiting most from their coordination, while overly aggressive parallel strategies do not necessarily yield better performance.

## 내 메모


