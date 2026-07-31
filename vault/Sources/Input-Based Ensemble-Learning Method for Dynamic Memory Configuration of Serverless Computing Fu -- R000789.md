---
type: research-source
item_id: 789
title: "Input-Based Ensemble-Learning Method for Dynamic Memory Configuration of Serverless Computing Functions"
source: "arxiv"
published: "2024-11-12T00:03:11Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2411.07444"
url: "https://arxiv.org/abs/2411.07444v1"
generated_by: codex-research-db
aliases:
  - "Input-Based Ensemble-Learning Method for Dynamic Memory Configuration of Serverless Computing Functions"
topics:
  - "cloud-infrastructure"
---

# Input-Based Ensemble-Learning Method for Dynamic Memory Configuration of Serverless Computing Functions

[원문 열기](https://arxiv.org/abs/2411.07444v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`S8E5I3ST`)
- 발행일: 2024-11-12T00:03:11Z
- 저자: Siddharth Agarwal, Maria A. Rodriguez, Rajkumar Buyya
- 식별자: `arxiv:2411.07444`

## 요약·초록

In today's Function-as-a-Service offerings, a programmer is usually responsible for configuring function memory for its successful execution, which allocates proportional function resources such as CPU and network. However, right-sizing the function memory force developers to speculate performance and make ad-hoc configuration decisions. Recent research has highlighted that a function's input characteristics, such as input size, type and number of inputs, significantly impact its resource demand, run-time performance and costs with fluctuating workloads. This correlation further makes memory configuration a non-trivial task. On that account, an input-aware function memory allocator not only improves developer productivity by completely hiding resource-related decisions but also drives an opportunity to reduce resource wastage and offer a finer-grained cost-optimised pricing scheme. Therefore, we present MemFigLess, a serverless solution that estimates the memory requirement of a serverless function with input-awareness. The framework executes function profiling in an offline stage and trains a multi-output Random Forest Regression model on the collected metrics to invoke input-aware optimal configurations. We evaluate our work with the state-of-the-art approaches on AWS Lambda service to find that MemFigLess is able to capture the input-aware resource relationships and allocate upto 82% less resources and save up to 87% run-time costs.

## 내 메모


