---
type: research-source
item_id: 2913
title: "Agentic Autoscaling through Worker-Pool Orchestration for LLM-driven Text Classification in Cloud Computing Environments"
source: "openalex"
published: "2026-09-14"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.14898"
url: "https://arxiv.org/abs/2609.14898"
generated_by: codex-research-db
aliases:
  - "Agentic Autoscaling through Worker-Pool Orchestration for LLM-driven Text Classification in Cloud Computing Environments"
topics:
  - "cloud-infrastructure"
---

# Agentic Autoscaling through Worker-Pool Orchestration for LLM-driven Text Classification in Cloud Computing Environments

[원문 열기](https://arxiv.org/abs/2609.14898)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`5S9P9V79`)
- 발행일: 2026-09-14
- 저자: Bablu Kumar, Anshul Verma, Rajkumar Buyya
- 식별자: `arxiv:2609.14898`

## 요약·초록

The growing adoption of large language model (LLM)-based systems for large-scale text processing has created a critical need for dynamic autoscaling to manage high-latency, bursty, and computationally intensive workloads. This paper proposes an agentic autoscaling framework through worker-pool orchestration for LLM-driven text classification. The framework integrates a priority task queue, a dynamic pool of agent workers, a real-time metrics collector, and an application-layer autoscaler. Its classifier-agnostic design supports both zero-shot and fine-tuned language models without modifying the autoscaling logic. The framework is evaluated using Autoscaling+BART and Autoscaling+DeBERTa against static allocation and standalone RoBERTa and DistilBERT baselines. On the AG News dataset, Autoscaling+BART achieves 84.5% accuracy, while Autoscaling+DeBERTa improves it to 90.5%. On the SMS Spam Collection dataset, Autoscaling+DeBERTa achieves 99.5% accuracy, whereas Autoscaling+BART attains 84.5% accuracy with lower execution time. Overall, the proposed framework consistently outperforms the baseline approaches in resource efficiency while maintaining high classification performance, demonstrating that elastic worker-pool orchestration provides an effective and cost-efficient solution for scalable LLM-driven text classification in cloud environments.

## 내 메모


