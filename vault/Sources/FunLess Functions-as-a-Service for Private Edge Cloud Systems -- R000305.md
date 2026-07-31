---
type: research-source
item_id: 305
title: "FunLess: Functions-as-a-Service for Private Edge Cloud Systems"
source: "arxiv"
published: "2024-05-31T16:47:42Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.21009"
url: "https://arxiv.org/abs/2405.21009v1"
generated_by: codex-research-db
aliases:
  - "FunLess: Functions-as-a-Service for Private Edge Cloud Systems"
topics:
  - "kubernetes"
---

# FunLess: Functions-as-a-Service for Private Edge Cloud Systems

[원문 열기](https://arxiv.org/abs/2405.21009v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`IXI3S4D5`)
- 발행일: 2024-05-31T16:47:42Z
- 저자: Giuseppe De Palma, Saverio Giallorenzo, Jacopo Mauro, Matteo Trentin, Gianluigi Zavattaro
- 식별자: `arxiv:2405.21009`

## 요약·초록

We present FunLess, a Function-as-a-Service (FaaS) platform tailored for the private edge cloud system. FunLess responds to recent trends that advocate for extending the coverage of serverless computing to private edge cloud systems and enhancing latency, security, and privacy while improving resource usage. Unlike existing solutions that rely on containers for function invocation, FunLess leverages WebAssembly (Wasm) as its runtime environment. Wasm's lightweight, sandboxed runtime is crucial to have functions run on constrained devices at the edge. Moreover, the advantages of using Wasm in FunLess include a consistent development and deployment environment for users and function portability (write once, run everywhere) We validate FunLess under different deployment scenarios, characterised by the presence/absence of constrained-resource devices (Raspberry Pi 3B+) and the (in)accessibility of container orchestration technologies - Kubernetes. We compare FunLess with three production-ready, widely adopted open-source FaaS platforms - OpenFaaS, Fission, and Knative. Our benchmarks confirm that FunLess is a proper solution for FaaS private edge cloud systems since it achieves performance comparable to the considered FaaS alternatives while it is the only fully-deployable alternative on constrained-resource devices, thanks to its small memory footprint.

## 내 메모


