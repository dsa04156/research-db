---
type: research-source
item_id: 3062
title: "TriFleetRCA: On-Premise LLM Root Cause Analysis for Kubernetes"
source: "arxiv"
published: "2026-09-20T17:34:18Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.23766"
url: "https://arxiv.org/abs/2609.23766v1"
generated_by: codex-research-db
aliases:
  - "TriFleetRCA: On-Premise LLM Root Cause Analysis for Kubernetes"
topics:
  - "kubernetes"
---

# TriFleetRCA: On-Premise LLM Root Cause Analysis for Kubernetes

[원문 열기](https://arxiv.org/abs/2609.23766v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-20T17:34:18Z
- 저자: Rohit Patel, Susil Kumar Mohanty, Jeenal Chaudhary
- 식별자: `arxiv:2609.23766`

## 요약·초록

Root cause analysis at a remote site is slow: evidence is scattered across pod logs, Kubernetes events and cluster-level objects, and many operators cannot send production logs to a hosted model at all. On-premise inference removes the second constraint but raises a question live-cluster benchmarks have not addressed: when one workstation GPU fixes both the model and the context budget, how should evidence be retrieved, and what happens when the runbooks the model consults have been tampered with? We present TriFleetRCA, a pipeline running entirely on one on-premise GPU that collects evidence at one of three scopes (pod, namespace, cluster), ranks it by template de-duplication then BM25, filters runbooks through an ingest guard, and returns a root cause with the evidence lines supporting it. We evaluate on a live Kubernetes cluster into which we inject four faults, so ground truth is known by construction, across 100 analyses with Qwen2.5-14B-Instruct at temperature 0. The hit rate was 0.85, 0.90 and 0.95 at pod, namespace and cluster scope; intervals overlap, but the whole scope effect comes from the one fault whose cause is a cluster-level object, and cluster scope costs 55% more tokens. De-duplication before ranking raised the hit rate from 0.75 to 0.90 at equal token cost. A poisoned runbook telling the model to delete the namespace was rejected by the guard every run; with the guard disabled the model declined to follow it in all 20 analyses, making the guard defence in depth rather than the sole barrier. Separating citation quality from accuracy proved informative: one fault was diagnosed correctly and cited incorrectly every trial, a failure mode accuracy conceals. Median latency was 1.6 s at 2,200 prompt tokens. We release the pipeline, the fault injector and all records.

## 내 메모
