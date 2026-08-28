---
type: research-source
item_id: 2246
title: "InjecMEM: Memory Injection Attack on LLM Agent Memory Systems"
source: "arxiv"
published: "2026-08-24T16:37:50Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.23471"
url: "https://arxiv.org/abs/2608.23471v1"
generated_by: codex-research-db
aliases:
  - "InjecMEM: Memory Injection Attack on LLM Agent Memory Systems"
topics:
  - "ai-agents"
---

# InjecMEM: Memory Injection Attack on LLM Agent Memory Systems

[원문 열기](https://arxiv.org/abs/2608.23471v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8TTHB7JW`)
- 발행일: 2026-08-24T16:37:50Z
- 저자: Hanling Tian, Gengyu Zhang, Zeyang Sha, Jingying Wang, Yuhang Liu, Zhehao Huang, Kun Yang, Xiaolin Huang
- 식별자: `arxiv:2608.23471`

## 요약·초록

Memory is becoming a default subsystem in deployed LLM agents to provide persistent personalization and continuity. This naturally prompts a question: will memory system introduce new vulnerabilities into agents? Thus we propose InjecMEM, a novel memory injection attack paradigm that requires only a single interaction (no read/edit access to memory store) to steer later responses of related queries toward a pre-specified output. Guided by the retrieval-then-generate mechanism of memory systems, we craft the injection with a retriever-agnostic anchor and an adversarial command. The anchor contains high-recall topical cues so that downstream retrieval consistently associates the record with the target topic. The command is a short sequence optimized to remain effective under uncertain fused contexts, variable placements, and long prompts so that it reliably steers outputs once retrieved. We learn the command via gradient-based coordinate search, averaging over synthetic prompt templates and insertion positions, and extend it to joint optimization across backbones to study transfer. Evaluated across multiple memory systems and backbone models, InjecMEM achieves reliable topic-conditioned retrieval and targeted generation, remains effective under memory drift, and leaves non-target queries unaffected. Our results underscore the need to harden memory systems and provide a reproducible framework for studying agent memory.

## 내 메모


