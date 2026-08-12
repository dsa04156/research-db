---
type: research-source
item_id: 1893
title: "MiDojo: Improve AI agent security with real-world red-teaming"
source: "rss:Red Hat Developer Blog"
published: "2026-08-10T07:01:20+00:00"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "url:39c96d63344583e9a784234d28f14dd153fa85ea589778dcc5a471dc5467f5ab"
url: "https://developers.redhat.com/articles/2026/08/10/midojo-improve-ai-agent-security-real-world-red-teaming"
generated_by: codex-research-db
aliases:
  - "MiDojo: Improve AI agent security with real-world red-teaming"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# MiDojo: Improve AI agent security with real-world red-teaming

[원문 열기](https://developers.redhat.com/articles/2026/08/10/midojo-improve-ai-agent-security-real-world-red-teaming)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `rss:Red Hat Developer Blog`
- 검토 상태: `pending`
- Zotero: created (`CZET2VTX`)
- 발행일: 2026-08-10T07:01:20+00:00
- 저자: Red Hat
- 식별자: `url:39c96d63344583e9a784234d28f14dd153fa85ea589778dcc5a471dc5467f5ab`

## 요약·초록

The "bring your own agent" (BYOA) approach lets you build with your preferred framework while relying on Red Hat AI for enterprise identity, isolation, guardrails, and observability—a model we recently detailed in our BYOA operationalization guide . But there's a question before any agent should touch production data: will this agent do something unintended when someone attacks it? Not the model—the agent. The whole system of model, tools, and data working together. We built MiDojo to answer that question. It's an open source framework for red-teaming AI agents in the environment where they run. In this post, we'll explain why agent-level adversarial testing differs from model-level testing and how MiDojo applies Red Hat's BYOA principle to security testing. Agent security is a system-level property Tool-using agents are vulnerable to prompt injection: adversarial instructions delivered through their inputs, or hidden in the data they read while doing legitimate work. The second kind, an indirect attack, can reside in a calendar invite the agent reads, a log line it summarizes, a database record it looks up, or the response of a compromised tool call. Resisting these attacks is a system-level property—it depends on the model, its harness, the tools it can call, the data sources it can reach, and the interactions among these components. You can scan a model for jailbreak susceptibility, yet a model passing a scan can still fail the moment you wire it to a tool reading poisoned data. The critical question is whether the whole system resists attacks planted anywhere across its operating context. We borrow this framing from AgentDojo , which pioneered planting attacks in the agent's environment. AgentDojo's limitation is its simulated nature: you rebuild the agent's entire world inside the framework. This setup means you're testing a copy of your agent, not the agent you're about to deploy. Test the agent you brought, not a simulation of it MiDojo instead takes the BYOA principle and applies it to agent security by bringing the red-teaming into the agent's real environment. As shown in Figure 1, MiDojo uses an interception layer to sit between the agent and real-world tools through a man-in-the-middle design. It interposes a layer of fake tools between your agent and the real world. Each fake tool independently decides what to do: forward the call to the real tool for authentic data, splice an attack payload into the response, capture the agent's actions, or any combination. Figure 1: MiDojo interposes fake tools between an agent and external systems to inject attack payloads into tool responses and evaluate agent resilience. The interception layer takes whatever shape your agent already expects—a stand-in server for agents speaking the Model Context Protocol (MCP), or a fake extension for agent runtimes with pluggable tools. Either way, the agent doesn't change. It doesn't even know you're testing it. Test against the most important vulnerabilities Most agent builders aren't security researchers, and they shouldn't have to be. MiDojo's attack payloads come from a library tagged against the Open Worldwide Application Security Project (OWASP) Agentic Security Initiative threat taxonomy, so you're testing against established vulnerability classes rather than inventing attack scenarios from scratch. The library is also separate from the test suites themselves: what you're testing stays stable while the attacks evolve, and you can pull in probes from existing catalogs like garak (an open source vulnerability scanner for LLMs) and deliver them through the same interception layer. Measure security and utility together Every MiDojo evaluation reports 2 independent scores: did the agent resist the attack (security), and did it still complete its task (utility)? This dual grading is another idea MiDojo carries over from AgentDojo. This setup makes the security-utility tradeoff visible: a defense blocking attacks by making the agent useless isn't much of a defense—but in some high-stakes situations, trading utility for security is exactly the right call. That decision belongs to you, not to the testing framework. MiDojo's job is to make both dimensions visible. One more check keeps those numbers honest: MiDojo verifies that each attack payload reached the agent during the run. If the agent never read the poisoned data, MiDojo marks the result as not applicable rather than counting it as a pass. You can't claim your agent resisted an injection it never saw. Put MiDojo to work in your environment MiDojo is open source and coming as a developer preview to Red Hat AI. The repository includes a few reference suites, plus software development kits (SDKs) for MCP-speaking agents and other agent runtimes like Pi , which powers OpenClaw, so you can wire it up to an agent you already have. Explore the MiDojo repository on GitHub and run the quick start against your own agent. Read the technical deep dive on the TrustyAI blog for the full architecture walkthrough. You brought your own agent. Before it ships, be sure to battle-test it right where it runs. The post MiDojo: Improve AI agent security with real-world red-teaming appeared first on Red Hat Developer .

## 내 메모


