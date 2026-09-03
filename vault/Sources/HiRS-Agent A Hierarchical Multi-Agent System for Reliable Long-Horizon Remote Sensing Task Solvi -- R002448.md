---
type: research-source
item_id: 2448
title: "HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving"
source: "arxiv"
published: "2026-08-31T12:13:41Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.30672"
url: "https://arxiv.org/abs/2608.30672v1"
generated_by: codex-research-db
aliases:
  - "HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving"
topics:
  - "ai-agents"
---

# HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving

[원문 열기](https://arxiv.org/abs/2608.30672v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2FEH6U8Q`)
- 발행일: 2026-08-31T12:13:41Z
- 저자: Boyang Mu, Zhiwei Wei, Mugen Peng, Wenjia Xu
- 식별자: `arxiv:2608.30672`

## 요약·초록

Recent advances in large language models and multimodal models have pushed remote sensing (RS) processing from simple perception models to agentic systems designed to tackle complex, long-horizon RS tasks. However, existing systems often rely on monolithic decision-making frameworks, which fail to accommodate the multi-stage, interdependent nature of RS tasks. This centralized approach leads to challenges such as unstable task execution, incorrect tool usage, and error propagation across stages. To address these issues, we propose HiRS-Agent, a hierarchical multi-agent system for long-horizon RS task solving. HiRS-Agent adopts a two-level collaborative architecture: the Manager Layer handles dynamic routing, step-level verification, replanning, and termination control, while the Specialist Layer organizes domain-specific tools according to the RS workflow and is responsible for subtask reasoning and tool execution. To further enhance the system's capability, we introduce a two-stage supervised tuning strategy and a verification-guided hierarchical reinforcement learning stage to jointly optimize coordination and tool-use policies. Experiments on Earth-Agent Benchmark and ThinkGeo show that HiRS-Agent substantially improves long-horizon tool-use capability and final-task correctness, demonstrating the effectiveness of structured multi-agent collaboration for reliable RS agents. The code is publicly available at https://github.com/IntelliSensing/HiRS-Agent.

## 내 메모


