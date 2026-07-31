---
type: research-source
item_id: 221
title: "Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities"
source: "arxiv"
published: "2024-07-10T16:08:46Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.07791"
url: "https://arxiv.org/abs/2407.07791v2"
generated_by: codex-research-db
aliases:
  - "Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities"
topics:
  - "ai-agents"
---

# Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities

[원문 열기](https://arxiv.org/abs/2407.07791v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3HTVW2DK`)
- 발행일: 2024-07-10T16:08:46Z
- 저자: Tianjie Ju, Yiting Wang, Xinbei Ma, Pengzhou Cheng, Haodong Zhao, Yulong Wang, Lifeng Liu, Jian Xie, Zhuosheng Zhang, Gongshen Liu
- 식별자: `arxiv:2407.07791`

## 요약·초록

The rapid adoption of large language models (LLMs) in multi-agent systems has highlighted their impressive capabilities in various applications, such as collaborative problem-solving and autonomous negotiation. However, the security implications of these LLM-based multi-agent systems have not been thoroughly investigated, particularly concerning the spread of manipulated knowledge. In this paper, we investigate this critical issue by constructing a detailed threat model and a comprehensive simulation environment that mirrors real-world multi-agent deployments in a trusted platform. Subsequently, we propose a novel two-stage attack method involving Persuasiveness Injection and Manipulated Knowledge Injection to systematically explore the potential for manipulated knowledge (i.e., counterfactual and toxic knowledge) spread without explicit prompt manipulation. Our method leverages the inherent vulnerabilities of LLMs in handling world knowledge, which can be exploited by attackers to unconsciously spread fabricated information. Through extensive experiments, we demonstrate that our attack method can successfully induce LLM-based agents to spread both counterfactual and toxic knowledge without degrading their foundational capabilities during agent communication. Furthermore, we show that these manipulations can persist through popular retrieval-augmented generation frameworks, where several benign agents store and retrieve manipulated chat histories for future interactions. This persistence indicates that even after the interaction has ended, the benign agents may continue to be influenced by manipulated knowledge. Our findings reveal significant security risks in LLM-based multi-agent systems, emphasizing the imperative need for robust defenses against manipulated knowledge spread, such as introducing ``guardian'' agents and advanced fact-checking tools.

## 내 메모


