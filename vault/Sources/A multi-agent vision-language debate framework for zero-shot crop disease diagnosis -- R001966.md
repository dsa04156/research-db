---
type: research-source
item_id: 1966
title: "A multi-agent vision-language debate framework for zero-shot crop disease diagnosis"
source: "openalex"
published: "2026-08-11"
first_seen: "2026-08-13"
review_status: "pending"
canonical_key: "doi:10.3389/fpls.2026.1890016"
url: "https://doi.org/10.3389/fpls.2026.1890016"
generated_by: codex-research-db
aliases:
  - "A multi-agent vision-language debate framework for zero-shot crop disease diagnosis"
topics:
  - "ai-agents"
---

# A multi-agent vision-language debate framework for zero-shot crop disease diagnosis

[원문 열기](https://doi.org/10.3389/fpls.2026.1890016)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-13|2026-08-13]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`FJCQKTRE`)
- 발행일: 2026-08-11
- 저자: Mustafa Al Juboori, Zeeshan Abbas, Zayed Al Aghbari, Farman Ullah, Mobeen ur Rehman
- 식별자: `doi:10.3389/fpls.2026.1890016`

## 요약·초록

Accurate crop disease diagnosis is critical for agricultural productivity and food security, yet existing deep learning systems often struggle to generalize across visually similar diseases and varying environmental conditions. Recent Vision-Language Models (VLMs) have demonstrated promising zero-shot reasoning capabilities; however, most agricultural diagnostic systems still rely on isolated single-model predictions without collaborative reasoning or consensus mechanisms. In this work, we propose VIDA+PANDA, a multi-agent Vision-Language framework for zero-shot crop disease diagnosis. The framework consists of two stages: VIDA, where multiple VLM agents independently analyze crop leaf images to establish baseline performance, and the Peer-Anchored Named Deliberation Architecture (PANDA), which introduces a structured multi-round debate among a selected group of high-performing and architecturally diverse agents. During deliberation, agents exchange reasoning, critique peer predictions, and revise decisions through evidence-grounded discussion, while an anti-sycophancy mechanism discourages unsupported consensus shifts. Final predictions are generated through performance-weighted consensus voting. Experiments are conducted on the CDDM benchmark using seven heterogeneous VLMs from four independent providers, including two open-source models, under a fully zero-shot setting. A non-participant GPT-5 model serves as an independent judge to assess the final diagnostic predictions. Beyond conventional accuracy, the framework introduces three semantic measures: Semantic Label Similarity (SLS), which measures how semantically close a predicted crop-disease pair is to the ground truth and captures partial correctness overlooked by exact-match evaluation; Reasoning Specificity (RS), which measures how concretely an agent’s explanation references visual evidence such as lesion color, shape, texture, or margins; and Inter-Agent Reasoning Convergence (IRC), which measures the extent to which agents rely on similar visual evidence, capturing epistemic alignment independently of label correctness. Experimental results show that collaborative multiagent deliberation improves individual diagnostic performance and semantic alignment, with the largest gains observed among weaker participating agents. The findings also reveal important relationships between predictive accuracy, persuasive influence, and consensus formation in VLM-based agricultural diagnosis.

## 내 메모


