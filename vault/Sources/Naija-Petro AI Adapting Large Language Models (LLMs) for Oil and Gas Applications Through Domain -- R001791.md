---
type: research-source
item_id: 1791
title: "Naija-Petro AI: Adapting Large Language Models (LLMs) for Oil and Gas Applications Through Domain-Specific Fine-Tuning"
source: "crossref"
published: "2026-08-10"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "doi:10.2118/234918-ms"
url: "https://doi.org/10.2118/234918-ms"
generated_by: codex-research-db
aliases:
  - "Naija-Petro AI: Adapting Large Language Models (LLMs) for Oil and Gas Applications Through Domain-Specific Fine-Tuning"
topics:
  - "edge-computing"
  - "kubernetes"
---

# Naija-Petro AI: Adapting Large Language Models (LLMs) for Oil and Gas Applications Through Domain-Specific Fine-Tuning

[원문 열기](https://doi.org/10.2118/234918-ms)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `crossref`
- 검토 상태: `pending`
- 발행일: 2026-08-10
- 저자: E. C. Ashinze
- 식별자: `doi:10.2118/234918-ms`

## 요약·초록

Abstract The global oil and gas industry has been increasingly turning to artificial intelligence to solve knowledge management challenges and domain-specific large language models (LLMs) catering to the petroleum engineering industry are still scarce. This issue is especially pronounced in Nigeria – the largest producer of crude oil in Africa – where the brain drain issue and data sovereignty concerns, coupled with the lack of infrastructure to access advanced AI tools, limit access to cutting-edge AI tools. This paper introduces Naija-Petro AI, an open-source domain-adapted large language model system which was fine-tuned on a tailored dataset of more than 33,000 instruction-response pairs in petroleum engineering by fine-tuning the Qwen3 model family (32B and 8B parameter variants). The training data was created through a two-stage pipeline consisting of web-scale scraping of academic corpus data from seven open access data sources (resulting in 66,905 text chunks of text with 20.5 million words in total) and synthetic instruction generation powered by Nvidia Data Designer. Fine-tuning was done using Quantized Low-Rank Adaptation (QLoRA) using the Unsloth framework and was able to reduce GPU memory usage to around 51GB for the 32B model and 28GB for the 8B model on Nvidia A100 hardware. A structured evaluation with 30 expert-level questions over six subdisciplines of petroleum engineering shows that the fine-tuned 32B model has an overall LLM-as-Judge score of 4.40 out of 5.0, which indicates a +0.77 improvement over the base Qwen3-32B model, with the greatest improvements in completeness (+1.04) and terminology precision (+0.70). The models are on Hugging Face under the Apache 2.0 licence and supports on premises deployments in line with the Data Protection Act, 2023 of Nigeria. The fine-tuned models are further integrated into a production retrieval augmented generation (RAG) assistant, publicly deployed at https://naija-petro.shinzii.tech, which combines hybrid semantic and full text retrieval over a self hosted vector store with dynamic live ingestion from authoritative Nigerian sources (NUPRC, NMDPRA, NNPC, NEITI and the Petroleum Industry Act), inline citations, and twelve deterministic engineering calculators, so that Nigeria specific answers stay current and verifiable while global fundamentals are carried in the model weights. This work gives a reproducible and resource-efficient way of fine-tuning open source LLMs to specialized engineering domains for resource constrained environments. Future work will include human expert evaluation by practising petroleum engineers, retrieval benchmarking of the deployed RAG layer with operator specific well data, and multilingual extension to support Nigerian Pidgin English and local technical terminology.

## 내 메모


