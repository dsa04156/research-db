---
type: research-source
item_id: 499
title: "DiffuseLoco: Real-Time Legged Locomotion Control with Diffusion from Offline Datasets"
source: "arxiv"
published: "2024-04-30T05:10:59Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2404.19264"
url: "https://arxiv.org/abs/2404.19264v1"
generated_by: codex-research-db
aliases:
  - "DiffuseLoco: Real-Time Legged Locomotion Control with Diffusion from Offline Datasets"
topics:
  - "edge-computing"
---

# DiffuseLoco: Real-Time Legged Locomotion Control with Diffusion from Offline Datasets

[원문 열기](https://arxiv.org/abs/2404.19264v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`54D6XJSU`)
- 발행일: 2024-04-30T05:10:59Z
- 저자: Xiaoyu Huang, Yufeng Chi, Ruofeng Wang, Zhongyu Li, Xue Bin Peng, Sophia Shao, Borivoje Nikolic, Koushil Sreenath
- 식별자: `arxiv:2404.19264`

## 요약·초록

This work introduces DiffuseLoco, a framework for training multi-skill diffusion-based policies for dynamic legged locomotion from offline datasets, enabling real-time control of diverse skills on robots in the real world. Offline learning at scale has led to breakthroughs in computer vision, natural language processing, and robotic manipulation domains. However, scaling up learning for legged robot locomotion, especially with multiple skills in a single policy, presents significant challenges for prior online reinforcement learning methods. To address this challenge, we propose a novel, scalable framework that leverages diffusion models to directly learn from offline multimodal datasets with a diverse set of locomotion skills. With design choices tailored for real-time control in dynamical systems, including receding horizon control and delayed inputs, DiffuseLoco is capable of reproducing multimodality in performing various locomotion skills, zero-shot transfer to real quadrupedal robots, and it can be deployed on edge computing devices. Furthermore, DiffuseLoco demonstrates free transitions between skills and robustness against environmental variations. Through extensive benchmarking in real-world experiments, DiffuseLoco exhibits better stability and velocity tracking performance compared to prior reinforcement learning and non-diffusion-based behavior cloning baselines. The design choices are validated via comprehensive ablation studies. This work opens new possibilities for scaling up learning-based legged locomotion controllers through the scaling of large, expressive models and diverse offline datasets.

## 내 메모


