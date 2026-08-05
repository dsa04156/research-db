---
type: research-source
item_id: 1671
title: "PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents"
source: "arxiv"
published: "2026-08-02T03:20:54Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.00962"
url: "https://arxiv.org/abs/2608.00962v1"
generated_by: codex-research-db
aliases:
  - "PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents"
topics:
  - "ai-agents"
---

# PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents

[원문 열기](https://arxiv.org/abs/2608.00962v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZZT3B2NK`)
- 발행일: 2026-08-02T03:20:54Z
- 저자: Jingyu Sun, Yan Lin, Yuyang Xue, Yifan Wang, Zhengtao Yao, Rui Qian, Zefeng Xu, Jiachen Li, Xianyang Liu, Jiancheng Pan, Jingyuan Sun, Syed Murtuza Baker, Hongpeng Zhou
- 식별자: `arxiv:2608.00962`

## 요약·초록

Long-term memory is essential for LVLM agents to maintain consistency and integrate information across extended multimodal interactions. Existing agent memory systems, however, often reduce visual experiences into textual summaries or rely on static retrieve-then-reason pipelines, which are inefficient at query time and brittle when questions require image-text binding, temporal updates, or visual details. We propose Prospective Multimodal Memory Compilation, a framework that shifts part of the memory reasoning process from query time to memory consolidation time. Given accumulated multimodal interactions, a Questioner predicts future question candidates, a Planner compiles question-conditioned multimodal memory programs, and a Doubter verifies whether the planned evidence path can support the predicted answer. The verified question-program pairs form a structured question bank for efficient query-time routing and evidence retrieval. Experiments on multimodal long-term memory benchmarks show that our method improves answer quality and visual evidence recall while reducing query-time token and latency costs. Extensive ablations analyze the effects of self-feedback, dynamic planning, raw-image access, and question bank coverage.

## 내 메모


