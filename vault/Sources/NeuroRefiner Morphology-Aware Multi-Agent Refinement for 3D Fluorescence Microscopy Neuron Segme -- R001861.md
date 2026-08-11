---
type: research-source
item_id: 1861
title: "NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation"
source: "arxiv"
published: "2026-08-10T14:14:47Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.09636"
url: "https://arxiv.org/abs/2608.09636v1"
generated_by: codex-research-db
aliases:
  - "NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation"
topics:
  - "ai-agents"
---

# NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation

[원문 열기](https://arxiv.org/abs/2608.09636v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-10T14:14:47Z
- 저자: Haiyang Yan, Jinyue Guo, Yanchao Zhang, Bingqing Wang, Zhenchen Li, Jing Liu, Jiazheng Liu, Linlin Li, Hua Han
- 식별자: `arxiv:2608.09636`

## 요약·초록

Accurate 3D neuron segmentation in fluorescence microscopy is critical for neuroscience. However, the sparse and elongated morphology of neurons poses significant challenges to existing segmentation methods. These methods struggle to preserve both local details and global topology, leading to fragmented results. To address this, we propose NeuroRefiner, a multi-agent system that formalizes the human expert workflow involving iterative global observation and local editing. Specifically, NeuroRefiner comprises three collaborative agents dedicated to diagnosing topological errors, generating correction instructions, and validating refinement quality. To facilitate agent instruction-guided segmentation refinement, we propose TopoRefineNet, a dedicated 3D U-Net-based tool that leverages cross-modality feature fusion to generate refined masks. Through multi-round agent reasoning and voxel-level editing, NeuroRefiner produces topologically more accurate segmentations with enhanced interpretability. Experiments on the BigNeuron, CWMBS, and ZBFWB datasets demonstrate that NeuroRefiner outperforms state-of-the-art methods, notably achieving a 3.02% improvement in F1 score on the challenging ZBFWB dataset.

## 내 메모


