---
type: research-source
item_id: 2437
title: "Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification"
source: "arxiv"
published: "2026-08-27T16:12:23Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2608.27311"
url: "https://arxiv.org/abs/2608.27311v1"
generated_by: codex-research-db
aliases:
  - "Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification"
topics:
  - "self-evolving-harness"
---

# Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification

[원문 열기](https://arxiv.org/abs/2608.27311v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KPJAFP4X`)
- 발행일: 2026-08-27T16:12:23Z
- 저자: Jinghan Xu, Yikai Zhang, Aili Chen, Weiyuan Li, Jiaqing Liang, Deqing Yang
- 식별자: `doi:10.48550/arxiv.2608.27311`

## 요약·초록

Agent harnesses shape how language-model agents use instructions, tools, and runtime components, but adapting these harnesses requires costly verification. Existing propose-and-verify methods typically score every candidate on a fixed task set, wasting rollouts on unrelated behaviors and allowing aggregate scores to obscure specific regressions. We introduce HarnessLens, a budget-aware framework for automated harness evolution. HarnessLens jointly explores the task space and user-configurable components, derives candidate modifications from execution trajectories, and selectively verifies each candidate on behavior-relevant tasks using an attributable-evidence gate. Across three agent harnesses and four benchmarks, HarnessLens improves average held-out performance by 7.6-13.6% while consuming substantially less evaluation budget than competing baselines. These results demonstrate that behavior-aware verification with explicit attribution enables more reliable and sample-efficient harness evolution under constrained interaction budgets. Our code is available at https://github.com/jhxu5214/HarnessLens.

## 내 메모


