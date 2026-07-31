---
type: research-source
item_id: 1629
title: "PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks"
source: "arxiv"
published: "2026-07-30T17:42:44Z"
first_seen: "2026-07-31"
review_status: "pending"
canonical_key: "arxiv:2607.28587"
url: "https://arxiv.org/abs/2607.28587v1"
generated_by: codex-research-db
aliases:
  - "PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks"
topics:
  - "ai-agents"
---

# PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks

[원문 열기](https://arxiv.org/abs/2607.28587v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-31|2026-07-31]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SMQWWE9W`)
- 발행일: 2026-07-30T17:42:44Z
- 저자: Manyi Wang, Junjielong Xu, Pinjia He
- 식별자: `arxiv:2607.28587`

## 요약·초록

SWE-bench-like benchmarks are widely used for evaluating LLM's issue resolution capability. They typically follow a common construction pipeline: each PR (Pull Request) is paired with its linked issue by extracting issue references from the PR description; the issue description is used as the problem statement, and the PR patch serves as the test oracle. However, due to the inherent complexity of developing and maintaining large repositories, such PR-Issue pairings are often misaligned in practice. In this work, we systematically study SWE-bench Verified instances, finding that 13.6% exhibit misalignment across five patterns in eleven fine-grained scenarios. To enable reliable and scalable construction of those benchmarks in the future, we propose PAIChecker, a multi-agent system for checking PR-Issue misalignment in SWE-bench-like benchmarks. Specifically, PAIChecker adopts a three-phase design that combines specific pattern identification, cross-agent label synthesis, and code-level validation, thereby enabling more accurate, generalizable, and progressively verified detection. Experiments on SWE-Gym and SWE-bench Multilingual show that PAIchecker achieves the best performance across all four LLM backbones, reaching up to 92.12% and 91.67% binary accuracy, respectively.

## 내 메모


