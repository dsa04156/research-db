---
type: research-source
item_id: 1147
title: "Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes"
source: "arxiv"
published: "2026-06-18T17:36:46Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.20520"
url: "https://arxiv.org/abs/2606.20520v2"
generated_by: codex-research-db
aliases:
  - "Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes"
topics:
  - "kubernetes"
---

# Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes

[원문 열기](https://arxiv.org/abs/2606.20520v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HKIZ4B3G`)
- 발행일: 2026-06-18T17:36:46Z
- 저자: Jun He, Deying Yu
- 식별자: `arxiv:2606.20520`

## 요약·초록

Autonomous agents are increasingly connected to cloud, deployment, and data-control workflows, but production mutation authority should not reside inside non-deterministic reasoning processes. Existing access-control mechanisms authorize identities, while assurance layers certify proposed actions; neither alone provides a mandatory enforcement point for certified authority at the moment of mutation. This paper introduces the Sovereign Execution Broker (SEB), a runtime enforcement boundary for certificate-bound agentic infrastructure. SEB consumes certificates issued by the Sovereign Assurance Boundary (SAB), verifies that the requested mutation matches the certified execution contract, checks validity windows, policy epochs, revocation epochs, and live-state drift, mints scoped execution identity, invokes infrastructure APIs, and records signed decision and outcome records. By separating proposal, admission, and execution, SEB turns certified authority into a short-lived, revocable, auditable runtime capability, provided that production mutation APIs reject non-broker identities. We present the SEB execution model, certificate and replay-verification predicates, scoped identity semantics, bypass-prevention deployment patterns, failure behavior, and a concrete prototype implementation. We evaluate the prototype on AWS and Kubernetes clusters, measuring latency overheads, revocation propagation, drift detection, and security under fault injection.

## 내 메모


