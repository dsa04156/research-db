---
type: research-source
item_id: 1022
title: "From Naive RAG to Deep Agentic Retrieval: An Evolving Context Engineering Pipeline for Regulatory Compliance"
source: "arxiv"
published: "2026-06-28T14:11:03Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.24791"
url: "https://arxiv.org/abs/2607.24791v1"
generated_by: codex-research-db
aliases:
  - "From Naive RAG to Deep Agentic Retrieval: An Evolving Context Engineering Pipeline for Regulatory Compliance"
topics:
  - "self-evolving-harness"
---

# From Naive RAG to Deep Agentic Retrieval: An Evolving Context Engineering Pipeline for Regulatory Compliance

[원문 열기](https://arxiv.org/abs/2607.24791v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JWQPDAHK`)
- 발행일: 2026-06-28T14:11:03Z
- 저자: Mishca de Costa, Muhammad Saleh Anwar, Dave Mercier, Issam Hammad
- 식별자: `arxiv:2607.24791`

## 요약·초록

Retrieval-augmented generation (RAG) is the dominant paradigm for applying large language models (LLMs) to enterprise document corpora, yet naive implementations encounter hard limits as corpus scale and query complexity grow. This paper traces the evolution of a production retrieval pipeline at Ontario Power Generation (OPG) for regulatory compliance and rate case analysis under Ontario Energy Board (OEB) reporting requirements. We examine successive stages: naive RAG, hybrid retrieval with re-ranking, agentic function-calling retrieval, and a deep multi-agent architecture with code-based tool synthesis and explicit planning, and identify the failure modes and tradeoffs that motivated each transition. We formalize the mature architecture as Progressive Evidence Acquisition with Cost-Aware Escalation (PEA-CAE): begin with low-cost, high-precision retrieval and escalate to full-document reads only when the expected evidence gain justifies latency and cost. Our findings show that context engineering is a more tractable and economically viable path than domain-specific fine-tuning for large, evolving regulatory corpora. More broadly, the progression toward deep agentic retrieval mirrors classical information retrieval ideas, introducing adaptive query reformulation, progressive document discovery, and hierarchical subagent summarization as practical system primitives. Operational traces further support the search-based nature of modern retrieval systems, where iterative evidence acquisition and adaptive planning increasingly replace single-pass retrieval as the foundation for enterprise-scale question answering.

## 내 메모


