---
type: research-source
item_id: 885
title: "Ludax: A GPU-Accelerated Domain Specific Language for Board Games"
source: "arxiv"
published: "2025-06-27T20:15:53Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2506.22609"
url: "https://arxiv.org/abs/2506.22609v2"
generated_by: codex-research-db
aliases:
  - "Ludax: A GPU-Accelerated Domain Specific Language for Board Games"
topics:
  - "edge-computing"
---

# Ludax: A GPU-Accelerated Domain Specific Language for Board Games

[원문 열기](https://arxiv.org/abs/2506.22609v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GB7APS7X`)
- 발행일: 2025-06-27T20:15:53Z
- 저자: Graham Todd, Alexander G. Padula, Dennis J. N. J. Soemers, Julian Togelius
- 식별자: `arxiv:2506.22609`

## 요약·초록

Games have long been used as benchmarks and testing environments for research in artificial intelligence. A key step in supporting this research was the development of game description languages: frameworks that compile domain-specific code into playable and simulatable game environments, allowing researchers to generalize their algorithms and approaches across multiple games without having to manually implement each one. More recently, progress in reinforcement learning (RL) has been largely driven by advances in hardware acceleration. Libraries like JAX allow practitioners to take full advantage of cutting-edge computing hardware, often speeding up training and testing by orders of magnitude. Here, we present a synthesis of these strands of research: a domain-specific language for board games which automatically compiles into hardware-accelerated code. Our framework, Ludax, combines the generality of game description languages with the speed of modern parallel processing hardware and is designed to fit neatly into existing deep learning pipelines. We envision Ludax as a tool to help accelerate games research generally, from RL to cognitive science, by enabling rapid simulation and providing a flexible representation scheme. We present a detailed breakdown of Ludax's description language and technical notes on the compilation process, along with speed benchmarking and a demonstration of training RL agents. The Ludax framework, along with implementations of existing board games, is open-source and freely available.

## 내 메모


