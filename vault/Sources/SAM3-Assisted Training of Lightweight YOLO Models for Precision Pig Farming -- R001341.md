---
type: research-source
item_id: 1341
title: "SAM3-Assisted Training of Lightweight YOLO Models for Precision Pig Farming"
source: "arxiv"
published: "2026-05-25T13:50:24Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.25860"
url: "https://arxiv.org/abs/2605.25860v1"
generated_by: codex-research-db
aliases:
  - "SAM3-Assisted Training of Lightweight YOLO Models for Precision Pig Farming"
topics:
  - "edge-computing"
---

# SAM3-Assisted Training of Lightweight YOLO Models for Precision Pig Farming

[원문 열기](https://arxiv.org/abs/2605.25860v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2CZM3EE4`)
- 발행일: 2026-05-25T13:50:24Z
- 저자: Marcos Vinicius Mendes Faria, Thiago Borges Pereira, Isabella C. F. S. Condotta, Thiago Meireles Paixão, Francisco de Assis Boldt
- 식별자: `arxiv:2605.25860`

## 요약·초록

Deep learning-based object detection has revolutionized Precision Livestock Farming (PLF), yet a critical barrier remains: high-performance Foundation Models (such as SAM 3) are too computationally intensive for edge deployment, while lightweight models (like YOLO) require prohibitive manual annotation efforts. This work proposes a fully automated knowledge distillation pipeline that leverages the Segment Anything Model 3 (SAM 3) to generate zero-shot pseudo-labels for training efficient YOLOv8 detectors. By treating SAM 3 as an offline auto-annotator, we eliminate the manual labeling bottleneck, producing models capable of real-time inference on resource-constrained hardware. We systematically evaluate this approach on the PigLife dataset, comparing SAM 3-supervised models against human-annotated baselines. Results demonstrate that a SAM 3-trained YOLOv8m achieves a mean Average Precision (mAP) of 79.4% without human intervention, while reducing inference latency by approximately 200$\times$ compared to the teacher model. Furthermore, stratified analysis reveals that in low-occlusion scenarios, the automated pipeline achieves detection rates comparable to human benchmarks ($AP_{50} > 99\%$). These findings indicate that foundation models can serve as effective, zero-annotation-cost supervisors, enabling scalable edge computing solutions for smart agriculture.

## 내 메모


