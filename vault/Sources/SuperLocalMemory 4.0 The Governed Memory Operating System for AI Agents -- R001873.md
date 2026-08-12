---
type: research-source
item_id: 1873
title: "SuperLocalMemory 4.0: The Governed Memory Operating System for AI Agents"
source: "arxiv"
published: "2026-08-08T17:26:58Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.08253"
url: "https://arxiv.org/abs/2608.08253v1"
generated_by: codex-research-db
aliases:
  - "SuperLocalMemory 4.0: The Governed Memory Operating System for AI Agents"
topics:
  - "ai-agents"
---

# SuperLocalMemory 4.0: The Governed Memory Operating System for AI Agents

[원문 열기](https://arxiv.org/abs/2608.08253v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZHPF7A5E`)
- 발행일: 2026-08-08T17:26:58Z
- 저자: Varun Pratap Bhardwaj, Garima Singh, Arun Pratap Bhardwaj
- 식별자: `arxiv:2608.08253`

## 요약·초록

AI agents are becoming shared infrastructure, yet durable memory is commonly assembled from separate retrieval, governance, and operational components. We present SuperLocalMemory 4.0, a governed, local-first memory operating system for AI agents. The system combines dense semantic, BM25 lexical, temporal, Hopfield-associative, and spreading-activation retrieval through reciprocal-rank fusion; a governed learning and behaviour layer; bi-temporal recall; multi-scope personal, shared, and global memory; role-based access control; GDPR-oriented export and verified erasure; audit trails; and a deployment-context EU AI Act checklist. V4 introduces a reliability spine for its primary write path: generation-fenced admission, a policy registry, verifiable memory transactions with per-projection apply, verify, compensate, and erase owners, and hash-checkable completion manifests. The runtime is available through CLI, MCP, an HTTP daemon, a dashboard, editor integration, and framework adapters, and supports fully local, local-with-on-device-model, and provider-assisted modes. We evaluate eleven fault-injection and mechanism scenarios, each repeated 200 times. The released evidence bundle reports 2,200 of 2,200 deterministic repetitions upholding their scoped component properties. The governed write envelope measured 3.522 ms at p50 and 5.297 ms at p99, versus 1.835 ms and 2.569 ms for the ungoverned baseline, corresponding to in-process control-plane overheads of 1.687 ms at p50 and 2.728 ms at p99. These are scoped component and mechanism measurements, not an end-to-end multi-process or external retrieval-accuracy benchmark. The paper consolidates prior SuperLocalMemory work on privacy-preserving multi-agent memory, information-geometric retrieval, and the V3.3 Living Brain lifecycle.

## 내 메모


