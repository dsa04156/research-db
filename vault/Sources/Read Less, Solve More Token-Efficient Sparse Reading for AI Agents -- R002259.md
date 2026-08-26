---
type: research-source
item_id: 2259
title: "Read Less, Solve More: Token-Efficient Sparse Reading for AI Agents"
source: "arxiv"
published: "2026-08-23T06:24:26Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.22237"
url: "https://arxiv.org/abs/2608.22237v1"
generated_by: codex-research-db
aliases:
  - "Read Less, Solve More: Token-Efficient Sparse Reading for AI Agents"
topics:
  - "ai-agents"
---

# Read Less, Solve More: Token-Efficient Sparse Reading for AI Agents

[원문 열기](https://arxiv.org/abs/2608.22237v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`BBP2MPZJ`)
- 발행일: 2026-08-23T06:24:26Z
- 저자: Zedong Liu, Jiaan Wu, Xinyang Ma, Le Xu, Kai Wang, Yuanchao Hu, Dingwen Tao, Guangming Tan
- 식별자: `arxiv:2608.22237`

## 요약·초록

Long-horizon agents increasingly rely on repeated access to external artifacts, yet current reading interfaces often expose entire objects even when only sparse evidence is needed. This over-reading increases token and latency costs and can dilute task-relevant evidence, while existing context-reduction methods mainly intervene after broad content has already entered the trajectory. We present SparseRead, a training-free, model-transparent reading layer that controls content admission before unnecessary evidence reaches the model context. SparseRead combines a regime-aware Read Gate, extensible Reader Backends, and a stateful protocol for bounded, source-anchored evidence acquisition with explicit refinement, verification, stopping, and fallback. Across six frontier models, including Claude Opus 5, and five workload scenarios, SparseRead reduces token volume by up to 92.9% and wall time by up to 89.0%, while preserving or improving task quality. Its consistent gains across three agent frameworks further demonstrate broad portability.

## 내 메모
