---
type: research-source
item_id: 2334
title: "Meta$^n$: Recursive Self-Improvement through Emergent Depth"
source: "arxiv"
published: "2026-08-25T15:44:25Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.24735"
url: "https://arxiv.org/abs/2608.24735v1"
generated_by: codex-research-db
aliases:
  - "Meta$^n$: Recursive Self-Improvement through Emergent Depth"
topics:
  - "self-evolving-harness"
---

# Meta$^n$: Recursive Self-Improvement through Emergent Depth

[원문 열기](https://arxiv.org/abs/2608.24735v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-25T15:44:25Z
- 저자: Zae Myung Kim, Young-Jun Lee, Seungyeon Jwa, Dongyeop Kang
- 식별자: `arxiv:2608.24735`

## 요약·초록

Self-improving LLM agents refine answers, not the process that produces those answers. Systems that add a meta-level hold that level fixed, and those that edit themselves must leave part of their own editing machinery untouched to stay stable, capping the meta-depth they realize at roughly two. We present Meta$^n$, which keeps the meta-operation fixed and recurses on its input instead. That operation, $Ω$, is applied repeatedly to its own products, reading the traces of the solver stack below together with the code that produced them, then writing the next layer as a strategic pre-process and a library of callable helpers. Because $Ω$ never changes, it cannot destabilize the system, and because its input strictly grows, each layer reasons from a higher vantage than the last. Depth is set by convergence rather than fixed in advance, and an evolutionary archive searches over layer chains. Across two backbones, Meta$^n$ outperforms prior self-improving agents on all eight benchmark families. The sharpest case is ARC-AGI-2, built to resist skill memorization, where it alone scores above zero. Ablations indicate that most of the gain from recursion comes from the conditioning each layer passes to the next, and distinct layer roles emerge with depth although no prompt prescribes them. Code available at https://github.com/minnesotanlp/meta-n

## 내 메모
