---
type: research-source
item_id: 177
title: "Teola: Towards End-to-End Optimization of LLM-based Applications"
source: "arxiv"
published: "2024-06-29T05:59:53Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3676641.3716278"
url: "https://arxiv.org/abs/2407.00326v3"
generated_by: codex-research-db
aliases:
  - "Teola: Towards End-to-End Optimization of LLM-based Applications"
topics:
  - "self-evolving-harness"
---

# Teola: Towards End-to-End Optimization of LLM-based Applications

[원문 열기](https://arxiv.org/abs/2407.00326v3)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`Q7FNSFTF`)
- 발행일: 2024-06-29T05:59:53Z
- 저자: Xin Tan, Yimin Jiang, Yitao Yang, Hong Xu
- 식별자: `doi:10.1145/3676641.3716278`

## 요약·초록

Large language model (LLM)-based applications consist of both LLM and non-LLM components, each contributing to the end-to-end latency. Despite great efforts to optimize LLM inference, end-to-end workflow optimization has been overlooked. Existing frameworks employ coarse-grained orchestration with task modules, which confines optimizations to within each module and yields suboptimal scheduling decisions. We propose fine-grained end-to-end orchestration, which utilizes task primitives as the basic units and represents each query's workflow as a primitive-level dataflow graph. This explicitly exposes a much larger design space, enables optimizations in parallelization and pipelining across primitives of different modules, and enhances scheduling to improve application-level performance. We build Teola, a novel orchestration framework for LLM-based applications that implements this scheme. Comprehensive experiments show that Teola can achieve up to 2.09x speedup over existing systems across various popular LLM applications. The code is available at https://github.com/NetX-lab/Ayo.

## 내 메모


