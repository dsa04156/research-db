---
type: research-source
item_id: 234
title: "On scalable oversight with weak LLMs judging strong LLMs"
source: "arxiv"
published: "2024-07-05T16:29:15Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.04622"
url: "https://arxiv.org/abs/2407.04622v2"
generated_by: codex-research-db
aliases:
  - "On scalable oversight with weak LLMs judging strong LLMs"
topics:
  - "ai-agents"
---

# On scalable oversight with weak LLMs judging strong LLMs

[원문 열기](https://arxiv.org/abs/2407.04622v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2MR3DWAV`)
- 발행일: 2024-07-05T16:29:15Z
- 저자: Zachary Kenton, Noah Y. Siegel, János Kramár, Jonah Brown-Cohen, Samuel Albanie, Jannis Bulian, Rishabh Agarwal, David Lindner, Yunhao Tang, Noah D. Goodman, Rohin Shah
- 식별자: `arxiv:2407.04622`

## 요약·초록

Scalable oversight protocols aim to enable humans to accurately supervise superhuman AI. In this paper we study debate, where two AI's compete to convince a judge; consultancy, where a single AI tries to convince a judge that asks questions; and compare to a baseline of direct question-answering, where the judge just answers outright without the AI. We use large language models (LLMs) as both AI agents and as stand-ins for human judges, taking the judge models to be weaker than agent models. We benchmark on a diverse range of asymmetries between judges and agents, extending previous work on a single extractive QA task with information asymmetry, to also include mathematics, coding, logic and multimodal reasoning asymmetries. We find that debate outperforms consultancy across all tasks when the consultant is randomly assigned to argue for the correct/incorrect answer. Comparing debate to direct question answering, the results depend on the type of task: in extractive QA tasks with information asymmetry debate outperforms direct question answering, but in other tasks without information asymmetry the results are mixed. Previous work assigned debaters/consultants an answer to argue for. When we allow them to instead choose which answer to argue for, we find judges are less frequently convinced by the wrong answer in debate than in consultancy. Further, we find that stronger debater models increase judge accuracy, though more modestly than in previous studies.

## 내 메모


