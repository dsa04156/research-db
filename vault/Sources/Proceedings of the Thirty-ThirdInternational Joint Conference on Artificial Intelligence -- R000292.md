---
type: research-source
item_id: 292
title: "Proceedings of the Thirty-ThirdInternational Joint Conference on Artificial Intelligence"
source: "openalex"
published: "2024-07-26"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.24963/ijcai.2024"
url: "https://doi.org/10.24963/ijcai.2024"
generated_by: codex-research-db
aliases:
  - "Proceedings of the Thirty-ThirdInternational Joint Conference on Artificial Intelligence"
topics:
  - "ai-agents"
---

# Proceedings of the Thirty-ThirdInternational Joint Conference on Artificial Intelligence

[원문 열기](https://doi.org/10.24963/ijcai.2024)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`MQES52BM`)
- 발행일: 2024-07-26
- 식별자: `doi:10.24963/ijcai.2024`

## 요약·초록

Markov Decision Processes (MDPs) are a classical model for decision making in the presence of uncertainty.Often they are viewed as state transformers with planning objectives defined with respect to paths over MDP states.An increasingly popular alternative is to view them as distribution transformers, giving rise to a sequence of probability distributions over MDP states.For instance, reachability and safety properties in modeling robot swarms or chemical reaction networks are naturally defined in terms of probability distributions over states.Verifying such distributional properties is known to be hard and often beyond the reach of classical state-based verification techniques.In this work, we consider the problems of certified policy (i.e.controller) verification and synthesis in MDPs under distributional reach-avoidance specifications.By certified we mean that, along with a policy, we also aim to synthesize a (checkable) certificate ensuring that the MDP indeed satisfies the property.Thus, given the target set of distributions and an unsafe set of distributions over MDP states, our goal is to either synthesize a certificate for a given policy or synthesize a policy along with a certificate, proving that the target distribution can be reached while avoiding unsafe distributions.To solve this problem, we introduce the novel notion of distributional reach-avoid certificates and present automated procedures for (1) synthesizing a certificate for a given policy, and (2) synthesizing a policy together with the certificate, both providing formal guarantees on certificate correctness.Our experimental evaluation demonstrates the ability of our method to solve several non-trivial examples, including a multi-agent robot-swarm model, to synthesize certified policies and to certify existing policies.

## 내 메모


