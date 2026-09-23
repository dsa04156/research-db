---
type: research-source
item_id: 3046
title: "Augmented Hypothesis Testing with Persona-Based LLM Simulations"
source: "arxiv"
published: "2026-09-21T14:11:34Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.24629"
url: "https://arxiv.org/abs/2609.24629v1"
generated_by: codex-research-db
aliases:
  - "Augmented Hypothesis Testing with Persona-Based LLM Simulations"
topics:
  - "ai-agents"
---

# Augmented Hypothesis Testing with Persona-Based LLM Simulations

[원문 열기](https://arxiv.org/abs/2609.24629v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T14:11:34Z
- 저자: Ziyad Benomar, Aymen Al Marjani, Paul Missault, Saab Mansour
- 식별자: `arxiv:2609.24629`

## 요약·초록

A/B testing requires large sample sizes, long timelines, and significant costs. When auxiliary predictions of experimental outcomes are available from machine learning models, uncertain prediction quality precludes replacing human experiments entirely, yet these predictions may still contain useful signal. We propose a principled framework for learning-augmented hypothesis testing that leverages predictions of unknown quality to reduce sample sizes while maintaining statistical validity. Predictions naturally vary in granularity, from coarse aggregate signals to fine-grained individual-level estimates, and our framework addresses both ends of this spectrum: (1) for population-level directional predictions, where only a binary signal on the treatment effect sign is available, we use an asymmetric test and prove consistency and robustness bounds within the learning-augmented algorithms paradigm; (2) for individual-level predictions, we introduce Generalized PPI++ (GPPI), extending Prediction-Powered Inference to handle nonlinear prediction errors through higher-dimensional transformations. Both methods benefit from accurate predictions while remaining robust to inaccurate or adversarial ones. We validate our framework using persona-based LLM simulations, where AI agents equipped with user personas predict individual behavior, as a natural prediction source spanning both granularity levels. Experiments on four real-world datasets demonstrate that our methods, combined with persona-based predictions, substantially reduce experimental costs while preserving rigorous statistical validity.

## 내 메모
