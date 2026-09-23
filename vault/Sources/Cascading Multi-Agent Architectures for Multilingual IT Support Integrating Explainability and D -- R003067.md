---
type: research-source
item_id: 3067
title: "Cascading Multi-Agent Architectures for Multilingual IT Support: Integrating Explainability and Dynamic Workload Optimisation"
source: "openalex"
published: "2026-09-20"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "doi:10.68104/ijasit.v1.i3.42"
url: "https://doi.org/10.68104/ijasit.v1.i3.42"
generated_by: codex-research-db
aliases:
  - "Cascading Multi-Agent Architectures for Multilingual IT Support: Integrating Explainability and Dynamic Workload Optimisation"
topics:
  - "ai-agents"
---

# Cascading Multi-Agent Architectures for Multilingual IT Support: Integrating Explainability and Dynamic Workload Optimisation

[원문 열기](https://doi.org/10.68104/ijasit.v1.i3.42)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-09-20
- 저자: Syed Muhammad Umar Afnan, Annette Nayana Nellyet
- 식별자: `doi:10.68104/ijasit.v1.i3.42`

## 요약·초록

Modern IT helpdesks increasingly need to support multiple languages while staying transparent and resistant to hallucination, yet most deployed chatbots still rely on single-model architectures that struggle on both counts. This paper presents NexaServe v2, a four-tier cascading multi-agent IT helpdesk system combining retrieval-based response, LLM validation, LLM fallback, and human escalation, alongside a hybrid multilingual classification pipeline, confidence-gated routing, and workload-aware ticket assignment. The system is evaluated on a public Kaggle multilingual helpdesk dataset (n = 28,587 tickets), 89 logged chatbot interactions, and operational logs collected during development and testing. Fine-tuning mBERT on combined English-German data reached 89.84% category accuracy, while an English-trained classical model applied to translated German priority tickets dropped from 77.70% to 57.23% accuracy, a much steeper decline than the equivalent category-classification result. The chatbot cascade maintained a low factual hallucination rate (2.7% on a 75-message held-out batch) despite rejecting 93.3-100% of retrieval-layer responses as insufficiently confident. An AI-based workload supervisor, despite generating fluent and specific justifications for its decisions, performed no better than a simple deterministic heuristic and violated its own explicit numerical rule in every recorded overload flag. These results demonstrate that a transparent, near-zero-marginal-cost multilingual helpdesk is achievable using local LLMs for classification and cascaded response generation, while showing that LLM-based supervision does not reliably outperform deterministic alternatives for tasks with strict, checkable correctness criteria.

## 내 메모
