# Skill Observation Log

Observations captured during task-oriented work.

**Status key:** OPEN = not yet actioned | ACTIONED (YYYY-MM-DD) = skill updated/created | DECLINED (YYYY-MM-DD) = user decided not to pursue — resolved statuses always carry their resolution date

---

## 2026-08-24

### Observation 1: Observer initialization can interfere with clean-tree pre-sync

**Status:** ACTIONED (2026-08-25) — Applied to task-observer (weekly review)
**Date:** 2026-08-24
**Session context:** An autonomous multi-step workflow required a clean Git worktree check before pulling, while Task Observer initialization created new workspace files first.
**Skill:** task-observer
**Type:** open-source
**Phase/Area:** Session Start Protocol

**Issue:** Creating the observation files before a workflow's clean-tree preflight can make an originally clean repository appear dirty and prevent an otherwise safe fast-forward pull.

**Suggested improvement:** When a task has an explicit repository pre-sync gate, inspect and record the initial worktree state before observer initialization, or define observer state outside the repository's tracked workspace.

**Principle:** Instrumentation should not mutate the state that a workflow's preconditions are about to measure.

### Observation 2: Explicit source exclusions still produce setup nudges

**Status:** OPEN
**Date:** 2026-08-24
**Session context:** Daily social and trend research set `EXCLUDE_SOURCES=x` on every last30days process because the workflow explicitly forbids X access and configuration.
**Skill:** last30days
**Type:** open-source
**Phase/Area:** Coverage reporting

**Issue:** Diagnostic and search output still suggested unlocking or configuring X even though X was explicitly excluded. This creates noisy, contradictory guidance in unattended runs.

**Suggested improvement:** Treat explicit exclusions as a hard suppression rule for setup tips, coverage warnings, and recommended next actions related to that source.

**Principle:** An explicit exclusion must remove a source from both execution and user-facing remediation advice.

### Observation 3: Quick mode silently narrows an explicit source plan

**Status:** OPEN
**Date:** 2026-08-24
**Session context:** The host supplied planned queries and requested Reddit, Hacker News, YouTube, TikTok, Instagram, GitHub, and LinkedIn for a one-day quick scan.
**Skill:** last30days
**Type:** open-source
**Phase/Area:** Planner and retrieval

**Issue:** Quick mode executed only the first planned subquery and returned evidence from Reddit/Hacker News without clearly surfacing that the other requested sources were not searched. A downstream automation could mistake missing execution for zero results.

**Suggested improvement:** Emit an explicit per-source status such as `skipped_by_quick_mode`, and preserve the host plan's source list in the machine-readable coverage report.

**Principle:** Optimization modes must report every requested source as searched, skipped, failed, or unavailable; silence is not a zero-result signal.

### Observation 4: Discovery clusters can overstate independent corroboration

**Status:** OPEN
**Date:** 2026-08-28
**Session context:** Daily trend discovery grouped a framework-free agent notebook with an unrelated Framework laptop post, and grouped several distinct local-model, WASM-harness, and security items under one trend label.
**Skill:** last30days
**Type:** open-source
**Phase/Area:** Discovery clustering and trend validation

**Issue:** Keyword overlap can place unrelated results from different platforms in one candidate cluster. Counting those platforms as independent corroboration then inflates trend confidence even though the underlying claims and entities differ.

**Suggested improvement:** Require entity and claim compatibility before increasing a candidate's independent-platform count, and expose rejected cluster members with a machine-readable mismatch reason.

**Principle:** Cross-platform corroboration is valid only when independent sources support the same entity and claim, not merely overlapping vocabulary.
