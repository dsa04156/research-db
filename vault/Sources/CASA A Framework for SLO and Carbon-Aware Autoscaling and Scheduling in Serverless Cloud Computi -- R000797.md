---
type: research-source
item_id: 797
title: "CASA: A Framework for SLO and Carbon-Aware Autoscaling and Scheduling in Serverless Cloud Computing"
source: "arxiv"
published: "2024-08-31T22:10:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2409.00550"
url: "https://arxiv.org/abs/2409.00550v1"
generated_by: codex-research-db
aliases:
  - "CASA: A Framework for SLO and Carbon-Aware Autoscaling and Scheduling in Serverless Cloud Computing"
topics:
  - "cloud-infrastructure"
---

# CASA: A Framework for SLO and Carbon-Aware Autoscaling and Scheduling in Serverless Cloud Computing

[원문 열기](https://arxiv.org/abs/2409.00550v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZF7CB4SM`)
- 발행일: 2024-08-31T22:10:22Z
- 저자: S. Qi, H. Moore, N. Hogade, D. Milojicic, C. Bash, S. Pasricha
- 식별자: `arxiv:2409.00550`

## 요약·초록

Serverless computing is an emerging cloud computing paradigm that can reduce costs for cloud providers and their customers. However, serverless cloud platforms have stringent performance requirements (due to the need to execute short duration functions in a timely manner) and a growing carbon footprint. Traditional carbon-reducing techniques such as shutting down idle containers can reduce performance by increasing cold-start latencies of containers required in the future. This can cause higher violation rates of service level objectives (SLOs). Conversely, traditional latency-reduction approaches of prewarming containers or keeping them alive when not in use can improve performance but increase the associated carbon footprint of the serverless cluster platform. To strike a balance between sustainability and performance, in this paper, we propose a novel carbon- and SLO-aware framework called CASA to schedule and autoscale containers in a serverless cloud computing cluster. Experimental results indicate that CASA reduces the operational carbon footprint of a FaaS cluster by up to 2.6x while also reducing the SLO violation rate by up to 1.4x compared to the state-of-the-art.

## 내 메모


