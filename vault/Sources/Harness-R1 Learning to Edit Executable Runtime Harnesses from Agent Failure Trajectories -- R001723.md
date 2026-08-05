---
type: research-source
item_id: 1723
title: "Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories"
source: "arxiv"
published: "2026-08-03T14:12:18Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.02276"
url: "https://arxiv.org/abs/2608.02276v1"
generated_by: codex-research-db
aliases:
  - "Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories"
topics:
  - "self-evolving-harness"
---

# Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories

[원문 열기](https://arxiv.org/abs/2608.02276v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`X4XP6WWP`)
- 발행일: 2026-08-03T14:12:18Z
- 저자: Shuai Shao, Kangning Zhang, Qingyao Li, Shijian Wang, Hao Wang, Wenxiang Jiao, Yuan Lu, Yi Guo, Weiwen Liu, Weinan Zhang
- 식별자: `arxiv:2608.02276`

## 요약·초록

Agents built around large language models continually accumulate interaction trajectories during deployment, yet their behavior typically remains fixed. Beyond updating model weights, these trajectories can improve the agent harness that constructs context, mediates tools, validates actions, and recovers execution. We introduce Harness-R1, the first method, to our knowledge, that makes failure-conditioned, lifecycle-wide editing of an existing executable runtime a learned capability. It post-trains a dedicated harness engineer with online reinforcement learning so that its edits are optimized for the realized task success they produce, rather than proposed by a fixed editor. A separate 9B engineer converts batches of target-agent failures into validated executable patches; fresh same-batch reruns of the frozen target provide outcome rewards, so training updates only the engineer. Cold-start supervised fine-tuning initializes this editing policy, which is then trained online with group-relative policy optimization. Across WebShop, ALFWorld, and DBBench, Harness-R1 raises vanilla Qwen3.5-9B success from 44.3% to 53.6% (+9.3 percentage points). After direct target-agent fine-tuning, a target-specific engineer raises the average further from 59.2% to 64.2% (+5.0 points); because these gains hold both before and after fine-tuning the target, Harness-R1 points toward co-evolving the harness engineer and the target agent.

## 내 메모


