---
type: research-source
item_id: 1220
title: "Efficient Multi-Model Orchestration for Self-Hosted Large Language Models"
source: "arxiv"
published: "2025-12-26T22:42:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.22402"
url: "https://arxiv.org/abs/2512.22402v1"
generated_by: codex-research-db
aliases:
  - "Efficient Multi-Model Orchestration for Self-Hosted Large Language Models"
topics:
  - "kubernetes"
---

# Efficient Multi-Model Orchestration for Self-Hosted Large Language Models

[원문 열기](https://arxiv.org/abs/2512.22402v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5P5QD9UC`)
- 발행일: 2025-12-26T22:42:40Z
- 저자: Bhanu Prakash Vangala, Tanu Malik
- 식별자: `arxiv:2512.22402`

## 요약·초록

Self-hosting large language models (LLMs) is increasingly appealing for organizations seeking privacy, cost control, and customization. Yet deploying and maintaining in-house models poses challenges in GPU utilization, workload routing, and reliability. We introduce Pick and Spin, a practical framework that makes self-hosted LLM orchestration scalable and economical. Built on Kubernetes, it integrates a unified Helm-based deployment system, adaptive scale-to-zero automation, and a hybrid routing module that balances cost, latency, and accuracy using both keyword heuristics and a lightweight DistilBERT classifier. We evaluate four models, Llama-3 (90B), Gemma-3 (27B), Qwen-3 (235B), and DeepSeek-R1 (685B) across eight public benchmark datasets, with five inference strategies, and two routing variants encompassing 31,019 prompts and 163,720 inference runs. Pick and Spin achieves up to 21.6% higher success rates, 30% lower latency, and 33% lower GPU cost per query compared with static deployments of the same models.

## 내 메모


