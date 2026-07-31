---
type: research-source
item_id: 487
title: "EdgeLoc: A Communication-Adaptive Parallel System for Real-Time Localization in Infrastructure-Assisted Autonomous Driving"
source: "arxiv"
published: "2024-05-20T15:38:53Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.12120"
url: "https://arxiv.org/abs/2405.12120v2"
generated_by: codex-research-db
aliases:
  - "EdgeLoc: A Communication-Adaptive Parallel System for Real-Time Localization in Infrastructure-Assisted Autonomous Driving"
topics:
  - "edge-computing"
---

# EdgeLoc: A Communication-Adaptive Parallel System for Real-Time Localization in Infrastructure-Assisted Autonomous Driving

[원문 열기](https://arxiv.org/abs/2405.12120v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VGEP8SPD`)
- 발행일: 2024-05-20T15:38:53Z
- 저자: Boyi Liu, Jingwen Tong, Yufan Zhuang
- 식별자: `arxiv:2405.12120`

## 요약·초록

This paper presents EdgeLoc, an infrastructure-assisted, real-time localization system for autonomous driving that addresses the incompatibility between traditional localization methods and deep learning approaches. The system is built on top of the Robot Operating System (ROS) and combines the real-time performance of traditional methods with the high accuracy of deep learning approaches. The system leverages edge computing capabilities of roadside units (RSUs) for precise localization to enhance on-vehicle localization that is based on the real-time visual odometry. EdgeLoc is a parallel processing system, utilizing a proposed uncertainty-aware pose fusion solution. It achieves communication adaptivity through online learning and addresses fluctuations via window-based detection. Moreover, it achieves optimal latency and maximum improvement by utilizing auto-splitting vehicle-infrastructure collaborative inference, as well as online distribution learning for decision-making. Even with the most basic end-to-end deep neural network for localization estimation, EdgeLoc realizes a 67.75\% reduction in the localization error for real-time local visual odometry, a 29.95\% reduction for non-real-time collaborative inference, and a 30.26\% reduction compared to Kalman filtering. Finally, accuracy-to-latency conversion was experimentally validated, and an overall experiment was conducted on a practical cellular network. The system is open sourced at https://github.com/LoganCome/EdgeAssistedLocalization.

## 내 메모


