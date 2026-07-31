---
type: research-source
item_id: 565
title: "Neural Finite-State Machines for Surgical Phase Recognition"
source: "arxiv"
published: "2024-11-27T03:21:57Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2411.18018"
url: "https://arxiv.org/abs/2411.18018v2"
generated_by: codex-research-db
aliases:
  - "Neural Finite-State Machines for Surgical Phase Recognition"
topics:
  - "self-evolving-harness"
---

# Neural Finite-State Machines for Surgical Phase Recognition

[원문 열기](https://arxiv.org/abs/2411.18018v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`CMC8PPCU`)
- 발행일: 2024-11-27T03:21:57Z
- 저자: Hao Ding, Zhongpai Gao, Benjamin Planche, Tianyu Luan, Abhishek Sharma, Meng Zheng, Ange Lou, Terrence Chen, Mathias Unberath, Ziyan Wu
- 식별자: `arxiv:2411.18018`

## 요약·초록

Surgical phase recognition (SPR) is crucial for applications in workflow optimization, performance evaluation, and real-time intervention guidance. However, current deep learning models often struggle with fragmented predictions, failing to capture the sequential nature of surgical workflows. We propose the Neural Finite-State Machine (NFSM), a novel approach that enforces temporal coherence by integrating classical state-transition priors with modern neural networks. NFSM leverages learnable global state embeddings as unique phase identifiers and dynamic transition tables to model phase-to-phase progressions. Additionally, a future phase forecasting mechanism employs repeated frame padding to anticipate upcoming transitions. Implemented as a plug-and-play module, NFSM can be integrated into existing SPR pipelines without changing their core architectures. We demonstrate state-of-the-art performance across multiple benchmarks, including a significant improvement on the BernBypass70 dataset - raising video-level accuracy by 0.9 points and phase-level precision, recall, F1-score, and mAP by 3.8, 3.1, 3.3, and 4.1, respectively. Ablation studies confirm each component's effectiveness and the module's adaptability to various architectures. By unifying finite-state principles with deep learning, NFSM offers a robust path toward consistent, long-term surgical video analysis.

## 내 메모


