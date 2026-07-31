---
type: research-source
item_id: 629
title: "EgoPrune: Efficient Token Pruning for Egomotion Video Reasoning in Embodied Agent"
source: "arxiv"
published: "2025-07-21T09:27:45Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.15428"
url: "https://arxiv.org/abs/2507.15428v1"
generated_by: codex-research-db
aliases:
  - "EgoPrune: Efficient Token Pruning for Egomotion Video Reasoning in Embodied Agent"
topics:
  - "ai-agents"
---

# EgoPrune: Efficient Token Pruning for Egomotion Video Reasoning in Embodied Agent

[원문 열기](https://arxiv.org/abs/2507.15428v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JW4ZHFB6`)
- 발행일: 2025-07-21T09:27:45Z
- 저자: Jiaao Li, Kaiyuan Li, Chen Gao, Yong Li, Xinlei Chen
- 식별자: `arxiv:2507.15428`

## 요약·초록

Egomotion videos are first-person recordings where the view changes continuously due to the agent's movement. As they serve as the primary visual input for embodied AI agents, making egomotion video reasoning more efficient is therefore essential for real-world deployment. Recent advances in vision-language models have enabled strong multimodal reasoning capabilities, but their computational cost remains prohibitive for long, redundant video inputs. Existing token pruning methods, typically designed for third-person videos, fail to leverage the spatiotemporal continuity and motion constraints inherent in egomotion settings. To address this, we propose EgoPrune, a training-free token pruning method tailored for egomotion video reasoning. EgoPrune comprises three components: a keyframe selector adapted from EmbodiedR for temporally efficient sampling; Perspective-Aware Redundancy Filtering (PARF), which aligns visual tokens using perspective transformations and removes redundant tokens; and a Maximal Marginal Relevance (MMR)-based token selector that jointly considers visual-text relevance and intra-frame diversity. Experiments on two egomotion video benchmarks show that EgoPrune consistently outperforms prior training-free methods across various pruning ratios while significantly reducing FLOPs, memory usage, and latency. Moreover, we deploy EgoPrune on an embodied agent equipped with a Jetson Orin NX 16GB edge device, demonstrating its real-world efficiency and suitability for on-device egomotion video reasoning.

## 내 메모


