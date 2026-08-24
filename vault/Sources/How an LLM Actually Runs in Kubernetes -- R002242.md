---
type: research-source
item_id: 2242
title: "How an LLM Actually Runs in Kubernetes"
source: "web:Cracking Walnuts"
published: "2026-08-23"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "url:1dc142c68a0eba196b4e613ba59962a01bd798012804d386ffe2f85334a491cf"
url: "https://crackingwalnuts.com/post/how-an-llm-actually-runs-in-kubernetes"
generated_by: codex-research-db
aliases:
  - "How an LLM Actually Runs in Kubernetes"
topics:
  - "kubernetes"
---

# How an LLM Actually Runs in Kubernetes

[원문 열기](https://crackingwalnuts.com/post/how-an-llm-actually-runs-in-kubernetes)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `web:Cracking Walnuts`
- 검토 상태: `pending`
- 발행일: 2026-08-23
- 식별자: `url:1dc142c68a0eba196b4e613ba59962a01bd798012804d386ffe2f85334a491cf`

## 요약·초록

Kubernetes 위 LLM 서빙에서 일반 Service 라우팅만으로는 KV·prefix cache, 대기 토큰량, prefill/decode 분리를 반영할 수 없다고 설명한다. vLLM, llm-d, tensor parallelism, NIXL/RDMA, tenant isolation을 한 요청 경로로 연결한 독립 기술 해설이다.

## 내 메모


