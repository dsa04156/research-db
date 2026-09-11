---
type: research-source
item_id: 2739
title: "Can AI Agents Deliver Verifiable Network-Wide Outcomes Across Authority Boundaries?"
source: "arxiv"
published: "2026-09-09T13:51:15Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.10181"
url: "https://arxiv.org/abs/2609.10181v1"
generated_by: codex-research-db
aliases:
  - "Can AI Agents Deliver Verifiable Network-Wide Outcomes Across Authority Boundaries?"
topics:
  - "ai-agents"
---

# Can AI Agents Deliver Verifiable Network-Wide Outcomes Across Authority Boundaries?

[원문 열기](https://arxiv.org/abs/2609.10181v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`CI2PTM8U`)
- 발행일: 2026-09-09T13:51:15Z
- 저자: Tianzhu Zhang, Chih-Kai Huang, Meikang Qiu
- 식별자: `arxiv:2609.10181`

## 요약·초록

AI agents are increasingly involved in network automation, where they can initiate configuration changes through mediated operational interfaces and assess the resulting state. Nonetheless, operational networks usually span many devices and administrative domains. Realizing an operator's intent requires coordinating agents with distinct authority scopes that define the resources they can access, the operations they can invoke, and the network state they can observe. This division limits the blast radius of an erroneous action but fragments the evidence needed to assess the network-wide outcome. Successful execution of a configuration action proposed by one agent does not establish that remote devices responded as intended or that routing changes reached the required devices. A valid observation may also become stale after a subsequent change. Before the coordinated operation can be declared complete, a trusted assurance layer must collect current observations from the required scopes and determine whether they collectively support the operator's intended network-wide outcome. To address the completion admission problem, we present EvidenceNet, a runtime assurance layer for deciding whether coordinated agent operations have achieved an operator's network intent. Its broker collects the post-change observations required by a completion contract, and its admission gate checks that the evidence comes from the required scopes, remains current, and satisfies the task rules. A verifier agent provides an additional assessment of the observation content. Experiments on live routing networks show that post-change state checks recognize successful outcomes that configuration-action records alone cannot establish. Controlled interventions further show that EvidenceNet rejects completion when otherwise satisfactory observations have the wrong source, have been substituted, or are stale.

## 내 메모


