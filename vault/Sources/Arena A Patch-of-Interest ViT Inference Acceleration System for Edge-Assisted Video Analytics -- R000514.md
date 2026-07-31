---
type: research-source
item_id: 514
title: "Arena: A Patch-of-Interest ViT Inference Acceleration System for Edge-Assisted Video Analytics"
source: "arxiv"
published: "2024-04-14T13:14:13Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2404.09245"
url: "https://arxiv.org/abs/2404.09245v2"
generated_by: codex-research-db
aliases:
  - "Arena: A Patch-of-Interest ViT Inference Acceleration System for Edge-Assisted Video Analytics"
topics:
  - "edge-computing"
---

# Arena: A Patch-of-Interest ViT Inference Acceleration System for Edge-Assisted Video Analytics

[원문 열기](https://arxiv.org/abs/2404.09245v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FQCF6QRF`)
- 발행일: 2024-04-14T13:14:13Z
- 저자: Haosong Peng, Wei Feng, Hao Li, Yufeng Zhan, Ren Jin, Yuanqing Xia
- 식별자: `arxiv:2404.09245`

## 요약·초록

The advent of edge computing has made real-time intelligent video analytics feasible. Previous works, based on traditional model architecture (e.g., CNN, RNN, etc.), employ various strategies to filter out non-region-of-interest content to minimize bandwidth and computation consumption but show inferior performance in adverse environments. Recently, visual foundation models based on transformers have shown great performance in adverse environments due to their amazing generalization capability. However, they require a large amount of computation power, which limits their applications in real-time intelligent video analytics. In this paper, we find visual foundation models like Vision Transformer (ViT) also have a dedicated acceleration mechanism for video analytics. To this end, we introduce Arena, an end-to-end edge-assisted video inference acceleration system based on ViT. We leverage the capability of ViT that can be accelerated through token pruning by only offloading and feeding Patches-of-Interest to the downstream models. Additionally, we design an adaptive keyframe inference switching algorithm tailored to different videos, capable of adapting to the current video content to jointly optimize accuracy and bandwidth. Through extensive experiments, our findings reveal that Arena can boost inference speeds by up to 1.58\(\times\) and 1.82\(\times\) on average while consuming only 47\% and 31\% of the bandwidth, respectively, all with high inference accuracy.

## 내 메모


