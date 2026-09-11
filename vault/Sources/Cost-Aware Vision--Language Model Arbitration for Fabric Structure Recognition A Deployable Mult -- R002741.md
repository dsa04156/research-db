---
type: research-source
item_id: 2741
title: "Cost-Aware Vision--Language Model Arbitration for Fabric Structure Recognition A Deployable Multi-Agent System"
source: "arxiv"
published: "2026-09-09T11:40:10Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.10065"
url: "https://arxiv.org/abs/2609.10065v1"
generated_by: codex-research-db
aliases:
  - "Cost-Aware Vision--Language Model Arbitration for Fabric Structure Recognition A Deployable Multi-Agent System"
topics:
  - "ai-agents"
---

# Cost-Aware Vision--Language Model Arbitration for Fabric Structure Recognition A Deployable Multi-Agent System

[원문 열기](https://arxiv.org/abs/2609.10065v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GXNWZ3G9`)
- 발행일: 2026-09-09T11:40:10Z
- 저자: Chenwei Wang, Haochen Li, Shuk Ching Tang, Misbah Iqbal, Carman Lee, Elif Ozden-Yenigun
- 식별자: `arxiv:2609.10065`

## 요약·초록

Recognizing a fabric's structure is a prerequisite for translating textile-specific material information into structured digital form for downstream supply-chain systems. Pure CNN classifiers are cost-efficient but fail on visually ambiguous categories; vision--language models (VLMs) generalize more broadly but cost much more per image and are unstable on specialist domains. We present a multi-agent system in which a CNN cascade handles the easy majority and a VLM is invoked only as a selective arbiter, constrained to a top-3 taxonomy-consistent choice. The fabric taxonomy performs as a constraint for the whole recognition process to increase the accuracy and reduce the VLM calls. Meanwhile, the CNN cascade is distilled to a small parameter size to reduce the inference time and meet the needs of practical deployment. On a newly curated 14-class benchmark, a flat ConvNeXt-Tiny baseline reaches $90.45\,\%$ top-1 and $76.9\,\%$ on the four hardest classes; \method's hierarchical cascade reaches $93.94\,\%$ top-1 and $94.50\,\%$ hard ($+17.6$\,pp). Tightening the VLM trigger from $60\,\%$ to $<\!10\,\%$ cuts API cost by ${\sim}90\,\%$ with no measurable accuracy loss. CPU inference is $\le\!93$\,ms without a VLM call ($9.3$\,ms distilled). Each prediction carries a machine-readable reasoning record, offered as an entry point for future supply-chain documentation.

## 내 메모


