---
type: research-source
item_id: 2338
title: "Feedback That Backfires: Why Small Language Model Agents Repeat the Call They Just Watched Fail"
source: "arxiv"
published: "2026-08-24T10:19:17Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.23651"
url: "https://arxiv.org/abs/2608.23651v1"
generated_by: codex-research-db
aliases:
  - "Feedback That Backfires: Why Small Language Model Agents Repeat the Call They Just Watched Fail"
topics:
  - "self-evolving-harness"
---

# Feedback That Backfires: Why Small Language Model Agents Repeat the Call They Just Watched Fail

[원문 열기](https://arxiv.org/abs/2608.23651v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-24T10:19:17Z
- 저자: Esmail Gumaan
- 식별자: `arxiv:2608.23651`

## 요약·초록

Agent harnesses record a failed tool call and its error message in the transcript and ask the model to continue, on the assumption that the error is corrective information. We measure whether it is. Defining the corrective gain of a failure record as the change in log-probability of re-emitting the action that just failed, we find the gain is negative for every instruction-tuned model we tested (6 checkpoints, 135M-1.7B, 4 families) in two environments: simulated tool calling and MBPP program repair. Normalised by action length the effect is about -1.03 nats per action token, a factor of 2.8 in the odds of each token, and holds on 90%-100% of individual items, not only on average. Over a fixed candidate set the probability of repeating the failed call rises from 0.06 to 0.54, and greedy decoding reproduces it token for token on 19% of items after the failure versus 0% before. Counterfactuals pairing the same call with a failure message, a success message, or a neutral acknowledgement separate two effects: the failed call's surface form accounts for 83% of the damage, while the semantic contribution of marking it failed is small and inconsistent in sign across environments. The problem is in the harness, not the model's grasp of error messages, and that predicts which remedies work. Replacing the verbatim call with a runtime-generated description of the failure removes 76% of the inversion at no token cost, and making previously-failed strings unreachable at the decoder acts on the same term. Two plausible remedies do not: an explicit "do not repeat" instruction leaves the measured quantity where it was, and deleting the failed attempt to retry from a clean context, the standard prescription for context contamination, is the worst harness we measured for repetition, because it restores the context that produced the failure. The study runs end to end on a CPU; all artefacts are released.

## 내 메모
