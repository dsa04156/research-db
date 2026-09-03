---
type: research-source
item_id: 2424
title: "Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents"
source: "arxiv"
published: "2026-08-31T16:48:51Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.31076"
url: "https://arxiv.org/abs/2608.31076v1"
generated_by: codex-research-db
aliases:
  - "Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents"
topics:
  - "self-evolving-harness"
---

# Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents

[원문 열기](https://arxiv.org/abs/2608.31076v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`54QMDFGR`)
- 발행일: 2026-08-31T16:48:51Z
- 저자: Xuehai Wang, Haowei Qin, Tongxin Liu, Junkai Li, Buqiang Xu, Jintian Zhang, Yijun Chen, Zirui Xue, Shumin Deng
- 식별자: `arxiv:2608.31076`

## 요약·초록

Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-ended research tasks often do not clearly specify the analyses, methods, and success criteria required to complete the task. As a result, agents may miss important analyses, use inappropriate methods, or draw conclusions that are insufficiently supported by evidence. To address the problem, we present AutoSciRub, an evaluation-first framework that induces a task-specific executable rubric before research execution, and uses it to guide execution, criterion-level verification as well as iterative revision. AutoSciRub decomposes an underspecified instruction into atomic scientific goals, grounds them in relevant literature and task-visible data, and synthesizes specific, actionable, and verifiable criteria. The resulting rubric makes implicit experimental and evidential requirements explicit, providing guidance for experiments and analyses. During revision, rubric-guided verification identifies unmet criteria and enables targeted refinement of the research report and its supporting artifacts. On ResearchClawBench, AutoSciRub consistently improves all tested configurations, with an average gain of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using a fixed DeepSeek-V4-Flash backbone. On a randomly sampled 20-task subset of AstaBench E2E Discovery, AutoSciRub further achieves an average improvement of 16.8 points across three agent harnesses, while maintaining or increasing the number of successfully completed tasks. These results demonstrate that evaluation-first guidance provides an effective and generalizable control mechanism for autonomous scientific research (Code: https://github.com/zjunlp/AutoSciRub).

## 내 메모


