---
type: research-source
item_id: 1006
title: "The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI"
source: "arxiv"
published: "2026-07-08T01:58:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.06906"
url: "https://arxiv.org/abs/2607.06906v1"
generated_by: codex-research-db
aliases:
  - "The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI

[원문 열기](https://arxiv.org/abs/2607.06906v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`PGTUP2PA`)
- 발행일: 2026-07-08T01:58:12Z
- 저자: Muayad Sayed Ali, Aliaksandra Novik, Anji Boddupally, Artem Yavorskyi, Chris Nickerson, Daniel Rica, Emily DuGranrut, Felix Leung, Garrett Prince, Grace Barnett, Heath Robinson, Hosain Al Ahmad, Jesse Resnick, Juan Carlos Farah, Jyothi Swaroop Meruga, Leonid Kuznetsov, Luke Gorham, Marie Schmoll, Michael Paciullo, Saumya Das, Sharath Sheripally, Tommy Griscom, Mykyta Osadchyi, Neha Mantri, Nick Westrum, Olivia Benowitz, Parikshith Kulkarni, Radik Chernyshov, Rakshith Vasudev, Rohith Nadimpally, Vikas Gangadevi, Waseem AlShikh
- 식별자: `arxiv:2607.06906`

## 요약·초록

Agentic AI development today runs on token maxing: buying capability with tokens -- longer reasoning traces, more turns, wider tool payloads, bigger replayed contexts -- so tokens per task grow faster than task value. Falling per-token prices mask the pattern; total spend rises anyway. We argue the decisive lever against token maxing is the harness: the orchestration layer that assembles context, exposes tools, sequences turns, delegates work, and carries enterprise observability and governance. We isolate it with a controlled swap: 22 locked evaluation tasks, six foundation models (Claude Sonnet 4.6, Gemini 3.1, Gemini Flash 3.5, Qwen 3.6, GLM 5.1, Palmyra X6), changing only the orchestration layer -- a frozen conventional production loop versus the Writer Agent Harness. Holding models constant, the harness cuts blended cost per task 41% ($0.21->$0.12), median wall-clock 44% (48s->27s), and tokens per task 38% (14.2k->8.8k), with task-completion quality at parity (0.78->0.81, directional at this sample size). Efficiency is model-invariant -- every model gets cheaper (33-61%) -- while quality gains are capability-dependent: a model's gain correlates almost perfectly with its baseline strength (r=0.99, n=6), a phenomenon we term harness leverage. Quality per dollar rises 82%; task-completions per million tokens rise from 54.9 to 92.0. On this workload the orchestration layer moved cost per task more than the full spread of the model menu did. We formalize token economics at the orchestration layer (including effective input price under prompt caching), detail the six mechanism families behind the effect -- cache-shape discipline to failure-spend governance -- compare six widely used agent systems on the same axes, and argue the harness is the one component whose efficiency multiplies across every model an organization runs -- present and future.

## 내 메모


