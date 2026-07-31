---
type: research-source
item_id: 995
title: "Implicit Fine-tuning via Context Engineering: A Curriculum Learning Framework for Multimodal Entity Alignment"
source: "arxiv"
published: "2026-07-12T02:01:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3770855.3817732"
url: "https://arxiv.org/abs/2607.10532v1"
generated_by: codex-research-db
aliases:
  - "Implicit Fine-tuning via Context Engineering: A Curriculum Learning Framework for Multimodal Entity Alignment"
topics:
  - "self-evolving-harness"
---

# Implicit Fine-tuning via Context Engineering: A Curriculum Learning Framework for Multimodal Entity Alignment

[원문 열기](https://arxiv.org/abs/2607.10532v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZXS3IMV7`)
- 발행일: 2026-07-12T02:01:40Z
- 저자: Yunpeng Hong, Chenyang Bu, Di Wu, Yi He, Xindong Wu
- 식별자: `doi:10.1145/3770855.3817732`

## 요약·초록

Multimodal Entity Alignment (MMEA) aims to identify equivalent entities across different modalities. While existing methods enhance MMEA performance through black-box context engineering strategies, their reliance on LLM parameter capacity and lack of theoretical interpretability remain unresolved. To this end, we first theoretically validate the mathematical equivalence between context engineering and model fine-tuning in MMEA tasks, demonstrating that prompt components simulate contrastive learning-based sequential fine-tuning in MMEA. Building on this foundation, we then propose PTFEA, a curriculum-learning-inspired framework that translates fine-tuning strategies into interpretable context engineering. Specifically, adaptive difficulty modulation dynamically adjusts information injection stages using confidence thresholds, establishing mathematical equivalence between curriculum learning weights and context sample selection; and three-stage progressive inference incorporates entity information from simple to complex cases, mirroring the gradient descent process in fine-tuning. Experiments on five public datasets demonstrate that PTFEA consistently outperforms strong baselines. In particular, on the ICWIKI dataset, PTFEA narrows the H@1 gap between Qwen2.5-72B and 14B to 0.6%. Moreover, compared with the representative context-engineering-based MMEA method MM-ChatAlign, PTFEA reduces the runtime of Qwen2.5-72B from 21 hours to 1 hour and lowers token consumption from 2200-3000 to 200-400, achieving over 80% reduction on the ICWIKI dataset. This work provides the first theoretical framework unifying context engineering and fine-tuning in MMEA, paving the way for future research that seeks to translate additional fine-tuning strategies into context engineering paradigms. Our code is available at https://github.com/DMiC-Lab-HFUT/PTFEA.

## 내 메모


