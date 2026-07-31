---
type: research-source
item_id: 212
title: "MetaTool: Facilitating Large Language Models to Master Tools with Meta-task Augmentation"
source: "arxiv"
published: "2024-07-15T10:15:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.12871"
url: "https://arxiv.org/abs/2407.12871v2"
generated_by: codex-research-db
aliases:
  - "MetaTool: Facilitating Large Language Models to Master Tools with Meta-task Augmentation"
topics:
  - "ai-agents"
---

# MetaTool: Facilitating Large Language Models to Master Tools with Meta-task Augmentation

[원문 열기](https://arxiv.org/abs/2407.12871v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`QN7K5TDU`)
- 발행일: 2024-07-15T10:15:41Z
- 저자: Xiaohan Wang, Dian Li, Yilin Zhao, Sinbadliu, Hui Wang
- 식별자: `arxiv:2407.12871`

## 요약·초록

Utilizing tools with Large Language Models (LLMs) is essential for grounding AI agents in real-world applications. The prevailing approach involves few-shot prompting with demonstrations or fine-tuning with expert annotations. However, mere in-context demonstrations may fail to cover sufficient knowledge for complex tools and tasks. Training on solution paths is also hindered by the high cost of expert annotations and generalizing to new tools. A core challenge of generalizable tool use lies in understanding the "meta", or fundamental natures of tools that are transferable across tasks, such as causality and constraints. In this paper, we present MetaTool, a novel tool learning methodology designed to generalize across any reusable toolset. Our approach incorporates a self-supervised augmentation technique derived from a series of meta-tasks. This involves predicting masked elements in the tool execution process. The self-supervised procedure enables scalable generation of high-quality QA data, which is handy for supervising tool understanding. By incorporating meta-task data into task-oriented training, our method significantly enhances the performance of open-source LLMs, achieving results comparable to ChatGPT in both tool-based planning and chatting scenarios. Through large-scale instruction tuning, the MetaTool model demonstrates impressive zero-shot generalizability on new tasks.

## 내 메모


