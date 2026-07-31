---
type: research-source
item_id: 1353
title: "LLM-Enhanced Deep Reinforcement Learning for Task Offloading in Collaborative Edge Computing"
source: "arxiv"
published: "2026-05-07T06:19:07Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.05727"
url: "https://arxiv.org/abs/2605.05727v2"
generated_by: codex-research-db
aliases:
  - "LLM-Enhanced Deep Reinforcement Learning for Task Offloading in Collaborative Edge Computing"
topics:
  - "edge-computing"
---

# LLM-Enhanced Deep Reinforcement Learning for Task Offloading in Collaborative Edge Computing

[원문 열기](https://arxiv.org/abs/2605.05727v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`73H5HWW7`)
- 발행일: 2026-05-07T06:19:07Z
- 저자: Hao Guo, Kaixiang Xu, Ziwu Ge, Lei Yang
- 식별자: `arxiv:2605.05727`

## 요약·초록

Collaborative edge computing uses edge nodes in different locations to execute tasks, necessitating dynamic task offloading decisions to maintain low latency and high reliability, especially under unpredictable node failures. Although deep reinforcement learning (DRL) and large language models (LLMs) have shown promise for task offloading, DRL often suffers from poor sample efficiency and local optima, while LLMs are difficult to use directly due to inference overhead and output uncertainty. To address these limitations, we propose \textbf{LeDRL}, a hybrid decision framework that couples a \emph{lightweight LLM} with self-attention-enhanced DRL for real-time task offloading. LeDRL constructs structured, context-aware prompts capturing node status, task semantics, and link dynamics to derive high-level strategy priors. These are selectively processed by a self-attention-based alignment module for context-aware policy optimization. A reflective evaluator further distills semantic feedback from past trajectories to refine subsequent prompts and provide consistent guidance. Extensive experiments show that LeDRL outperforms representative baselines in task success rate, convergence speed, and real-time responsiveness across diverse network scales, achieving over 17\% improvement in success rate. Furthermore, we deploy LeDRL on Jetson-based edge devices using our prototype system \textit{CoEdgeSys}, demonstrating its robustness and feasibility under resource constraints. Our code is available at:https://github.com/GalleyG5/LeDRL.git.

## 내 메모


