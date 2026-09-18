---
type: research-source
item_id: 2886
title: "GPT-6-Astra in a Navigation Workflow: Behavioral Analysis in Zero-Shot Vision-and-Language Navigation in Continuous Environments"
source: "arxiv"
published: "2026-09-17T12:14:43Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.20116"
url: "https://arxiv.org/abs/2609.20116v1"
generated_by: codex-research-db
aliases:
  - "GPT-6-Astra in a Navigation Workflow: Behavioral Analysis in Zero-Shot Vision-and-Language Navigation in Continuous Environments"
topics:
  - "self-evolving-harness"
---

# GPT-6-Astra in a Navigation Workflow: Behavioral Analysis in Zero-Shot Vision-and-Language Navigation in Continuous Environments

[원문 열기](https://arxiv.org/abs/2609.20116v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`WU8MGK9F`)
- 발행일: 2026-09-17T12:14:43Z
- 저자: Guangzhao Dai, Qi Wu, Bin Zhu
- 식별자: `arxiv:2609.20116`

## 요약·초록

We study GPT-6-Astra in a zero-shot Vision-and-Language Navigation in Continuous Environments (VLN-CE) system, where it interprets instructions, assesses its surroundings, and proposes actions. The system uses a common observation--decision--execution workflow with direct model API calls, without a packaged agent harness or navigation-specific fine-tuning. In this workflow, each request receives selected observations, execution feedback, and retained progress records. Evaluation covers the complete system, including context management and action control. We evaluate the system on 50 of the 100 R2R-CE val-unseen episodes used by Open-Nav. It achieves a success rate of 52.0\%, an SPL of 48.9\%, and an nDTW of 70.8\%. Our analysis highlights three findings. First, recorded responses link landmarks and earlier actions to instructions using observations and supplied history. Second, reviews include requests for additional views and revisions of uncertain judgments. Third, the results suggest a gap between task understanding and autonomous completion: an unfinished crossing is recognized while rotation continues. At termination, 36.0\% of episodes succeed with a workflow-accepted STOP, while another 16.0\% meet the distance criterion at the step limit. These results highlight a central challenge: translating correct local judgments into sustained progress and appropriate stopping.

## 내 메모


