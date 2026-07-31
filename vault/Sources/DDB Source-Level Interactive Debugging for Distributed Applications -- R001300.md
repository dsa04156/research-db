---
type: research-source
item_id: 1300
title: "DDB: Source-Level Interactive Debugging for Distributed Applications"
source: "openalex"
published: "2026-07-07"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.06107"
url: "https://arxiv.org/abs/2607.06107"
generated_by: codex-research-db
aliases:
  - "DDB: Source-Level Interactive Debugging for Distributed Applications"
topics:
  - "cloud-infrastructure"
---

# DDB: Source-Level Interactive Debugging for Distributed Applications

[원문 열기](https://arxiv.org/abs/2607.06107)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`XUMHUNBF`)
- 발행일: 2026-07-07
- 저자: Yibo Yan, Junzhou He, Seo Jin Park
- 식별자: `arxiv:2607.06107`

## 요약·초록

Interactive debugging is an effective tool for understanding program behavior at the source level, allowing developers to pause execution, navigate the call stack, and inspect runtime state. However, interactive debuggers are designed for single-process execution, and interactive debugging has been widely considered impractical for distributed systems. Call stacks stop at process boundaries, debugging state fails to survive infrastructure dynamics, and, most critically, debugger-induced execution pauses trigger catastrophic timeout cascades that destroy the intended debug flow. Consequently, developers are forced to abandon live hypothesis testing in favor of unwieldy and iterative log-and-redeploy cycles. We present DDB, a source-level interactive debugger that extends interactive debugging capabilities to distributed applications. We show that each of these challenges admits a targeted solution. To bridge disjoint processes, Distributed Backtrace (DBT) embeds compact causality metadata in every RPC and reconstructs a unified call stack across RPC boundaries. To manage the lifecycle of a distributed session, an intent-preserving control plane automatically coordinates and propagates breakpoints across dynamic process sets. To make pausing safe, Pause-Erased Time (PET) virtualizes each process's clock, decoupling logical time from physical pauses and preventing timeout cascades. DDB integrates with an RPC framework in 20-60 lines of code. Evaluated on gRPC, ServiceWeaver, Nu, and Quicksand across up to 122 processes, DDB achieves 30ms median cross-RPC backtrace latency, sub-5 ms time jump under repeated execution pauses, and adds 1-5% throughput overhead, comparable to attaching a single-process debugger. In a controlled user study, DDB achieves a 100% fault localization success rate (compared to 38.5% for baseline tools) with a median localization time of ~8 minutes.

## 내 메모


