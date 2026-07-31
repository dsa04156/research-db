---
type: research-source
item_id: 886
title: "Radar and Event Camera Fusion for Agile Robot Ego-Motion Estimation"
source: "arxiv"
published: "2025-06-23T09:27:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2506.18443"
url: "https://arxiv.org/abs/2506.18443v2"
generated_by: codex-research-db
aliases:
  - "Radar and Event Camera Fusion for Agile Robot Ego-Motion Estimation"
topics:
  - "edge-computing"
---

# Radar and Event Camera Fusion for Agile Robot Ego-Motion Estimation

[원문 열기](https://arxiv.org/abs/2506.18443v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KXJGJ2ZC`)
- 발행일: 2025-06-23T09:27:22Z
- 저자: Yang Lyu, Zhenghao Zou, Yanfeng Li, Xiaohu Guo, Chunhui Zhao, Quan Pan
- 식별자: `arxiv:2506.18443`

## 요약·초록

Achieving reliable ego motion estimation for agile robots, e.g., aerobatic aircraft, remains challenging because most robot sensors fail to respond timely and clearly to highly dynamic robot motions, often resulting in measurement blurring, distortion, and delays. In this paper, we propose an IMU-free and feature-association-free framework to achieve aggressive ego-motion velocity estimation of a robot platform in highly dynamic scenarios by combining two types of exteroceptive sensors, an event camera and a millimeter wave radar, First, we used instantaneous raw events and Doppler measurements to derive rotational and translational velocities directly. Without a sophisticated association process between measurement frames, the proposed method is more robust in texture-less and structureless environments and is more computationally efficient for edge computing devices. Then, in the back-end, we propose a continuous-time state-space model to fuse the hybrid time-based and event-based measurements to estimate the ego-motion velocity in a fixed-lagged smoother fashion. In the end, we validate our velometer framework extensively in self-collected experiment datasets. The results indicate that our IMU-free and association-free ego motion estimation framework can achieve reliable and efficient velocity output in challenging environments. The source code, illustrative video and dataset are available at https://github.com/ZzhYgwh/TwistEstimator.

## 내 메모


