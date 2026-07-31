---
type: research-source
item_id: 1058
title: "Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks"
source: "arxiv"
published: "2026-07-28T15:39:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25877"
url: "https://arxiv.org/abs/2607.25877v1"
generated_by: codex-research-db
aliases:
  - "Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks"
topics:
  - "ai-agents"
---

# Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks

[원문 열기](https://arxiv.org/abs/2607.25877v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RZR733EF`)
- 발행일: 2026-07-28T15:39:43Z
- 저자: Bart Custers, Koorosh Aslansefat
- 식별자: `arxiv:2607.25877`

## 요약·초록

This paper investigates how multi-agent systems (MAS)-based on large language models (LLMs) can support actuarial risk modelling, with a particular focus on uncertainty quantification. Actuarial workflows represent a high-stakes decision-support setting where unreliable outputs may lead to incorrect risk assessment, unfair pricing, and regulatory non-compliance. To address uncertainty introduced by the probabilistic nature of LLMs and dependencies between agents, a multi-agent framework is proposed in which specialised agents perform data preparation, modelling, review, and explanation tasks under a central hub. The main contribution is a novel approach to uncertainty propagation using token-level log-probabilities and a Bayesian Network. Importantly, log probabilities are not treated as direct probabilities of correctness or task success. Instead, length-normalised log-probability summaries are transformed into calibrated task-level confidence estimates before incorporation into the Bayesian Network. Results show that the framework reproduces baseline actuarial performance while providing additional insight into workflow stability and runtime uncertainty propagation.

## 내 메모


