---
type: research-source
item_id: 1721
title: "Global Optimization and Inference-Time Region Grafting for Agentic Workflows"
source: "arxiv"
published: "2026-08-03T15:04:26Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.02353"
url: "https://arxiv.org/abs/2608.02353v1"
generated_by: codex-research-db
aliases:
  - "Global Optimization and Inference-Time Region Grafting for Agentic Workflows"
topics:
  - "self-evolving-harness"
---

# Global Optimization and Inference-Time Region Grafting for Agentic Workflows

[원문 열기](https://arxiv.org/abs/2608.02353v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7DRABJB2`)
- 발행일: 2026-08-03T15:04:26Z
- 저자: Donghyeok Koh, Gyuwan Kim, Jinyeong Bak, Seung-Hoon Na, Tao Yang, Haneol Jang, Cheoneum Park
- 식별자: `arxiv:2608.02353`

## 요약·초록

Recent advances in agentic workflow optimization automate workflow design through task-specific workflow search or input-conditioned architecture selection. However, they determine the workflow before execution and cannot adapt failed workflow regions using execution-time label-free quality signals. Naively enabling such inference-time adaptation through whole-workflow re-optimization would be computationally prohibitive. To tackle this challenge, we introduce GRAFT, which preserves a globally optimized workflow while locally replacing only selected regions for each input. Without parameter training, GRAFT evaluates region-level alternatives using label-free execution-quality signals and accepts only replacements that improve local quality while preserving workflow-level consistency, thereby enabling instance-wise adaptation without whole-workflow re-optimization. GRAFT applies without modification across a range of tasks spanning mathematical reasoning, code generation, and multi-hop and knowledge-intensive question answering. Under matched optimizer and executor settings, it improves over the strongest prior workflow-optimization method, MaAS, by 3.85 points on average. Replacing only the executor with a stronger model yields further gains without re-optimizing the global workflow. This suggests that an optimized workflow is not merely a static optimization artifact, but an adaptable execution policy that can evolve with inference-time feedback and stronger executors.

## 내 메모


