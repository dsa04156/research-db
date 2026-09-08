---
type: research-source
item_id: 2613
title: "DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems"
source: "arxiv"
published: "2026-09-04T05:29:31Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.04749"
url: "https://arxiv.org/abs/2609.04749v1"
generated_by: codex-research-db
aliases:
  - "DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems"
topics:
  - "ai-agents"
---

# DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems

[원문 열기](https://arxiv.org/abs/2609.04749v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-04T05:29:31Z
- 저자: Zehao Wang, Lanjun Wang, Shilong Jin, Junjie Chen, Yanghua Xiao
- 식별자: `arxiv:2609.04749`

## 요약·초록

Large language model (LLM)-based multi-agent systems have experienced rapid growth in recent years. Despite their promise, such systems remain fragile, frequently exhibiting reasoning and coordination errors that can lead to system-level failures. Failure attribution in such systems relies on tracing natural language interactions among agents to identify the decisive error, which refers to the earliest action whose correction can reverse system failure. There are two key challenges: 1) Shallow attribution: Existing methods often capture only minor deviations, such as incomplete retrievals or formatting errors, which verification mechanisms can correct, while missing the decisive cause of system failure. 2) Contextual degradation: As the length of the system traces increases, the model's reasoning ability rapidly deteriorates. To address these challenges, we propose DCFA, a training-free framework for failure attribution. DCFA integrates a global module that constructs structured causal-inspired dependency graphs from system traces to identify the initial decisive error, and a local module that applies local counterfactual-inspired reasoning to refine causal-inspired attribution. Experiments on the Who&When benchmark across six LLMs show that DCFA improves step-level accuracy by up to 8.27% over state-of-the-art baselines.

## 내 메모


