---
type: research-source
item_id: 100
title: "Towards COLREGs-aware ship collision avoidance with multi-agent PPO-LSTM in maritime IoT"
source: "openalex"
published: "2026-07-31"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:e54d4f9269134196635a194f1fa952e7446fdb7834ee2cec462214c665989110"
url: "https://openalex.org/W7169746535"
generated_by: codex-research-db
aliases:
  - "Towards COLREGs-aware ship collision avoidance with multi-agent PPO-LSTM in maritime IoT"
topics:
  - "ai-agents"
---

# Towards COLREGs-aware ship collision avoidance with multi-agent PPO-LSTM in maritime IoT

[원문 열기](https://openalex.org/W7169746535)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`7JEU8UDA`)
- 발행일: 2026-07-31
- 저자: Y. Ding, W. Meng, S. He, Weiwei Li
- 식별자: `url:e54d4f9269134196635a194f1fa952e7446fdb7834ee2cec462214c665989110`

## 요약·초록

Maritime Autonomous Surface Ships are expected to operate in a maritime IoT environment, where distributed sensing, V2V/AIS/VDES communication links, and electronic charts jointly support perception–decision–control loops for safe navigation in congested waters. A key challenge is to realise multi-ship collision avoidance that is consistent with the International Regulations for Preventing Collisions at Sea, while accounting for the limited manoeuvrability of large commercial vessels and the geometric constraints of ENC-derived chart-constrained narrow waterways. To address this problem, this work proposes a three-layer maritime IoT architecture in which each KVLCC2-class tanker is modelled as an IoT node, and ship states, TCPA/DCPA-based risk measures, and chart-derived environmental features are fused into a shared situational-awareness representation. On this basis, the task is formulated as a cooperative multi-agent partially observable Markov decision process, in which COLREGs encounter types, give-way/stand-on roles, and safety-domain constraints are embedded explicitly through the observation and reward design. A parameter-sharing recurrent multi-agent PPO–LSTM framework is then developed under the centralised-training-decentralised-execution paradigm, using a weakly centralised critic to handle partial observability and temporal coupling in dense multi-vessel interactions. The framework is evaluated in a unified simulation environment covering standard Imazu multi-vessel scenarios and an ENC-derived rasterised narrow-waterway case of Zhanjiang Bay, with comparisons against MA-PPO, MA-DDPG, and a classical VO baseline. Results show stronger convergence stability, higher mission success rates, larger closest-point-of-approach margins, and fewer COLREGs violations than the compared methods, while producing smooth and channel-conforming avoidance manoeuvres. Additional no-COLREG ablation and fixed-delay tests further clarify the roles of explicit rule-aware reward shaping and communication timeliness in cooperative multi-vessel collision avoidance.

## 내 메모


