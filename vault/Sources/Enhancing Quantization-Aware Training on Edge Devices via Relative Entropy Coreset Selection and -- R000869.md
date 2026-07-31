---
type: research-source
item_id: 869
title: "Enhancing Quantization-Aware Training on Edge Devices via Relative Entropy Coreset Selection and Cascaded Layer Correction"
source: "arxiv"
published: "2025-07-17T02:19:33Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.17768"
url: "https://arxiv.org/abs/2507.17768v1"
generated_by: codex-research-db
aliases:
  - "Enhancing Quantization-Aware Training on Edge Devices via Relative Entropy Coreset Selection and Cascaded Layer Correction"
topics:
  - "edge-computing"
---

# Enhancing Quantization-Aware Training on Edge Devices via Relative Entropy Coreset Selection and Cascaded Layer Correction

[원문 열기](https://arxiv.org/abs/2507.17768v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`T8FAENIM`)
- 발행일: 2025-07-17T02:19:33Z
- 저자: Yujia Tong, Jingling Yuan, Chuang Hu
- 식별자: `arxiv:2507.17768`

## 요약·초록

With the development of mobile and edge computing, the demand for low-bit quantized models on edge devices is increasing to achieve efficient deployment. To enhance the performance, it is often necessary to retrain the quantized models using edge data. However, due to privacy concerns, certain sensitive data can only be processed on edge devices. Therefore, employing Quantization-Aware Training (QAT) on edge devices has become an effective solution. Nevertheless, traditional QAT relies on the complete dataset for training, which incurs a huge computational cost. Coreset selection techniques can mitigate this issue by training on the most representative subsets. However, existing methods struggle to eliminate quantization errors in the model when using small-scale datasets (e.g., only 10% of the data), leading to significant performance degradation. To address these issues, we propose QuaRC, a QAT framework with coresets on edge devices, which consists of two main phases: In the coreset selection phase, QuaRC introduces the ``Relative Entropy Score" to identify the subsets that most effectively capture the model's quantization errors. During the training phase, QuaRC employs the Cascaded Layer Correction strategy to align the intermediate layer outputs of the quantized model with those of the full-precision model, thereby effectively reducing the quantization errors in the intermediate layers. Experimental results demonstrate the effectiveness of our approach. For instance, when quantizing ResNet-18 to 2-bit using a 1% data subset, QuaRC achieves a 5.72% improvement in Top-1 accuracy on the ImageNet-1K dataset compared to state-of-the-art techniques.

## 내 메모


