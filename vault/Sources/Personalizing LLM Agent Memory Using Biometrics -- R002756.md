---
type: research-source
item_id: 2756
title: "Personalizing LLM Agent Memory Using Biometrics"
source: "arxiv"
published: "2026-09-08T10:46:12Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.08558"
url: "https://arxiv.org/abs/2609.08558v1"
generated_by: codex-research-db
aliases:
  - "Personalizing LLM Agent Memory Using Biometrics"
topics:
  - "ai-agents"
---

# Personalizing LLM Agent Memory Using Biometrics

[원문 열기](https://arxiv.org/abs/2609.08558v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`B5E4JGAZ`)
- 발행일: 2026-09-08T10:46:12Z
- 저자: Yanhong Qian, Qingguo Meng, Shihao Ding, Xingbo Dong, Zhe Jin, Hanrui Wang, Isao Echizen
- 식별자: `arxiv:2609.08558`

## 요약·초록

Personalized memory helps LLM agents deliver stable, tailored assistance by storing and reusing user-specific data across interactions. In multi-user scenarios, however, retrieval must consider not only semantic similarity but also whether the current requester matches the identity associated with the stored memory. We propose Bio-Memory, a biometric-aware memory architecture that conditions memory retrieval on both semantic similarity and biometric matching. Built on top of A-Mem, Bio-Memory augments each atomic memory note with a biometric embedding and uses biometric matching to form the retrieval candidate pool before semantic ranking. We evaluate Bio-Memory on LoCoMo in a 10-user shared-agent setting over 7 face benchmarks and 10 palmprint protocols. Across datasets, Bio-Memory consistently separates owner and non-owner queries. Under face-based personalization, the largest average gap reaches 27.29% / 21.15% in F1 / BLEU-1 on CALFW; under palmprint-based personalization, the corresponding gap is 25.75% / 19.22% on MS_Blue. These results support biometrics as a practical control signal for personalized memory retrieval in shared environments.

## 내 메모


