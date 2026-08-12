---
type: research-source
item_id: 1943
title: "A Systematic Taxonomy of Large Language Model Inference Optimization: Bridging Model-Level and API-Layer Latency Reduction Strategies"
source: "openalex"
published: "2026-08-10"
first_seen: "2026-08-12"
review_status: "pending"
canonical_key: "doi:10.6025/pca/2026/15/2/82-103"
url: "https://doi.org/10.6025/pca/2026/15/2/82-103"
generated_by: codex-research-db
aliases:
  - "A Systematic Taxonomy of Large Language Model Inference Optimization: Bridging Model-Level and API-Layer Latency Reduction Strategies"
topics:
  - "ai-agents"
---

# A Systematic Taxonomy of Large Language Model Inference Optimization: Bridging Model-Level and API-Layer Latency Reduction Strategies

[원문 열기](https://doi.org/10.6025/pca/2026/15/2/82-103)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-12|2026-08-12]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`FAEGN6QE`)
- 발행일: 2026-08-10
- 저자: Yao-Liang Chung
- 식별자: `doi:10.6025/pca/2026/15/2/82-103`

## 요약·초록

The deployment of Large Language Models (LLMs) as autonomous agents in next generation infrastructures, such as Agentic AI-Native 6G networks, introduces severe latency, memory, and operational cost bottlenecks.Existing optimization approaches frequently treat model compression and system orchestration in isolation, failing to adequately address the multidimensional constraints of modern production environments.This paper presents a systematic, multi criteria taxonomy of LLM inference optimization, bridging granular model level compression techniques with macro level API-layer orchestration strategies.We conduct a rigorous comparative analysis of post training quantization algorithms specifically highlighting activationaware methods like AWQ alongside GPTQ and GGUF evaluating their trade offs across memory efficiency, inference throughput, and predictive quality.Our findings reveal that deployment efficiency is not solely dictated by numerical precision but is fundamentally a co-design problem requiring optimized hardware kernels and adaptive, importance aware parameter protection.Furthermore, we demonstrate that systemlevel interventions, such as intelligent model routing, prompt caching, and deterministic decoupling, yield immediate latency reductions without altering underlying model weights.Ultimately, this study provides a comprehensive, scenario based decision framework for matching specific quantization algorithms and APIlayer strategies to distinct deployment environments, ranging from high throughput GPU serving to resourceconstrained edge devices and safety critical autonomous systems.By unifying these perspectives, we establish a foundational guide for practitioners aiming to build reliable, high performance inference pipelines that ensure scalable and economically sustainable AI integration across diverse industrial domains.

## 내 메모


