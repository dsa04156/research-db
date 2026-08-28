---
type: research-source
item_id: 2311
title: "Referee Report — arXiv:2606.04329 \"Memory Poisoning\": Resolving a Conflicting-Claims Discrepancy Through Primary-Source Verification"
source: "openalex"
published: "2026-08-24"
first_seen: "2026-08-26"
review_status: "pending"
canonical_key: "doi:10.5281/zenodo.22084116"
url: "https://arxiv.org/abs/2606.04329"
generated_by: codex-research-db
aliases:
  - "Referee Report — arXiv:2606.04329 \"Memory Poisoning\": Resolving a Conflicting-Claims Discrepancy Through Primary-Source Verification"
topics:
  - "ai-agents"
---

# Referee Report — arXiv:2606.04329 "Memory Poisoning": Resolving a Conflicting-Claims Discrepancy Through Primary-Source Verification

[원문 열기](https://arxiv.org/abs/2606.04329)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-26|2026-08-26]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`HCJ6GKP8`)
- 발행일: 2026-08-24
- 저자: Mustafa Melikoğlu, Yağız Deniz Altınbaş, Tayfun Tanrıöver
- 식별자: `doi:10.5281/zenodo.22084116`

## 요약·초록

A verification referee report resolving a conflicting-claims discrepancy about arXiv:2606.04329 ("From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents", Dash, Ge, Jain, Shah, Shang). Two secondary-source claims about the paper's headline attack-success numbers were circulating: a "70–95% vulnerability" figure (amplified on Reddit) versus "average ASR of 50.46% and RSR of 41.05% across both agents." We verified both claims directly against the paper's raw HTML full text using grep-based textual confirmation, independent of any fetch/summarization layer. Finding: the 50.46% / 41.05% figures are the paper's own verbatim headline statistic (Introduction, contributions list), and reproduce exactly as the average of the two tested agents' averages (OpenClaw, HERMES). The "70–95%" figure appears nowhere in the paper as a summary; it is a cherry-picked over-generalization of the single most-vulnerable agent's strong-signal attack subset (a lone 92.76% maximum), not the general finding. The arXiv ID is real and resolves correctly — this is not a hallucinated citation, but a selective-reading error, and the Sources C / Reddit quotation should be corrected or contextualized downstream. The report doubles as a case study in source-verification discipline: why numeric claims must be traced to the primary source, and why fetch/summarizer layers require raw-text cross-verification even for location attributions. AI-transparency note: The authors of this record operate under human direction. This report was drafted by an AI agent, cross-family jury-reviewed (blind; producer family excluded), and reviewed by a human before publication.

## 내 메모


