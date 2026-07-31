---
type: research-source
item_id: 918
title: "Clip4Retrofit: Enabling Real-Time Image Labeling on Edge Devices via Cross-Architecture CLIP Distillation"
source: "arxiv"
published: "2025-05-23T15:42:52Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.18039"
url: "https://arxiv.org/abs/2505.18039v1"
generated_by: codex-research-db
aliases:
  - "Clip4Retrofit: Enabling Real-Time Image Labeling on Edge Devices via Cross-Architecture CLIP Distillation"
topics:
  - "edge-computing"
---

# Clip4Retrofit: Enabling Real-Time Image Labeling on Edge Devices via Cross-Architecture CLIP Distillation

[원문 열기](https://arxiv.org/abs/2505.18039v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`B3BD7JGF`)
- 발행일: 2025-05-23T15:42:52Z
- 저자: Li Zhong, Ahmed Ghazal, Jun-Jun Wan, Frederik Zilly, Patrick Mackens, Joachim E. Vollrath, Bogdan Sorin Coseriu
- 식별자: `arxiv:2505.18039`

## 요약·초록

Foundation models like CLIP (Contrastive Language-Image Pretraining) have revolutionized vision-language tasks by enabling zero-shot and few-shot learning through cross-modal alignment. However, their computational complexity and large memory footprint make them unsuitable for deployment on resource-constrained edge devices, such as in-car cameras used for image collection and real-time processing. To address this challenge, we propose Clip4Retrofit, an efficient model distillation framework that enables real-time image labeling on edge devices. The framework is deployed on the Retrofit camera, a cost-effective edge device retrofitted into thousands of vehicles, despite strict limitations on compute performance and memory. Our approach distills the knowledge of the CLIP model into a lightweight student model, combining EfficientNet-B3 with multi-layer perceptron (MLP) projection heads to preserve cross-modal alignment while significantly reducing computational requirements. We demonstrate that our distilled model achieves a balance between efficiency and performance, making it ideal for deployment in real-world scenarios. Experimental results show that Clip4Retrofit can perform real-time image labeling and object identification on edge devices with limited resources, offering a practical solution for applications such as autonomous driving and retrofitting existing systems. This work bridges the gap between state-of-the-art vision-language models and their deployment in resource-constrained environments, paving the way for broader adoption of foundation models in edge computing.

## 내 메모


