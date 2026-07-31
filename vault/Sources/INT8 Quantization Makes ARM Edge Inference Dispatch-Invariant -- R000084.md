---
type: research-source
item_id: 84
title: "INT8 Quantization Makes ARM Edge Inference Dispatch-Invariant"
source: "arxiv"
published: "2026-07-25T14:24:55Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.23227"
url: "https://arxiv.org/abs/2607.23227v1"
generated_by: codex-research-db
aliases:
  - "INT8 Quantization Makes ARM Edge Inference Dispatch-Invariant"
topics:
  - "edge-computing"
---

# INT8 Quantization Makes ARM Edge Inference Dispatch-Invariant

[원문 열기](https://arxiv.org/abs/2607.23227v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KNGR583Z`)
- 발행일: 2026-07-25T14:24:55Z
- 저자: Sebastián A. Cruz Romero, Shenied E. Maldonado Guerra
- 식별자: `arxiv:2607.23227`

## 요약·초록

On x86, kernel dispatch fragments the outputs of the same neural network into many equivalence classes across hardware. We ask whether the same fragmentation governs ARM edge inference, where most edge ML actually runs. Across four Raspberry Pi devices spanning Cortex-A53, A72, and A76 under ONNX Runtime CPU, microarchitecture is not observable in the outputs of a fixed FP32 CNN. Holding hardware constant at Cortex-A76 and switching only the execution provider, FP32 outputs disagree on every CIFAR-10 image with a mean remaining precision of 14.97 of 23 mantissa bits. INT8 QDQ post-training quantization collapses both axes to a single equivalence class. We trace this to a structural property of QDQ graphs that we call H1+H2: discrete-grid inputs make any Conv dispatch-deterministic (H1) and QuantizeLinear at every layer boundary preserves that precondition (H2). H1+H2 predicts that bit-exact agreement should extend to production CNNs under runtimes that confirmably exercise different ARM microkernels. We verify this on MobileNetV2 and ResNet50V2 under TensorFlow Lite with XNNPACK, where timing evidence confirms SDOT dispatch on A76 and NEON multiply-accumulate on A72 yet every intermediate INT32 accumulator and every final output is byte-identical across 500 ImageNet images per model. We then identify the specific x86 mechanism that breaks the same invariant on x86, namely PMADDUBSW saturating INT16 intermediates, which has no ARM analogue. The Schlögl et al. divergence phenomenon is delineated rather than contradicted. For practitioners deploying quantized CNNs across heterogeneous ARM fleets, the operational consequence is direct. INT8 inference is the reproducible mode and the relevant behavioral variation axis is precision, not microarchitecture.

## 내 메모


