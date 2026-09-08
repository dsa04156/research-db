---
type: research-source
item_id: 2607
title: "Environment Evolution for Terminal Agents"
source: "arxiv"
published: "2026-09-03T17:26:33Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.04128"
url: "https://arxiv.org/abs/2609.04128v1"
generated_by: codex-research-db
aliases:
  - "Environment Evolution for Terminal Agents"
topics:
  - "self-evolving-harness"
---

# Environment Evolution for Terminal Agents

[원문 열기](https://arxiv.org/abs/2609.04128v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T17:26:33Z
- 저자: Zhiyuan Fan, Tinghao Yu, Yuanjun Cai, Jiang Zhou, Jiangtao Guan, Jincheng Liu, Yun Yang, Dingxin Hu, Zhuo Han, Xing Wu, Feng Zhang, Lilin Wang
- 식별자: `arxiv:2609.04128`

## 요약·초록

Scaling interactive and verifiable environments is critical for training terminal agents. As frontier models become more capable, environments synthesized from scratch become less challenging and thus provide limited learning signals. Recent co-evolution methods iteratively synthesize environments near the model's learnable frontier based on weaknesses exposed during rollouts. However, their dependence on on-policy rollouts limits generalization and the continuous provision of learning signals as the model becomes stronger. In this paper, we propose environment evolution, which incrementally increases environment difficulty off-policy and schedules the evolved environments generation by generation during training to provide continuous learning signals. We derive three evolution directions that influence environment difficulty from the multi-turn learning objective and then implement evolution along these directions through a loop-engineered multi-agent harness. Quantitative rollout experiments with Hy4 preview, Claude Opus 5, and GPT-5.6 Sol show that environment evolution consistently produces more difficult environments. We validate its effectiveness on Qwen3.6-27B and Qwen3.6-35B-A3B through simple long-horizon RL training, improving their performance by 14.4 and 18.0 percentage points on Terminal-Bench 2.1, respectively.

## 내 메모


