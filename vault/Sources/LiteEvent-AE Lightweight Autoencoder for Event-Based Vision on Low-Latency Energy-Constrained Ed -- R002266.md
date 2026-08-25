---
type: research-source
item_id: 2266
title: "LiteEvent-AE: Lightweight Autoencoder for Event-Based Vision on Low-Latency Energy-Constrained Edge Devices"
source: "arxiv"
published: "2026-08-22T04:13:47Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.21764"
url: "https://arxiv.org/abs/2608.21764v1"
generated_by: codex-research-db
aliases:
  - "LiteEvent-AE: Lightweight Autoencoder for Event-Based Vision on Low-Latency Energy-Constrained Edge Devices"
topics:
  - "edge-computing"
---

# LiteEvent-AE: Lightweight Autoencoder for Event-Based Vision on Low-Latency Energy-Constrained Edge Devices

[원문 열기](https://arxiv.org/abs/2608.21764v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-22T04:13:47Z
- 저자: Riadul Islam, Joey Mule, Dhandeep Challagundla, Shahmir Rizvi, Sean Carson, Rachit Saini
- 식별자: `arxiv:2608.21764`

## 요약·초록

Event-based vision has emerged as a promising paradigm for energy-aware artificial intelligence (AI), offering sparse, low-latency visual signals that reduce redundant data processing and support sustainable edge computing. However, the asynchronous and noise-prone nature of event streams creates challenges for conventional deep learning models, which are often too computationally intensive for low-power embedded platforms. This work presents a compact and configurable event-driven autoencoder that efficiently compresses neuromorphic data while preserving essential spatiotemporal structure for downstream inference. The architecture integrates lightweight convolutional encoding with robust performance under adaptive event thresholding and a minimal classifier head, enabling substantial reductions in computational cost without degrading recognition fidelity. Extensive evaluations on the Smart Event Face Dataset (SEFD) and Event-Based Crossing Dataset (EBCD) show that the proposed framework achieves competitive or superior accuracy compared to YOLOv9 while requiring up to 35.6$\times$ fewer parameters. To assess real-world sustainability, the model is deployed on resource-constrained hardware: a Raspberry Pi 4B and a NVIDIA Jetson Nano. On NVIDIA Jetson Nano, it delivers real-time throughput of 44.8 FPS. On a Raspberry Pi 4B CPU, the 50\% autoencoder classifier consumes 16.19 J for the evaluated inference workload, corresponding to approximately 726.3$\times$ lower energy consumption than YOLOv9 under the same evaluation protocol. These results demonstrate the potential of compact event-driven models to advance environmentally conscious, low-power AI systems for high-speed perception in autonomous, mobile, and embedded computing environments.

## 내 메모
