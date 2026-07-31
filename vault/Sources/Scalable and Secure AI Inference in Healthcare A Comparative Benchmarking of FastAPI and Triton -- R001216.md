---
type: research-source
item_id: 1216
title: "Scalable and Secure AI Inference in Healthcare: A Comparative Benchmarking of FastAPI and Triton Inference Server on Kubernetes"
source: "arxiv"
published: "2026-01-19T18:48:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2602.00053"
url: "https://arxiv.org/abs/2602.00053v1"
generated_by: codex-research-db
aliases:
  - "Scalable and Secure AI Inference in Healthcare: A Comparative Benchmarking of FastAPI and Triton Inference Server on Kubernetes"
topics:
  - "kubernetes"
---

# Scalable and Secure AI Inference in Healthcare: A Comparative Benchmarking of FastAPI and Triton Inference Server on Kubernetes

[원문 열기](https://arxiv.org/abs/2602.00053v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VPIW6E6V`)
- 발행일: 2026-01-19T18:48:29Z
- 저자: Ratul Ali
- 식별자: `arxiv:2602.00053`

## 요약·초록

Efficient and scalable deployment of machine learning (ML) models is a prerequisite for modern production environments, particularly within regulated domains such as healthcare and pharmaceuticals. In these settings, systems must balance competing requirements, including minimizing inference latency for real-time clinical decision support, maximizing throughput for batch processing of medical records, and ensuring strict adherence to data privacy standards such as HIPAA. This paper presents a rigorous benchmarking analysis comparing two prominent deployment paradigms: a lightweight, Python-based REST service using FastAPI, and a specialized, high-performance serving engine, NVIDIA Triton Inference Server. Leveraging a reference architecture for healthcare AI, we deployed a DistilBERT sentiment analysis model on Kubernetes to measure median (p50) and tail (p95) latency, as well as throughput, under controlled experimental conditions. Our results indicate a distinct trade-off. While FastAPI provides lower overhead for single-request workloads with a p50 latency of 22 ms, Triton achieves superior scalability through dynamic batching, delivering a throughput of 780 requests per second on a single NVIDIA T4 GPU, nearly double that of the baseline. Furthermore, we evaluate a hybrid architectural approach that utilizes FastAPI as a secure gateway for protected health information de-identification and Triton for backend inference. This study validates the hybrid model as a best practice for enterprise clinical AI and offers a blueprint for secure, high-availability deployments.

## 내 메모


