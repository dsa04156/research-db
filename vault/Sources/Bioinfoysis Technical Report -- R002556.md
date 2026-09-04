---
type: research-source
item_id: 2556
title: "Bioinfoysis Technical Report"
source: "arxiv"
published: "2026-09-03T13:59:00Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.03871"
url: "https://arxiv.org/abs/2609.03871v1"
generated_by: codex-research-db
aliases:
  - "Bioinfoysis Technical Report"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Bioinfoysis Technical Report

[원문 열기](https://arxiv.org/abs/2609.03871v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T13:59:00Z
- 저자: Qingyang Shao, Xin Zhang, Zhouyang Yuan, Xianying Chen, Yujia Xiang, Zihao Yang, Tong Ye, Yangqi Zhang, Jiakang Xu, Xiaoqing Yan, Xuan Luo, Keyi Li, Enci Fan, Kai Kang, Zhuohan Liu, Xingyu Jin, Chunran Teng, Tao Li, Xinyu Lv, Minghui Wang, Wenfeng Li, Yidan Gao, Siyu Liu, Mingrui Luo, Zhu Liang, Guanren Qiao, Zhiping Xu
- 식별자: `arxiv:2609.03871`

## 요약·초록

Large language model agents have shown promise in bioinformatics, but most existing systems focus primarily on producing final answers, treating planning, tool use, and code execution as transient interactions. This design is poorly suited to long-horizon bioinformatics tasks, where conclusions must remain connected to the data, computations, and intermediate evidence that support them. We introduce \textbf{Bioinfoysis}, a multi-agent harness that represents each request as a persistent, artifact-grounded analysis run. Bioinfoysis combines global planning with step-wise, evidence-driven replanning: the planner maintains an executable checklist and revises pending steps using structured handoffs returned after each worker execution. These handoffs bind intermediate results to their responsible agent, checklist step, and plan generation, preventing stale evidence from being silently reused after replanning. A controlled runtime validates generated scripts, tables, and figures before they are used in downstream analysis or reporting, while role-specific context, persistent memory, and governed bioinformatics skills support reliable execution over long analysis trajectories. We evaluate Bioinfoysis on BixBench and two question-answering tracks of LAB-Bench 2. On BixBench, Bioinfoysis achieves state-of-the-art accuracy of 82.4\%. Across four underlying language models, Bioinfoysis increases average accuracy from 27.81\% to 64.13\% on SeqQA2 and from 3.13\% to 31.25\% on DbQA2. These results demonstrate that reliable bioinformatics automation depends not only on model capability, but also on the harness that governs planning, execution, memory, and evidence flow. We hope that the emergence of Bioinfoysis will play a driving and leading role in the development of the bioinformatics community. Our demo website can be seen in https://report.bioinfoysis.com/.

## 내 메모


