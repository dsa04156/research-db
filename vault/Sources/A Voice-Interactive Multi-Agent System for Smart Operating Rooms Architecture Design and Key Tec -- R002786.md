---
type: research-source
item_id: 2786
title: "A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies"
source: "arxiv"
published: "2026-09-10T08:29:27Z"
first_seen: "2026-09-11"
review_status: "pending"
canonical_key: "arxiv:2609.11231"
url: "https://arxiv.org/abs/2609.11231v1"
generated_by: codex-research-db
aliases:
  - "A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies"
topics:
  - "ai-agents"
---

# A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies

[원문 열기](https://arxiv.org/abs/2609.11231v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-11|2026-09-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-10T08:29:27Z
- 저자: Tianxiang Zhou
- 식별자: `arxiv:2609.11231`

## 요약·초록

This paper presents SurgicalRoomAgent, a voice-interactive multi-agent system for smart operating rooms based on large language models (LLMs). The system achieves natural language understanding, device control, intraoperative recording, and surgical report generation through a layered architecture comprising a voice interaction pipeline (wake, ASR, turn detection, agent reasoning, TTS) and an agent core (skill registry, task planner, device manager). Three key technologies are investigated: (1) KV Cache prefix warming for low-latency inference, reducing recomputation overhead from approximately 500 ms to tens of milliseconds via byte-level Longest Common Prefix reuse; (2) streaming partial JSON parsing with early parallel task execution, reducing end-to-end latency by approximately 30%; and (3) progressive skill prompt disclosure, which dynamically filters system prompts based on user role, connected devices, and surgical phase to maximize information density within limited context windows. The system is implemented using the Qwen3-27B model with llama.cpp/sglang inference engines. Experimental analysis demonstrates effective operation within a 16,384-token context limit and multi-device parallel control response times meeting OR real-time requirements.

## 내 메모


