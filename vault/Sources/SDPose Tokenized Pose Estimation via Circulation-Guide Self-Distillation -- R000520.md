---
type: research-source
item_id: 520
title: "SDPose: Tokenized Pose Estimation via Circulation-Guide Self-Distillation"
source: "arxiv"
published: "2024-04-04T15:23:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2404.03518"
url: "https://arxiv.org/abs/2404.03518v1"
generated_by: codex-research-db
aliases:
  - "SDPose: Tokenized Pose Estimation via Circulation-Guide Self-Distillation"
topics:
  - "edge-computing"
---

# SDPose: Tokenized Pose Estimation via Circulation-Guide Self-Distillation

[원문 열기](https://arxiv.org/abs/2404.03518v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`45FRZNWG`)
- 발행일: 2024-04-04T15:23:14Z
- 저자: Sichen Chen, Yingyi Zhang, Siming Huang, Ran Yi, Ke Fan, Ruixin Zhang, Peixian Chen, Jun Wang, Shouhong Ding, Lizhuang Ma
- 식별자: `arxiv:2404.03518`

## 요약·초록

Recently, transformer-based methods have achieved state-of-the-art prediction quality on human pose estimation(HPE). Nonetheless, most of these top-performing transformer-based models are too computation-consuming and storage-demanding to deploy on edge computing platforms. Those transformer-based models that require fewer resources are prone to under-fitting due to their smaller scale and thus perform notably worse than their larger counterparts. Given this conundrum, we introduce SDPose, a new self-distillation method for improving the performance of small transformer-based models. To mitigate the problem of under-fitting, we design a transformer module named Multi-Cycled Transformer(MCT) based on multiple-cycled forwards to more fully exploit the potential of small model parameters. Further, in order to prevent the additional inference compute-consuming brought by MCT, we introduce a self-distillation scheme, extracting the knowledge from the MCT module to a naive forward model. Specifically, on the MSCOCO validation dataset, SDPose-T obtains 69.7% mAP with 4.4M parameters and 1.8 GFLOPs. Furthermore, SDPose-S-V2 obtains 73.5% mAP on the MSCOCO validation dataset with 6.2M parameters and 4.7 GFLOPs, achieving a new state-of-the-art among predominant tiny neural network methods. Our code is available at https://github.com/MartyrPenink/SDPose.

## 내 메모


