---
type: research-source
item_id: 1387
title: "Efficient Few-Shot Learning for Edge AI via Knowledge Distillation on MobileViT"
source: "arxiv"
published: "2026-03-27T08:02:50Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.26145"
url: "https://arxiv.org/abs/2603.26145v1"
generated_by: codex-research-db
aliases:
  - "Efficient Few-Shot Learning for Edge AI via Knowledge Distillation on MobileViT"
topics:
  - "edge-computing"
---

# Efficient Few-Shot Learning for Edge AI via Knowledge Distillation on MobileViT

[원문 열기](https://arxiv.org/abs/2603.26145v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GBBHPGVQ`)
- 발행일: 2026-03-27T08:02:50Z
- 저자: Shuhei Tsuyuki, Reda Bensaid, Jérémy Morlier, Mathieu Léonardon, Naoya Onizawa, Vincent Gripon, Takahiro Hanyu
- 식별자: `arxiv:2603.26145`

## 요약·초록

Efficient and adaptable deep learning models are an important area of deep learning research, driven by the need for highly efficient models on edge devices. Few-shot learning enables the use of deep learning models in low-data regimes, a capability that is highly sought after in real-world applications where collecting large annotated datasets is costly or impractical. This challenge is particularly relevant in edge scenarios, where connectivity may be limited, low-latency responses are required, or energy consumption constraints are critical. We propose and evaluate a pre-training method for the MobileViT backbone designed for edge computing. Specifically, we employ knowledge distillation, which transfers the generalization ability of a large-scale teacher model to a lightweight student model. This method achieves accuracy improvements of 14% and 6.7% for one-shot and five-shot classification, respectively, on the MiniImageNet benchmark, compared to the ResNet12 baseline, while reducing by 69% the number of parameters and by 88% the computational complexity of the model, in FLOPs. Furthermore, we deployed the proposed models on a Jetson Orin Nano platform and measured power consumption directly at the power supply, showing that the dynamic energy consumption is reduced by 37% with a latency of 2.6 ms. These results demonstrate that the proposed method is a promising and practical solution for deploying few-shot learning models on edge AI hardware.

## 내 메모


