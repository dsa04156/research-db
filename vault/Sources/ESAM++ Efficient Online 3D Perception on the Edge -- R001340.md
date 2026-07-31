---
type: research-source
item_id: 1340
title: "ESAM++: Efficient Online 3D Perception on the Edge"
source: "arxiv"
published: "2026-05-28T07:29:02Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.29505"
url: "https://arxiv.org/abs/2605.29505v1"
generated_by: codex-research-db
aliases:
  - "ESAM++: Efficient Online 3D Perception on the Edge"
topics:
  - "edge-computing"
---

# ESAM++: Efficient Online 3D Perception on the Edge

[원문 열기](https://arxiv.org/abs/2605.29505v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JXAUJK7I`)
- 발행일: 2026-05-28T07:29:02Z
- 저자: Qin Liu, Lavisha Aggarwal, Saptarashmi Bandyopadhyay, Vikas Bahirwani, Marc Niethammer, Ehsan Adeli, Andrea Colaco
- 식별자: `arxiv:2605.29505`

## 요약·초록

Online 3D scene perception in real time is essential for robotics, AR/VR, and autonomous systems, particularly in edge computing scenarios where computational resources are limited and privacy is crucial. Recent state-of-the-art methods like EmbodiedSAM (ESAM) demonstrate the promise of online 3D perception by leveraging the Segment Anything Model (SAM) for real-time, fine-grained, and generalized 3D instance segmentation. However, ESAM still relies on a computationally expensive 3D sparse UNet for point cloud feature extraction, which accounts for the majority of the 3D inference time, hindering its practicality on resource-constrained devices. In this paper, we propose ESAM++, a lightweight and scalable alternative for online 3D scene perception tailored to edge devices without GPU acceleration. Our method introduces a 3D Sparse Feature Pyramid Network (SFPN) that efficiently captures multi-scale geometric features from streaming 3D point clouds while significantly reducing computational overhead and model size. We evaluate our approach on four challenging segmentation benchmarks, namely ScanNet, ScanNet200, SceneNN, and 3RScan, demonstrating that our model achieves competitive accuracy with up to 3 times faster inference with a 2 times smaller model size compared to ESAM, enabling practical deployment on edge devices.

## 내 메모


