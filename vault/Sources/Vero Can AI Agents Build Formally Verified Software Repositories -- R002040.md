---
type: research-source
item_id: 2040
title: "Vero: Can AI Agents Build Formally Verified Software Repositories?"
source: "kurate"
published: "2026-08-13T17:41:27Z"
first_seen: "2026-08-18"
review_status: "pending"
canonical_key: "arxiv:2608.13522"
url: "http://arxiv.org/abs/2608.13522v1"
generated_by: codex-research-db
aliases:
  - "Vero: Can AI Agents Build Formally Verified Software Repositories?"
topics:
  - "ai-agents"
---

# Vero: Can AI Agents Build Formally Verified Software Repositories?

[원문 열기](http://arxiv.org/abs/2608.13522v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-18|2026-08-18]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- Zotero: created (`NPHGZDNI`)
- 발행일: 2026-08-13T17:41:27Z
- 저자: Zhe Ye, Hantao Lou, Yuechun Sun, Peiyang Song, Zhengxu Yan, Timothe Kasriel, Qingyang Zhang, Kaiyu Yang
- 식별자: `arxiv:2608.13522`

## 요약·초록

AI agents are increasingly used for programming, but do not provide any guarantee on the correctness of generated code. Verified code generation, in which an agent produces both an implementation and a machine-checked proof of its specification, offers a stronger path toward trustworthy AI-generated software. Existing benchmarks in this direction either focus on individual functions or only evaluate proof generation with provided implementations. It is still an open question whether agents can make coherent implementation and proof choices across real multi-module codebases. To bridge this gap, we introduce Vero, the first benchmark to evaluate joint implementation and proof synthesis at the repository level. Vero contains 43 multi-module instances sourced from real-world repositories spanning Python, Dafny, Verus, and Coq, and covering diverse domains from cryptographic protocols to distributed systems. Each instance consists of a multi-module Lean 4 repository with predetermined API interfaces, manually curated formal specifications, and reference implementations, supporting both proof-only and code-and-proof evaluation modes. To improve benchmark reliability, Vero also includes an audit mechanism where agents are allowed to formally prove unsatisfiability of provided specification or incorrectness of reference code, which surfaces and corrects latent code and specification errors during curation. We evaluate frontier coding-agent configurations with Lean toolchain access. The strongest agent fully solves only 27 of 43 instances and closes no specifications on the hardest repositories. Vero provides a concrete testbed for measuring progress toward repository-scale verified software synthesis, where current agents still fall short. We release the benchmark, curation pipeline, and evaluation harness at https://github.com/sunblaze-ucb/vero.

## 내 메모


