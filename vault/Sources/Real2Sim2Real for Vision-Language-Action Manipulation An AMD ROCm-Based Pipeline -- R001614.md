---
type: research-source
item_id: 1614
title: "Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline"
source: "arxiv"
published: "2026-07-25T02:23:34Z"
first_seen: "2026-07-31"
review_status: "pending"
canonical_key: "arxiv:2607.22997"
url: "https://arxiv.org/abs/2607.22997v1"
generated_by: codex-research-db
aliases:
  - "Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline"
topics:
  - "edge-computing"
---

# Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline

[원문 열기](https://arxiv.org/abs/2607.22997v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-31|2026-07-31]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`PIJGG4AI`)
- 발행일: 2026-07-25T02:23:34Z
- 저자: Qing Yang, Xun Wang, Ziguan Wang, Zhenjiang Li, Hongqiang Wang, Dongdong Weng
- 식별자: `arxiv:2607.22997`

## 요약·초록

Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr. Lisa Su (`we're entering the world of Physical AI ... this is where AI enters the real world,' CES 2026). This paper presents an end-to-end, fully AMD-accelerated technology stack for embodied manipulation, spanning data-center training silicon, Radeon PRO simulation/rendering GPUs, and Ryzen AI edge compute, unified by the open ROCm software stack. We demonstrate that training and deploying VLA-based manipulation policies does not require a CUDA-locked ecosystem. Four progressive demonstrations are presented: (1) a Sim-to-Real manipulation pipeline trained with SmolVLA and deployed on a physical Franka arm; (2) a semantic, language-grounded object-selection task (`one-of-three'); (3) a Real2Sim synthetic-data generation pipeline that fuses 3D Gaussian Splatting (3DGS) reconstructions of real scenes with the Genesis physics engine; and (4) large-scale reinforcement learning for quadruped and humanoid locomotion benchmarked across multiple hardware platforms. All pipelines run natively on ROCm + PyTorch on RDNA4 (Radeon AI PRO R9700) and RDNA3.5 (Radeon PRO W7900) hardware and are reproducible on the free Radeon Cloud Platform.

## 내 메모


