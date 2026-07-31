---
type: research-source
item_id: 15
title: "CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference"
source: "arxiv"
published: "2026-07-24T17:32:35Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.22511"
url: "https://arxiv.org/abs/2607.22511v1"
generated_by: codex-research-db
aliases:
  - "CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference"
topics:
  - "self-evolving-harness"
---

# CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference

[원문 열기](https://arxiv.org/abs/2607.22511v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`B27ERVCC`)
- 발행일: 2026-07-24T17:32:35Z
- 저자: Jiyuan Tan, Vasilis Syrgkanis
- 식별자: `arxiv:2607.22511`

## 요약·초록

Automating theoretical research is constrained not only by the generation of candidate results, but also by their reliable evaluation. A common approach is to close the research loop with a large language model (LLM) reviewer. However, such reviewers remain empirically unreliable: they may accept fabricated papers and detect them at rates close to chance (Bad Scientist, 2025). We present CausalForge, a framework for automated theoretical research in causal inference grounded in the Lean proof assistant. CausalForge combines Causalean, a foundational Lean library for causal inference containing 7,035 machine-checked declarations developed with language-model assistance under human design and review, with CausalSmith, a self-improving agentic pipeline that selects research topics, proposes results, formalizes statements, constructs proofs, and presents the resulting artifacts for human inspection. Because a machine-checked proof establishes only that a formal statement follows from its assumptions, not that the statement faithfully captures the intended scientific claim, the pipeline augments kernel verification with a statement audit that compares each formal theorem against the informal claim it is intended to express. We evaluate the system using artifacts produced by completed autonomous research runs. The source code, formal library, and run records are available at https://github.com/Jiyuan-Tan/CausalForge.

## 내 메모


