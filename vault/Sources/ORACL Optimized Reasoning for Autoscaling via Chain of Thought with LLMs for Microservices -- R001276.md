---
type: research-source
item_id: 1276
title: "ORACL: Optimized Reasoning for Autoscaling via Chain of Thought with LLMs for Microservices"
source: "arxiv"
published: "2026-02-05T04:27:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2602.05292"
url: "https://arxiv.org/abs/2602.05292v1"
generated_by: codex-research-db
aliases:
  - "ORACL: Optimized Reasoning for Autoscaling via Chain of Thought with LLMs for Microservices"
topics:
  - "cloud-infrastructure"
---

# ORACL: Optimized Reasoning for Autoscaling via Chain of Thought with LLMs for Microservices

[원문 열기](https://arxiv.org/abs/2602.05292v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GVRDUGXK`)
- 발행일: 2026-02-05T04:27:29Z
- 저자: Haoyu Bai, Muhammed Tawfiqul Islam, Minxian Xu, Rajkumar Buyya
- 식별자: `arxiv:2602.05292`

## 요약·초록

Applications are moving away from monolithic designs to microservice and serverless architectures, where fleets of lightweight and independently deployable components run on public clouds. Autoscaling serves as the primary control mechanism for balancing resource utilization and quality of service, yet existing policies are either opaque learned models that require substantial per-deployment training or brittle hand-tuned rules that fail to generalize. We investigate whether large language models can act as universal few-shot resource allocators that adapt across rapidly evolving microservice deployments. We propose ORACL, Optimized Reasoning for Autoscaling via Chain of Thought with LLMs for Microservices, a framework that leverages prior knowledge and chain-of-thought reasoning to diagnose performance regressions and recommend resource allocations. ORACL transforms runtime telemetry, including pods, replicas, CPU and memory usage, latency, service-level objectives, and fault signals, into semantic natural-language state descriptions and invokes an LLM to produce an interpretable intermediate reasoning trace. This reasoning identifies likely root causes, prunes the action space, and issues safe allocation decisions under policy constraints. Experiments on representative open-source microservice workloads show that ORACL improves root-cause identification accuracy by 15 percent, accelerates training by up to 24x, and improves quality of service by 6 percent in short-term scenarios, without deployment-specific retraining.

## 내 메모


