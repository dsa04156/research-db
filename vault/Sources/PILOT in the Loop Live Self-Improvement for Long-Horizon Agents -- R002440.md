---
type: research-source
item_id: 2440
title: "PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents"
source: "openalex"
published: "2026-08-27"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2608.26530"
url: "https://arxiv.org/abs/2608.26530"
generated_by: codex-research-db
aliases:
  - "PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents"
topics:
  - "ai-agents"
---

# PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents

[원문 열기](https://arxiv.org/abs/2608.26530)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`X9INNZPZ`)
- 발행일: 2026-08-27
- 저자: Yang Xiao, Yusong Sun, Haoyi Wu, Wenyang Hui, Wen Da, Zhaokai Luo, Mu Chuan, Yao Hu, Wenjie Li, Chengyue Jiang
- 식별자: `doi:10.48550/arxiv.2608.26530`

## 요약·초록

Long-horizon agent runs generate experience that can improve both the current run and future work. Most self-improvement methods process this experience only after execution ends, so they cannot redirect the active run or immediately apply and validate lessons learned from it. We argue that self-improvement should instead be live, using emerging experience both to redirect the active run and to update the persistent harness. Existing agent architectures do not fully support this goal. Single-agent self-correction combines task execution and trajectory assessment within one context, while subagent delegation separates execution but typically cannot redirect an active subagent. We present PILOT, a supervisor-worker harness for live self-improvement through two coupled mechanisms: (1) live steering lets a separate supervisor redirect or abort the active worker during execution; and (2) live self-evolution distils procedures and failure modes revealed during execution into reusable skills and memory. Across two frozen backbones and three benchmarks, PILOT ranks first in five of six configurations. On Terminal-Bench 2.0, PILOT outperforms counterpart harnesses by up to 9.8 percentage points. In the self-improvement setting, PILOT gains 14.6 points with GLM-5.1 and 12.4 points with Kimi-K2.6. Mean output tokens fall by 42.9% and 47.4%, while successful evaluations per million output tokens rise by 110.3% and 134.0%, respectively.

## 내 메모


