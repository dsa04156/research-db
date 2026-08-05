---
type: research-source
item_id: 1725
title: "HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses"
source: "arxiv"
published: "2026-08-03T08:51:50Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01918"
url: "https://arxiv.org/abs/2608.01918v1"
generated_by: codex-research-db
aliases:
  - "HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses"
topics:
  - "self-evolving-harness"
---

# HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses

[원문 열기](https://arxiv.org/abs/2608.01918v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UDRK6NHN`)
- 발행일: 2026-08-03T08:51:50Z
- 저자: Luan Zhang, Ruochen Zhou, Dandan Song, Zhengyu Chen, Yuhang Tian, Jun Yang, Huipeng Ma, Chenhao Li, Guangyuan Feng, Xudong Li, Yizhou Jin, Yan Xu
- 식별자: `arxiv:2608.01918`

## 요약·초록

Harness design plays a critical role in agent performance by shaping how large language models (LLMs) perceive, reason over, and act within executable environments. Recent work has proposed automatic harness evolution, which iteratively improves the harness from agent--environment interactions. However, existing methods often overfit to the evolution tasks, rely exclusively on trajectory-derived signals, and optimize harness components jointly, causing interference across components. We propose HarnessCompass, a novel automatic harness evolution framework built around constrained evolution, proactive feedback, and component-wise optimization. HarnessCompass first enforces global constraints on evolution, restricting modifications to task-agnostic harness changes that generalize beyond the evolution tasks. It then augments trajectory-derived evidence with proactive first-person feedback from the agent about harness usage, yielding richer signals for evolution. Finally, it decouples the optimization of different harness components before consolidating them into a unified harness, reducing cross-component interference while preserving component synergy. On SWE-bench Verified with GPT-5.4, HarnessCompass improves Pass@1 from 54\% to 66\% in only 5 evolution iterations, outperforming AHE in both effectiveness and evolution efficiency. In addition, the evolved harness transfers effectively to held-out tasks and other models, demonstrating substantially stronger generalization than prior automatic harness evolution methods.

## 내 메모


