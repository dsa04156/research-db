---
type: research-source
item_id: 383
title: "SPES: Towards Optimizing Performance-Resource Trade-Off for Serverless Functions"
source: "arxiv"
published: "2024-03-26T10:28:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2403.17574"
url: "https://arxiv.org/abs/2403.17574v2"
generated_by: codex-research-db
aliases:
  - "SPES: Towards Optimizing Performance-Resource Trade-Off for Serverless Functions"
topics:
  - "cloud-infrastructure"
---

# SPES: Towards Optimizing Performance-Resource Trade-Off for Serverless Functions

[원문 열기](https://arxiv.org/abs/2403.17574v2)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZTSFIB3I`)
- 발행일: 2024-03-26T10:28:41Z
- 저자: Cheryl Lee, Zhouruixing Zhu, Tianyi Yang, Yintong Huo, Yuxin Su, Pinjia He, Michael R. Lyu
- 식별자: `arxiv:2403.17574`

## 요약·초록

As an emerging cloud computing deployment paradigm, serverless computing is gaining traction due to its efficiency and ability to harness on-demand cloud resources. However, a significant hurdle remains in the form of the cold start problem, causing latency when launching new function instances from scratch. Existing solutions tend to use over-simplistic strategies for function pre-loading/unloading without full invocation pattern exploitation, rendering unsatisfactory optimization of the trade-off between cold start latency and resource waste. To bridge this gap, we propose SPES, the first differentiated scheduler for runtime cold start mitigation by optimizing serverless function provision. Our insight is that the common architecture of serverless systems prompts the concentration of certain invocation patterns, leading to predictable invocation behaviors. This allows us to categorize functions and pre-load/unload proper function instances with finer-grained strategies based on accurate invocation prediction. Experiments demonstrate the success of SPES in optimizing serverless function provision on both sides: reducing the 75th-percentile cold start rates by 49.77% and the wasted memory time by 56.43%, compared to the state-of-the-art. By mitigating the cold start issue, SPES is a promising advancement in facilitating cloud services deployed on serverless architectures.

## 내 메모


