---
type: research-source
item_id: 1356
title: "Benchmarking Local Language Models for Social Robots using Edge Devices"
source: "arxiv"
published: "2026-05-04T19:49:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.03111"
url: "https://arxiv.org/abs/2605.03111v1"
generated_by: codex-research-db
aliases:
  - "Benchmarking Local Language Models for Social Robots using Edge Devices"
topics:
  - "edge-computing"
---

# Benchmarking Local Language Models for Social Robots using Edge Devices

[원문 열기](https://arxiv.org/abs/2605.03111v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`PH85HA65`)
- 발행일: 2026-05-04T19:49:22Z
- 저자: Dorian Lamouille, Matevž B. Zorec, Farnaz Baksh, Karl Kruusamäe
- 식별자: `arxiv:2605.03111`

## 요약·초록

Social-educational robots designed for socially interactive pedagogical support, such as the Robot Study Companion (RSC), rely on responsive, privacy-preserving interaction despite severely limited compute. However, there is a gap in systematic benchmarking of language models for edge computing in pedagogical applications. This paper benchmarks 25 open-source language models for local deployment on edge hardware. We evaluate each model across three dimensions: inference efficiency (tokens per second, energy consumption), general knowledge (a six-category MMLU subset), and teaching effectiveness (LLM-rated pedagogical quality), validated against five independent human raters using the Raspberry Pi(RPi)4 as the primary platform, with additional comparisons on the RPi5 and a laptop GPU. Results reveal pronounced trade-offs: throughput and energy efficiency vary by over an order of magnitude across models, MMLU accuracy ranges from near-random to 57.2%, and teaching effectiveness does not correlate monotonically with either metric. Among the evaluated models, Granite4 Tiny Hybrid (7B) achieves a strong overall balance, reaching 2.5 tokens per second, 0.90 tokens per joule, and 54.6% MMLU accuracy; high MMLU accuracy does not appear necessary for strong teaching scores. Human validation on four representative models preserved the automated rank ordering (Pearson r = 0.967, n = 4). Based on these findings, we propose a three-tier local inference architecture for the RSC that balances responsiveness and accuracy on resource-constrained hardware.

## 내 메모


