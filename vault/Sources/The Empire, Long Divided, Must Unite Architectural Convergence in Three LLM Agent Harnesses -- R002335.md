---
type: research-source
item_id: 2335
title: "The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses"
source: "arxiv"
published: "2026-08-25T01:26:41Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.23953"
url: "https://arxiv.org/abs/2608.23953v1"
generated_by: codex-research-db
aliases:
  - "The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses"
topics:
  - "self-evolving-harness"
---

# The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses

[원문 열기](https://arxiv.org/abs/2608.23953v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`K9529FXN`)
- 발행일: 2026-08-25T01:26:41Z
- 저자: Dai Jiahong
- 식별자: `arxiv:2608.23953`

## 요약·초록

An agent harness is what turns a language model into an autonomous agent: the surrounding code that builds the model's context, mediates its tools, runs the loop, and persists state across a long-horizon run. This layer, not the model it wraps, is increasingly the binding constraint on agent behaviour. We present a source-level, multi-case study of three open coding-agent harnesses built from deliberately opposing philosophies: LangChain's deepagents (batteries-included), Earendil's pi (radical minimalism), and DeepSeek's dsh (everything-is-a-plugin). Reading each at a pinned commit and following its commit history, we find that the two mature harnesses have travelled in opposite directions (deepagents subtracting authored scaffolding, pi accreting durable infrastructure), yet converged toward one architectural middle form of five recurring elements: a commoditised loop, an append-only replayable session record, model quirks kept as data, progressive disclosure of context, and explicit extension seams. A third harness, read afterward as a held-out check, exhibits all five, and in one seam reuses another's implementation outright. We therefore do not claim independent invention, and decompose the convergence into parallel discovery, diffusion, and literal reuse. Finally, one load-bearing dimension shows no convergence, and indeed no presence: external verifiability, a tamper-evident record an outside party can check without trusting the runtime. We read this absence not as an oversight but as a predictive gap, the next axis on which harnesses for provenance-sensitive domains will differ.

## 내 메모


