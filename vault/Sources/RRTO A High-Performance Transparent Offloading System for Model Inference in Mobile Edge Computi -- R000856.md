---
type: research-source
item_id: 856
title: "RRTO: A High-Performance Transparent Offloading System for Model Inference in Mobile Edge Computing"
source: "arxiv"
published: "2025-07-29T12:16:56Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.21739"
url: "https://arxiv.org/abs/2507.21739v1"
generated_by: codex-research-db
aliases:
  - "RRTO: A High-Performance Transparent Offloading System for Model Inference in Mobile Edge Computing"
topics:
  - "edge-computing"
---

# RRTO: A High-Performance Transparent Offloading System for Model Inference in Mobile Edge Computing

[원문 열기](https://arxiv.org/abs/2507.21739v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6Q6FDA34`)
- 발행일: 2025-07-29T12:16:56Z
- 저자: Zekai Sun, Xiuxian Guan, Zheng Lin, Yuhao Qing, Haoze Song, Zihan Fang, Zhe Chen, Fangming Liu, Heming Cui, Wei Ni, Jun Luo
- 식별자: `arxiv:2507.21739`

## 요약·초록

Deploying Machine Learning (ML) applications on resource-constrained mobile devices remains challenging due to limited computational resources and poor platform compatibility. While Mobile Edge Computing (MEC) offers offloading-based inference paradigm using GPU servers, existing approaches are divided into non-transparent and transparent methods, with the latter necessitating modifications to the source code. Non-transparent offloading achieves high performance but requires intrusive code modification, limiting compatibility with diverse applications. Transparent offloading, in contrast, offers wide compatibility but introduces significant transmission delays due to per-operator remote procedure calls (RPCs). To overcome this limitation, we propose RRTO, the first high-performance transparent offloading system tailored for MEC inference. RRTO introduces a record/replay mechanism that leverages the static operator sequence in ML models to eliminate repetitive RPCs. To reliably identify this sequence, RRTO integrates a novel Operator Sequence Search algorithm that detects repeated patterns, filters initialization noise, and accelerates matching via a two-level strategy. Evaluation demonstrates that RRTO achieves substantial reductions of up to 98% in both per-inference latency and energy consumption compared to state-of-the-art transparent methods and yields results comparable to non-transparent approaches, all without necessitating any source code modification.

## 내 메모


