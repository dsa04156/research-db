---
type: research-source
item_id: 1286
title: "Metronome: Differentiated Delay Scheduling for Serverless Functions"
source: "arxiv"
published: "2025-12-05T13:30:04Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.05703"
url: "https://arxiv.org/abs/2512.05703v1"
generated_by: codex-research-db
aliases:
  - "Metronome: Differentiated Delay Scheduling for Serverless Functions"
topics:
  - "cloud-infrastructure"
---

# Metronome: Differentiated Delay Scheduling for Serverless Functions

[원문 열기](https://arxiv.org/abs/2512.05703v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RB8KJIZE`)
- 발행일: 2025-12-05T13:30:04Z
- 저자: Zhuangbin Chen, Juzheng Zheng, Zibin Zheng
- 식별자: `arxiv:2512.05703`

## 요약·초록

Function-as-a-Service (FaaS) computing is an emerging cloud computing paradigm for its ease-of-management and elasticity. However, optimizing scheduling for serverless functions remains challenging due to their dynamic and event-driven nature. While data locality has been proven effective in traditional cluster computing systems through delay scheduling, its application in serverless platforms remains largely unexplored. In this paper, we systematically evaluate existing delay scheduling methods in serverless environments and identify three key observations: 1) delay scheduling benefits vary significantly based on function input characteristics; 2) serverless computing exhibits more complex locality patterns than cluster computing systems, encompassing both data locality and infrastructure locality; and 3) heterogeneous function execution times make rule-based delay thresholds ineffective. Based on these insights, we propose Metronome, a differentiated delay scheduling framework that employs predictive mechanisms to identify optimal locality-aware nodes for individual functions. Metronome leverages an online Random Forest Regression model to forecast function execution times across various nodes, enabling informed delay decisions while preventing SLA violations. Our implementation on OpenLambda shows that Metronome significantly outperforms baselines, achieving 64.88%-95.83% reduction in mean execution time for functions, while maintaining performance advantages under increased concurrency levels and ensuring SLA compliance.

## 내 메모


