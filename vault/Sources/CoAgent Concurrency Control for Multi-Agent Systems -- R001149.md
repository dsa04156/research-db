---
type: research-source
item_id: 1149
title: "CoAgent: Concurrency Control for Multi-Agent Systems"
source: "arxiv"
published: "2026-06-13T16:15:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.15376"
url: "https://arxiv.org/abs/2606.15376v1"
generated_by: codex-research-db
aliases:
  - "CoAgent: Concurrency Control for Multi-Agent Systems"
topics:
  - "ai-agents"
  - "kubernetes"
---

# CoAgent: Concurrency Control for Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2606.15376v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GVHVENJJ`)
- 발행일: 2026-06-13T16:15:14Z
- 저자: Hongtao Lyu, Dingyan Zhang, Mingyu Wu, Xingda Wei, Haibo Chen
- 식별자: `arxiv:2606.15376`

## 요약·초록

Multi-agent LLM systems -- coding agents, devops agents, document agents -- now routinely run several agents in parallel against the same git tree, Kubernetes cluster, or document. As soon as two of them mutate shared state, they enter the regime classical concurrency control has studied for decades, but classical mechanisms fit LLM agents poorly. A single agent transaction spans minutes of inference, read sets are broad and opaque rather than statically inferable, and the live state agents act on admits neither fork nor buffer, so writes take effect the moment they execute. Locks block long inference intervals; OCC abort-and-retry discards minutes of work on every conflict. This paper builds concurrency control on a capability classical transactions lack: the LLM inside each agent can judge whether a conflicting write invalidates its plan, and can repair exactly the operations that depended on it. Control therefore turns advisory: the runtime informs, the agent repairs. Our protocol, MTPO (Monotonic Trajectory Pre-Order), fixes a serialization order at launch, serves each read the order-filtered value, and applies writes speculatively in place; a one-way notification asks an affected reader to re-judge and patch its plan, while the framework mechanically undoes and reorders misplaced writes through the saga-style inverse each tool registers in advance. At quiescence the run is serializable in the pre-decided order. We realize MTPO as CoAgent, toolcall middleware whose privileged ToolSmith grows footprint-declared, undoable tools online. On ten contended workloads, CoAgent stays within 5\% of serial correctness at a $1.4\times$ speedup and near-serial token cost, where 2PL and OCC surrender nearly all concurrency gains; on a bash-only target system, it grows a 25-tool library online and lifts the task pass rate from 45/71 to 63/71 at $0.80\times$ the time and $0.86\times$ the cost.

## 내 메모


