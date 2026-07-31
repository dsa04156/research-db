---
type: research-source
item_id: 941
title: "You Sense Only Once Beneath: Ultra-Light Real-Time Underwater Object Detection"
source: "arxiv"
published: "2025-04-22T08:26:35Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/rcar65431.2025.11139626"
url: "https://arxiv.org/abs/2504.15694v1"
generated_by: codex-research-db
aliases:
  - "You Sense Only Once Beneath: Ultra-Light Real-Time Underwater Object Detection"
topics:
  - "edge-computing"
---

# You Sense Only Once Beneath: Ultra-Light Real-Time Underwater Object Detection

[원문 열기](https://arxiv.org/abs/2504.15694v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VN87NIND`)
- 발행일: 2025-04-22T08:26:35Z
- 저자: Jun Dong, Wenli Wu, Jintao Cheng, Xiaoyu Tang
- 식별자: `doi:10.1109/rcar65431.2025.11139626`

## 요약·초록

Despite the remarkable achievements in object detection, the model's accuracy and efficiency still require further improvement under challenging underwater conditions, such as low image quality and limited computational resources. To address this, we propose an Ultra-Light Real-Time Underwater Object Detection framework, You Sense Only Once Beneath (YSOOB). Specifically, we utilize a Multi-Spectrum Wavelet Encoder (MSWE) to perform frequency-domain encoding on the input image, minimizing the semantic loss caused by underwater optical color distortion. Furthermore, we revisit the unique characteristics of even-sized and transposed convolutions, allowing the model to dynamically select and enhance key information during the resampling process, thereby improving its generalization ability. Finally, we eliminate model redundancy through a simple yet effective channel compression and reconstructed large kernel convolution (RLKC) to achieve model lightweight. As a result, forms a high-performance underwater object detector YSOOB with only 1.2 million parameters. Extensive experimental results demonstrate that, with the fewest parameters, YSOOB achieves mAP50 of 83.1% and 82.9% on the URPC2020 and DUO datasets, respectively, comparable to the current SOTA detectors. The inference speed reaches 781.3 FPS and 57.8 FPS on the T4 GPU (TensorRT FP16) and the edge computing device Jetson Xavier NX (TensorRT FP16), surpassing YOLOv12-N by 28.1% and 22.5%, respectively.

## 내 메모


