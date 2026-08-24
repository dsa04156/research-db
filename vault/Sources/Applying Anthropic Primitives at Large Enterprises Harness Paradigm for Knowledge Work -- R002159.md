---
type: research-source
item_id: 2159
title: "Applying Anthropic Primitives at Large Enterprises: Harness Paradigm for Knowledge Work"
source: "arxiv"
published: "2026-08-20T23:44:52Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.20622"
url: "https://arxiv.org/abs/2608.20622v1"
generated_by: codex-research-db
aliases:
  - "Applying Anthropic Primitives at Large Enterprises: Harness Paradigm for Knowledge Work"
topics:
  - "self-evolving-harness"
---

# Applying Anthropic Primitives at Large Enterprises: Harness Paradigm for Knowledge Work

[원문 열기](https://arxiv.org/abs/2608.20622v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-20T23:44:52Z
- 저자: George Juraj Salapa
- 식별자: `arxiv:2608.20622`

## 요약·초록

Frontier models have collapsed the cost of writing custom code: a niche problem a specialist sees in their own domain now costs an afternoon. The cost of reviewing and maintaining that code hasn't collapsed. Each solution drifts from the next; understanding one means reading its codebase from scratch. Large enterprises build something centrally governed instead: at worst an off-the-shelf product, at best a graph-orchestration framework wired bespoke per use case, or a low-code platform used as the orchestrator. These are custom every time and limited in scope. Enterprises don't weigh a third option that escapes both constraints: the harness paradigm. Recent work treats the coding-agent harness as enterprise infrastructure rather than a coding tool, converging on three findings: harnesses suffice at the task level and outperform more elaborate architectures on enterprise work (arXiv:2604.00073, arXiv:2604.13107); harness choice accounts for most of the variance in agent benchmark results, more than model choice does (arXiv:2605.23950); and the gap between that finding and enterprise adoption is governance (arXiv:2605.10223, arXiv:2605.18747). We propose an architecture that closes that gap. One harness runs unmodified as the backbone; the code stays identical across every deployment, so reviewing what gets built collapses to reading its instructions file. Section 4 gives four mechanisms: credential-scoped tooling, where each backend gets one generic request tool and a scoped credential instead of a hand-built method; authorization logic outside the harness, so one artifact runs as a cron backbone, a chat-surface engine, and a terminal tool; registration is a side effect of pushing code, collapsing an audit a review of a text file. Built on microcc (<https://pypi.org/project/micro-cc/>), our reference harness.

## 내 메모


