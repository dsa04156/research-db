---
type: research-source
item_id: 994
title: "SETA: Scaling Environments for Terminal Agents"
source: "arxiv"
published: "2026-07-12T19:40:27Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.10891"
url: "https://arxiv.org/abs/2607.10891v1"
generated_by: codex-research-db
aliases:
  - "SETA: Scaling Environments for Terminal Agents"
topics:
  - "self-evolving-harness"
---

# SETA: Scaling Environments for Terminal Agents

[원문 열기](https://arxiv.org/abs/2607.10891v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`T57QKWQE`)
- 발행일: 2026-07-12T19:40:27Z
- 저자: Qijia Shen, Zhiqi Huang, Vamsidhar Kamanuru, Aznaur Aliev, Jay Rainton, Ahmed Awelkair, Zhichen Zeng, Jiajun Li, Shi Dong, Yueming Yuan, Boyuan Ma, Qizheng Zhang, Jiwei Fu, Yuzhen Mao, Wendong Fan, Ping Nie, Philip Torr, Bernard Ghanem, Changran Hu, Jonathan Lingjie Li, Urmish Thakker, Guohao Li
- 식별자: `arxiv:2607.10891`

## 요약·초록

Large language models (LLMs) are rapidly shifting toward agents that solve tasks through diverse interfaces, including web and graphical user interfaces (GUIs). Among these, the terminal command line provides a text-based, general-purpose interface, covering tasks from system operations to data science and machine learning. However, scaling terminal-agent training remains challenging, as it requires diverse and coherent task instructions, executable environments, and reliable verification, while lacking naturally grounded supervision data. In this work, we propose SETA, a scalable framework for generating verifiable terminal environments for reinforcement learning (RL). The framework consists of two pipelines sharing a unified verification mechanism: SETA-Synth converts diverse sources into standardized RL environments, and SETA-Evol further expands from existing environments with adaptive control of difficulty and diversity. Together, we construct and release SETA-Env, the largest open-source verifiable terminal RL dataset to date, containing over 4,500 environments. We evaluate our dataset by training Qwen3-8B with GRPO on SETA-Env, achieving 12% pass rate on Terminal-Bench 2.0, the best reported result for an RL-trained model at the 8B scale. We further observe gains on DeepSeek-V4-Flash under the same terminal agent harness, with pass@1 on Terminal-Bench 2.0 improving from 40% to 43% and pass@5 improving from 54% to 58%. These results demonstrate that SETA- Env provides high-quality training environments for terminal agents and serves as a valuable resource for advancing research on terminal-based agent learning.

## 내 메모


