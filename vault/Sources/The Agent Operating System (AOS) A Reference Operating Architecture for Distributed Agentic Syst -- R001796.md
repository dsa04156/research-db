---
type: research-source
item_id: 1796
title: "The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems"
source: "openalex"
published: "2026-08-04"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.03214"
url: "https://arxiv.org/abs/2608.03214"
generated_by: codex-research-db
aliases:
  - "The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems"
topics:
  - "cloud-infrastructure"
---

# The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems

[원문 열기](https://arxiv.org/abs/2608.03214)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`CUM6EP49`)
- 발행일: 2026-08-04
- 저자: Ankur Sharma, Deep Shah
- 식별자: `arxiv:2608.03214`

## 요약·초록

Large language models have transformed artificial intelligence from isolated prediction services into components of long-running, distributed systems that reason, invoke tools, retrieve external state, delegate tasks, and act on behalf of users and organizations. The surrounding ecosystem has responded with agent frameworks, workflow engines, model-serving platforms, memory systems, communication protocols, and observability tools. These technologies improve execution, but they do not provide a stable, implementation-independent operating architecture for governing intent, selecting capabilities, preserving authority across delegation, controlling uncertainty, coordinating runtime behavior, and reconstructing why consequential actions occurred. This paper proposes the Agent Operating System (AOS), a vendor-neutral reference operating architecture for distributed agentic systems. AOS contains two internal planes: a Control & Governance Plane responsible for intent, policy, trust, authority, confidence, auditability, observability, and human oversight; and a Runtime & Coordination Plane responsible for agent lifecycle, workflow coordination, model and tool routing, context and memory coordination, scheduling, traffic management, and runtime assurance. Platform services, Linux or Windows, container runtimes, and physical infrastructure remain outside the AOS boundary and are integrated through explicit interfaces. The paper specifies AOS concepts, invariants, interface objects, optimization objectives, deployment profiles, and reliability responsibilities. It also identifies tradeoffs and unresolved research questions. AOS is not presented as a replacement for existing frameworks or infrastructure; it is proposed as the operating architecture through which heterogeneous components can be composed into governable, reliable, observable, and interoperable agentic systems.

## 내 메모


