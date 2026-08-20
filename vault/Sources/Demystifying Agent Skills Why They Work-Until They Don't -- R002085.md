---
type: research-source
item_id: 2085
title: "Demystifying Agent Skills: Why They Work-Until They Don't"
source: "arxiv"
published: "2026-08-14T07:26:38Z"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.14036"
url: "https://arxiv.org/abs/2608.14036v1"
generated_by: codex-research-db
aliases:
  - "Demystifying Agent Skills: Why They Work-Until They Don't"
topics:
  - "self-evolving-harness"
---

# Demystifying Agent Skills: Why They Work-Until They Don't

[원문 열기](https://arxiv.org/abs/2608.14036v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`EMAW7KVM`)
- 발행일: 2026-08-14T07:26:38Z
- 저자: Zhiyuan Jiang, Fangrui Huang, Hanwen Xing, Xander Wu, Yipeng Gao, Rui Cao, Mengdi Wang, Shilong Liu, Yijiang Li
- 식별자: `arxiv:2608.14036`

## 요약·초록

Skills have emerged as a practical and effective approach for enhancing LLM agents at inference time through structured packages of knowledge. However, existing evaluations largely measure whether skills improve aggregated task success, leaving a more fundamental question underexplored: \emph{\textbf{When do skills help, why do they work, and where do they fail?}} Through controlled experiments across various benchmarks, agent harnesses and LLMs, we isolate the effects of representation, outcome annotation, retrieval difficulty, and cross-framework robustness of skills. To further answer this question, we design a contrastive study that combines controlled quantitative experiments with paired trajectory analysis. We normalize 8,135 trial records from controlled experiments and retain 238 valid unique labels from 240 open-coded records. We consolidate these observations into a taxonomy of three high-level categories and twelve skill-use modes: skills work when noisy trajectories become procedural anchors that stabilize execution. Skills improve over Workflow Memory by 6.06 points in matched comparisons. Procedural anchoring accounts for 65.7\% of skill cases, versus 4.5\% for explicit knowledge injection, showing that skills stabilize action rather than inject missing facts. Retrieval is a separate bottleneck: as pools grow from 5 to 100, actual-use precision falls from 29.6\% to 3.3\%. Confusable distractors impair offline identification, yet downstream success remains stable; exact ground-truth invocation is neither sufficient nor necessary. Skills fail under brittle assumptions, incompatible contexts, or insufficient adaptation. These findings move evaluation beyond aggregate success rates and guide reliable self-evolving agents.

## 내 메모


