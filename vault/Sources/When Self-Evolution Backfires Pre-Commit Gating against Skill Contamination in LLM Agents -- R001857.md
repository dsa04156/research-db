---
type: research-source
item_id: 1857
title: "When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents"
source: "openalex"
published: "2026-08-06"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.05810"
url: "https://arxiv.org/abs/2608.05810"
generated_by: codex-research-db
aliases:
  - "When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents"
topics:
  - "self-evolving-harness"
---

# When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents

[원문 열기](https://arxiv.org/abs/2608.05810)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-08-06
- 저자: Linfang Shang, Ming Xu, Yiding Sun, Tianle Xia, Lingxiang Hu, Lan Xu, Ning Zheng
- 식별자: `arxiv:2608.05810`

## 요약·초록

Self-evolving agents accumulate capability by distilling reusable skills from their execution trajectories, but we find this process is not monotonic: past a critical pool size, newly added skills degrade performance instead of improving it. We formalize this capability-contamination phase transition and trace it to a structural cause: once a defective skill enters the decision context, it becomes reference material for distilling later skills, forming cross-round contamination chains. We further show the contamination is structurally irreversible: removing a source skill after the fact cannot erase the flawed reasoning its descendants have already inherited, so post-hoc rollback recovers only a small fraction of the lost performance. This makes skill admission a pre-commit necessity rather than a post-hoc fix, and motivates Verifier-as-Gatekeeper (VaG): a progressive trust hierarchy whose three heterogeneous critics - structural validity, behavioral harmlessness, and semantic consistency - filter each skill individually, coupled with a marginal-gain subset selection that removes combinatorial contamination at the top tier before skills reach the runtime context. On Terminal-Bench 2, unconditional accumulation rises to a peak and then degrades, giving back most of its gains as the pool keeps growing, and post-hoc removal of the culprit skills recovers only a small part of the drop - the empirical signature of irreversibility. In contrast, VaG improves every round, reaching 72% pass@1 with a pool roughly 5x smaller, and its frozen skill pool transfers positively to four other backbones and a second benchmark without re-evolution. Ablations confirm the three critics are complementary and mutually non-substitutable, each intercepting a largely disjoint class of harmful skills.

## 내 메모


