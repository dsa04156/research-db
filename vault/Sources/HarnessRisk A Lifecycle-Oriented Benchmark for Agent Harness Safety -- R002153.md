---
type: research-source
item_id: 2153
title: "HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety"
source: "kurate"
published: "2026-08-18T10:03:58Z"
first_seen: "2026-08-20"
review_status: "pending"
canonical_key: "arxiv:2608.17597"
url: "http://arxiv.org/abs/2608.17597v1"
generated_by: codex-research-db
aliases:
  - "HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety"
topics:
  - "self-evolving-harness"
---

# HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety

[원문 열기](http://arxiv.org/abs/2608.17597v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-20|2026-08-20]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- 발행일: 2026-08-18T10:03:58Z
- 저자: Yajing Bai, Jinhao Duan, Jie Peng, Xianfeng Wu, Sijia Liu, Song Wang, Tianlong Chen
- 식별자: `arxiv:2608.17597`

## 요약·초록

Large language models are increasingly deployed through agent harnesses that manage tools, extensions, persistent state, permissions, and external actions. Existing safety benchmarks mainly target individual attack mechanisms or a limited subset of operational settings, making it difficult to compare how safety failures emerge across different harness responsibilities. We present HarnessRisk, a lifecycle oriented benchmark that organizes agent harness safety into six operational phases including Harness Configuration, Capability Extension, Runtime Operation, State Persistence, Action Control, and Incident Recovery. HarnessRisk contains 128 sandboxed cases, each pairing a benign user objective with an adversarial instruction embedded in an untrusted workflow artifact. We evaluate each trajectory using Utility, Attack Success Rate, Persistence, and Detection. Across three harnesses, six language models, and 14 model and harness configurations, attack success ranges from 12.6% to 80.9%, while Utility remains between 75.0% and 97.6%. Harness Configuration is the most vulnerable phase across all three harnesses, showing that attacks can succeed by altering security sensitive parameters within otherwise authorized workflows. We also find that explicit risk recognition does not reliably lead to safe action, as some configurations detect risks in more than 90% of runs while retaining substantial attack success. These results highlight the need to evaluate agent safety across multiple harness responsibilities and at the level of the deployed model and harness configuration.

## 내 메모


