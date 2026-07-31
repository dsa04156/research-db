---
type: research-source
item_id: 435
title: "LibProf: A Python Profiler for Improving Cold Start Performance in Serverless Applications"
source: "openalex"
published: "2024-06-17"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2406.11734"
url: "http://arxiv.org/abs/2406.11734"
generated_by: codex-research-db
aliases:
  - "LibProf: A Python Profiler for Improving Cold Start Performance in Serverless Applications"
topics:
  - "cloud-infrastructure"
---

# LibProf: A Python Profiler for Improving Cold Start Performance in Serverless Applications

[원문 열기](http://arxiv.org/abs/2406.11734)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`EFN546B3`)
- 발행일: 2024-06-17
- 저자: Syed Salauddin Mohammad Tariq, Ali Al Zein, Soumya Sripad Vaidya, Arati Khanolkar, Probir Roy
- 식별자: `doi:10.48550/arxiv.2406.11734`

## 요약·초록

Serverless computing abstracts away server management, enabling automatic scaling and efficient resource utilization. However, cold-start latency remains a significant challenge, affecting end-to-end performance. Our preliminary study reveals that inefficient library initialization and usage are major contributors to this latency in Python-based serverless applications. We introduce LibProf, a Python profiler that uses dynamic program analysis to identify inefficient library initializations. LibProf collects library usage data through statistical sampling and call-path profiling, then generates a report to guide developers in addressing four types of inefficiency patterns. Systematic evaluations on 15 serverless applications demonstrate that LibProf effectively identifies inefficiencies. LibProf guided optimization results up to 2.26x speedup in cold-start execution time and 1.51x reduction in memory usage.

## 내 메모


