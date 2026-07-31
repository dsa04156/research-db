---
type: research-source
item_id: 254
title: "Octo-planner: On-device Language Model for Planner-Action Agents"
source: "arxiv"
published: "2024-06-26T05:40:10Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.18082"
url: "https://arxiv.org/abs/2406.18082v2"
generated_by: codex-research-db
aliases:
  - "Octo-planner: On-device Language Model for Planner-Action Agents"
topics:
  - "ai-agents"
---

# Octo-planner: On-device Language Model for Planner-Action Agents

[원문 열기](https://arxiv.org/abs/2406.18082v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HNS5T9P3`)
- 발행일: 2024-06-26T05:40:10Z
- 저자: Wei Chen, Zhiyuan Li, Zhen Guo, Yikang Shen
- 식별자: `arxiv:2406.18082`

## 요약·초록

AI agents have become increasingly significant in various domains, enabling autonomous decision-making and problem-solving. To function effectively, these agents require a planning process that determines the best course of action and then executes the planned actions. In this paper, we present an efficient on-device Planner-Action framework that separates planning and action execution into two distinct components: a planner agent based on Phi-3 Mini, a 3.8 billion parameter LLM optimized for edge devices, and an action agent using the Octopus model for function execution. The planner agent first responds to user queries by decomposing tasks into a sequence of sub-steps, which are then executed by the action agent. To optimize performance on resource-constrained devices, we employ model fine-tuning instead of in-context learning, reducing computational costs and energy consumption while improving response times. Our approach involves using GPT-4 to generate diverse planning queries and responses based on available functions, with subsequent validations to ensure data quality. We fine-tune the Phi-3 Mini model on this curated dataset, achieving a 97\% success rate in our in-domain test environment. To address multi-domain planning challenges, we developed a multi-LoRA training method that merges weights from LoRAs trained on distinct function subsets. This approach enables flexible handling of complex, multi-domain queries while maintaining computational efficiency on resource-constrained devices. To support further research, we have open-sourced our model weights at https://huggingface.co/NexaAIDev/octopus-planning. For the demo, please refer to https://www.nexa4ai.com/octo-planner.

## 내 메모


