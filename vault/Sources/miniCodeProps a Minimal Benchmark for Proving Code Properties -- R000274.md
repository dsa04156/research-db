---
type: research-source
item_id: 274
title: "miniCodeProps: a Minimal Benchmark for Proving Code Properties"
source: "arxiv"
published: "2024-06-16T21:11:23Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.11915"
url: "https://arxiv.org/abs/2406.11915v2"
generated_by: codex-research-db
aliases:
  - "miniCodeProps: a Minimal Benchmark for Proving Code Properties"
topics:
  - "ai-agents"
---

# miniCodeProps: a Minimal Benchmark for Proving Code Properties

[원문 열기](https://arxiv.org/abs/2406.11915v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KV59SEVC`)
- 발행일: 2024-06-16T21:11:23Z
- 저자: Evan Lohn, Sean Welleck
- 식별자: `arxiv:2406.11915`

## 요약·초록

AI agents have shown initial promise in automating mathematical theorem proving in proof assistants such as Lean. The same proof assistants can be used to verify the correctness of code by pairing code with specifications and proofs that the specifications hold. Automating the writing of code, specifications, and proofs could lower the cost of verification, or, ambitiously, enable an AI agent to output safe, provably correct code. However, it remains unclear whether current neural theorem provers can automatically verify even relatively simple programs. We present miniCodeProps, a benchmark of 201 program specifications in the Lean proof assistant, aimed at the subproblem of automatically generating a proof for a provided program and specification. miniCodeProps contains specifications about simple, self-contained programs (e.g., lists, natural numbers, binary trees) with varied proof difficulty. Despite its simplicity, miniCodeProps is sufficient to break current LLM-based provers, with state-of-the-art methods showing promise on the easy properties in miniCodeProps, yet failing to prove nearly all of the medium and hard properties. We publicly release miniCodeProps as a benchmark for furthering automated theorem proving in the context of formally verified code.

## 내 메모


