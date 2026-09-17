# Skill Observation Log

Observations captured during task-oriented work.

**Status key:** OPEN = not yet actioned | ACTIONED (YYYY-MM-DD) = skill updated/created | DECLINED (YYYY-MM-DD) = user decided not to pursue — resolved statuses always carry their resolution date

---

## 2026-08-24

### Observation 2: Explicit source exclusions still produce setup nudges

**Status:** ACTIONED (2026-09-15) — Applied to last30days (weekly review)
**Date:** 2026-08-24
**Session context:** Daily social and trend research set `EXCLUDE_SOURCES=x` on every last30days process because the workflow explicitly forbids X access and configuration.
**Skill:** last30days
**Type:** open-source
**Phase/Area:** Coverage reporting

**Issue:** Diagnostic and search output still suggested unlocking or configuring X even though X was explicitly excluded. This creates noisy, contradictory guidance in unattended runs.

**Suggested improvement:** Treat explicit exclusions as a hard suppression rule for setup tips, coverage warnings, and recommended next actions related to that source.

**Principle:** An explicit exclusion must remove a source from both execution and user-facing remediation advice.

### Observation 3: Quick mode silently narrows an explicit source plan

**Status:** ACTIONED (2026-09-15) — Applied to last30days (weekly review)
**Date:** 2026-08-24
**Session context:** The host supplied planned queries and requested Reddit, Hacker News, YouTube, TikTok, Instagram, GitHub, and LinkedIn for a one-day quick scan.
**Skill:** last30days
**Type:** open-source
**Phase/Area:** Planner and retrieval

**Issue:** Quick mode executed only the first planned subquery and returned evidence from Reddit/Hacker News without clearly surfacing that the other requested sources were not searched. A downstream automation could mistake missing execution for zero results.

**Suggested improvement:** Emit an explicit per-source status such as `skipped_by_quick_mode`, and preserve the host plan's source list in the machine-readable coverage report.

**Principle:** Optimization modes must report every requested source as searched, skipped, failed, or unavailable; silence is not a zero-result signal.

### Observation 4: Discovery clusters can overstate independent corroboration

**Status:** ACTIONED (2026-09-15) — Applied to last30days (weekly review)
**Date:** 2026-08-28
**Session context:** Daily trend discovery grouped a framework-free agent notebook with an unrelated Framework laptop post, and grouped several distinct local-model, WASM-harness, and security items under one trend label.
**Skill:** last30days
**Type:** open-source
**Phase/Area:** Discovery clustering and trend validation

**Issue:** Keyword overlap can place unrelated results from different platforms in one candidate cluster. Counting those platforms as independent corroboration then inflates trend confidence even though the underlying claims and entities differ.

**Suggested improvement:** Require entity and claim compatibility before increasing a candidate's independent-platform count, and expose rejected cluster members with a machine-readable mismatch reason.

**Principle:** Cross-platform corroboration is valid only when independent sources support the same entity and claim, not merely overlapping vocabulary.

## 2026-09-14

### Observation 5: Unreadable optional config aborts before degraded-mode reporting

**Status:** ACTIONED (2026-09-15) — Applied to last30days (weekly review)
**Date:** 2026-09-14
**Session context:** An unattended research run executed in a restricted environment where the global last30days config file existed but could not be read.
**Skill:** last30days
**Type:** open-source
**Phase/Area:** Configuration loading and source status

**Issue:** The engine raised `PermissionError` while reading the optional global config and exited before writing a machine-readable report. Setting an empty config directory avoided the crash, but then configured sources appeared as unavailable rather than inaccessible.

**Suggested improvement:** Catch permission errors on optional config files, continue in keyless mode, and emit an explicit `config-inaccessible` status without exposing the path contents or secret values.

**Principle:** Optional configuration failures should degrade into explicit coverage status, not erase the entire run before observability artifacts are produced.
