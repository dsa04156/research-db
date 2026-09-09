---
type: research-source
item_id: 2611
title: "Cost-Aware Hierarchical Multi-Agent Ransomware Detection and Family Attribution"
source: "arxiv"
published: "2026-09-04T07:17:09Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.04820"
url: "https://arxiv.org/abs/2609.04820v1"
generated_by: codex-research-db
aliases:
  - "Cost-Aware Hierarchical Multi-Agent Ransomware Detection and Family Attribution"
topics:
  - "ai-agents"
---

# Cost-Aware Hierarchical Multi-Agent Ransomware Detection and Family Attribution

[원문 열기](https://arxiv.org/abs/2609.04820v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7P83IKHB`)
- 발행일: 2026-09-04T07:17:09Z
- 저자: Mubashar Iqbal, Asifullah Khan
- 식별자: `arxiv:2609.04820`

## 요약·초록

Ransomware detection and family attribution require analysis of different modalities because it can use packing, obfuscation, process manipulation and runtime evasion techniques. However, conventional multimodal usually uses all available modalities for every sample resulting in unnecessary computational cost and increased latency. In this paper, we present a Cost Aware Hierarchical Multi-Agent System (HMAS) for adaptive ransomware detection. The proposed architecture organizes specialized agents into hierarchical domain controllers coordinated by a Meta Orchestrator. Static analysis is used as the initial low-cost modality while additional dynamic and memory modality is selectively used when confidence is insufficient or specialist agents exhibit disagreement. A cost model incorporates modality use and processing overhead. It enables the orchestration policy to balance analysis performance against computational cost. A locally deployed large language model provides verification for selected difficult cases without replacing the deterministic pipeline. Experimental evaluation compares adaptive HMAS with static only, static plus dynamic and exhaustive analysis policies across binary ransomware detection and multiclass family attribution. The complete HMAS achieved 96.57% accuracy, 0.96 F1-score and 0.99 ROC-AUC for binary detection. It also achieved 0.90 macro-F1 for family attribution. At the same time, the HMAS reduced average analysis cost by 43.97% relative to exhaustive analysis and substantially reduced average analysis latency except for the case where LLM is used. Routing analysis showed that 56.05% of cases were resolved using static evidence alone. Only 4.33% required the complete evidence pipeline. These findings demonstrate that adaptive HMAS can provide accuracy cost tradeoff for ransomware analysis while retaining support for heterogeneous and incomplete modalities.

## 내 메모


