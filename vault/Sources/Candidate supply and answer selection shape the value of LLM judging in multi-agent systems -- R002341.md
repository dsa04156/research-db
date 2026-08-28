---
type: research-source
item_id: 2341
title: "Candidate supply and answer selection shape the value of LLM judging in multi-agent systems"
source: "arxiv"
published: "2026-08-26T15:52:20Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25937"
url: "https://arxiv.org/abs/2608.25937v1"
generated_by: codex-research-db
aliases:
  - "Candidate supply and answer selection shape the value of LLM judging in multi-agent systems"
topics:
  - "ai-agents"
---

# Candidate supply and answer selection shape the value of LLM judging in multi-agent systems

[원문 열기](https://arxiv.org/abs/2608.25937v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8KEWNSPQ`)
- 발행일: 2026-08-26T15:52:20Z
- 저자: Jia-Hao Ji, Sijie Li, Jiabei Cheng, Zixi She, Jin-Tai Yu, Zhiyuan Yuan
- 식별자: `arxiv:2608.25937`

## 요약·초록

Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when an LLM judge provides effective selection pressure by supplying a signal of answer correctness for candidates generated in a multi-agent system, and (2) when using that signal improves the reported answer. To map judge reliability, we analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks. We report three findings. (1) A correct answer is often already present among the generated candidates, but the system can still converge on and report a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the task, the generator and how rare the correct answer is. (3) Combining answer frequency with the judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors. In the systems studied here, the value of generating more candidates depends on whether those extra samples make correct answers present, frequent or recognisable. By isolating generation, recognition and selection, these findings establish a diagnostic basis for designing multi-agent architectures that protect generated correct answers from being lost.

## 내 메모


