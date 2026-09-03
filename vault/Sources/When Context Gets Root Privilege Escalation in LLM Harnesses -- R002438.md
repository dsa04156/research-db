---
type: research-source
item_id: 2438
title: "When Context Gets Root: Privilege Escalation in LLM Harnesses"
source: "arxiv"
published: "2026-08-27T16:03:57Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.27299"
url: "https://arxiv.org/abs/2608.27299v1"
generated_by: codex-research-db
aliases:
  - "When Context Gets Root: Privilege Escalation in LLM Harnesses"
topics:
  - "self-evolving-harness"
---

# When Context Gets Root: Privilege Escalation in LLM Harnesses

[원문 열기](https://arxiv.org/abs/2608.27299v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`IWIJ824F`)
- 발행일: 2026-08-27T16:03:57Z
- 저자: Xingbang He, Yuanwei Chen, Yi Qian, Haiyang Wei, Ligeng Chen, Zenan Fu, Linzhang Wang, Hao Wu, Bing Mao
- 식별자: `arxiv:2608.27299`

## 요약·초록

Instruction hierarchy is a model-side defense that assigns instructions different levels of privilege according to their sources. These levels constrain which content may direct model behavior. During agent execution, however, agent harnesses construct context for each model invocation. This construction can elevate low-level content to a higher instruction level and grant it greater model-facing privilege. We introduce instruction privilege escalation. In this attack, an attacker induces an agent to elevate low-level malicious content to a higher instruction level. The elevated content then causes the agent to execute instructions it would not follow at their original level. We evaluate this threat by using multi-agent mechanisms to achieve 13 attack objectives across six coding-agent harnesses. These objectives span confidentiality, integrity, availability, and remote code execution. With unrestricted action execution, the attacks achieve all 13 objectives on all six harnesses. Under automatic permission review, the attacks achieve all 13 objectives on all three harnesses that provide this mode. We further reproduce the vulnerability using harness-provided persistent goals and scheduled tasks. These results demonstrate the generality of instruction privilege escalation.

## 내 메모


