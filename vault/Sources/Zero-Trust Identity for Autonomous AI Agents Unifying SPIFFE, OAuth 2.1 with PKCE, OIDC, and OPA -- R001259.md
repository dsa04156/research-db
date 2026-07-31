---
type: research-source
item_id: 1259
title: "Zero-Trust Identity for Autonomous AI Agents: Unifying SPIFFE, OAuth 2.1 with PKCE, OIDC, and OPA in Multi-Agent Architectures"
source: "openalex"
published: "2026-05-23"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.32628/cseit2612335"
url: "https://doi.org/10.32628/cseit2612335"
generated_by: codex-research-db
aliases:
  - "Zero-Trust Identity for Autonomous AI Agents: Unifying SPIFFE, OAuth 2.1 with PKCE, OIDC, and OPA in Multi-Agent Architectures"
topics:
  - "ai-agents"
---

# Zero-Trust Identity for Autonomous AI Agents: Unifying SPIFFE, OAuth 2.1 with PKCE, OIDC, and OPA in Multi-Agent Architectures

[원문 열기](https://doi.org/10.32628/cseit2612335)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`WE7QH5MX`)
- 발행일: 2026-05-23
- 저자: Venkata Krishna Prasanth Budigi, Maheshbabu Dhanekula, Siri Chandana Sirigiri, Srinivas Rao Marri
- 식별자: `doi:10.32628/cseit2612335`

## 요약·초록

The rapid adoption of autonomous AI agents in distributed microservices architectures introduces a critical and largely unsolved security challenge: how to establish, verify, and enforce identity across every layer of an agentic workflow. In traditional systems, identity management addresses two well-understood dimensions: human user identity (authenticated via passwords, single sign-on, or multi-factor mechanisms) and a limited number of service identities (managed through static API keys or long-lived service accounts). These approaches suffice when services execute predetermined logic on behalf of known callers. However, the emergence of agentic workflows, where autonomous agents reason, invoke tools, and chain multi-step actions across service boundaries, fundamentally changes the identity landscape. Each agent workload requires its own cryptographically verifiable workload identity, and the system must maintain governed identity propagation that securely carries both the originating user’s authorization context and the calling service’s identity through every hop of the request chain, all while preserving secure session state across process boundaries and service restarts. Moreover, just as APIs are classified into public, protected, and private tiers with progressively stricter access controls, agents must be similarly classified: public agents accessible to any authenticated user, protected agents restricted to users with specific roles, and private agents accessible only through authorized internal services with both valid user credentials and verified workload identity. We present AgentSecurity, a production-ready framework that unifies three complementary standards to achieve zero-trust identity with governed identity propagation for multi-agent systems: (1) OAuth 2.1 with Proof Key for Code Exchange (PKCE) for secure human authentication via OpenID Connect (OIDC), with disk-persisted session state that survives process restarts, eliminating authorization code interception attacks; (2) SPIFFE JWT-SVIDs (JSON Web Token-based SPIFFE Verifiable Identity Documents) for cryptographic workload identity, replacing heavyweight X.509 mutual TLS (mTLS) with lightweight, audience-scoped, short-lived JWTs that give every agent its own verifiable identity; and (3) the Open Policy Agent (OPA) for declarative, two-dimensional authorization that jointly evaluates user roles and caller service identity in a single policy decision, ensuring that identity propagation is governed at every trust boundary. We demonstrate this framework on a real multi-agent platform comprising LangGraph agents orchestrated via the Model Context Protocol (MCP), where every inter-service call carries both a user identity token and a workload identity token, propagating the user’s authorization context through the entire agentic pipeline. Every access decision is governed by auditable, version-controlled Rego policies. Our evaluation shows that the framework adds less than 12 ms of latency overhead per request while providing four independent authentication layers, fail-closed authorization, and automatic credential rotation. A complete reference implementation is available at https://github.com/krishna1501/AgentSecurity.

## 내 메모


