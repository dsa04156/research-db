---
type: research-source
item_id: 1127
title: "ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D"
source: "arxiv"
published: "2026-07-21T17:41:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19321"
url: "https://arxiv.org/abs/2607.19321v2"
generated_by: codex-research-db
aliases:
  - "ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D"
topics:
  - "ai-agents"
---

# ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D

[원문 열기](https://arxiv.org/abs/2607.19321v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6JF9FTGN`)
- 발행일: 2026-07-21T17:41:12Z
- 저자: Lena Libon, Ben Rank, Jehyeok Yeon, David Schmotz, Jeremy Qin, Daniel Donnelly, Derck Prinzhorn, Maksym Andriushchenko
- 식별자: `arxiv:2607.19321`

## 요약·초록

As AI agents begin to automate AI R&D, we need ways to assess whether their outputs are safe to deploy, even when the agents themselves may be untrusted. AI control offers one such approach: rather than trusting the agent, it treats it as a potential adversary and uses a monitor to detect covert sabotage before deployment. We evaluate AI control for automated AI R&D with ResearchArena, a framework spanning four long-horizon tasks: safety post-training, capabilities post-training, CUDA-kernel optimization, and inference-server optimization. Because the deliverable in AI R&D is an artifact that will be deployed and run, we pair each main task with two kinds of hidden side task: an embedded side task that sabotages the submitted model, adapter, kernel, or server itself, and an independent side task that takes a covert out-of-scope action in the sandbox while leaving the artifact honest. We evaluate frontier agents at both sabotage and monitoring, across four monitor types that vary along two axes: whether the monitor may execute and probe the produced artifact, and whether it sees the agent's chain-of-thought. We find that sabotage hidden in the training data is the hardest to catch, flagged fewer than half the time. Letting the monitor run experiments on the artifact, rather than only read the trajectory, helps, but it is not enough: monitors still miss embedded sabotage by inspecting only the surface, by noticing the anomaly but explaining it away, or by probing the artifact with the wrong test. We release ResearchArena as a modular framework for evaluating sabotage and control in automated AI R&D.

## 내 메모


