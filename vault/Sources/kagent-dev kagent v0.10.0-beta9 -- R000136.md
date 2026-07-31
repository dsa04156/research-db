---
type: research-source
item_id: 136
title: "kagent-dev/kagent v0.10.0-beta9"
source: "github-release"
published: "2026-07-21T16:59:56Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:709fe5dd2f885d9cd9427b92bd5623cd46dc1d3f01d896dfae2b433c6deb9c47"
url: "https://github.com/kagent-dev/kagent/releases/tag/v0.10.0-beta9"
generated_by: codex-research-db
aliases:
  - "kagent-dev/kagent v0.10.0-beta9"
topics:
  - "kubernetes"
  - "ai-agents"
---

# kagent-dev/kagent v0.10.0-beta9

[원문 열기](https://github.com/kagent-dev/kagent/releases/tag/v0.10.0-beta9)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `github-release`
- 검토 상태: `pending`
- Zotero: created (`FRN53ECD`)
- 발행일: 2026-07-21T16:59:56Z
- 저자: github-actions[bot]
- 식별자: `url:709fe5dd2f885d9cd9427b92bd5623cd46dc1d3f01d896dfae2b433c6deb9c47`

## 요약·초록

## What's Changed ### Features * feat(helm): bump bundled oauth2-proxy subchart to ~10.7.0 by @elihai-risk in https://github.com/kagent-dev/kagent/pull/2254 * feat: default nodeSelector for agent deployments (--default-agent-node-selector) by @elihai-risk in https://github.com/kagent-dev/kagent/pull/2259 * feat(helm): add podLabels for controller and UI pod templates by @elihai-risk in https://github.com/kagent-dev/kagent/pull/2237 * feat(helm): add extraObjects for arbitrary manifests by @younsl in https://github.com/kagent-dev/kagent/pull/2174 * feat(ui-test): Playwright ui tests foundation stage 0 by @cjlg-soloio in https://github.com/kagent-dev/kagent/pull/2262 ### Bug Fixes * fix(ui): fix model name editing on the model config form by @Valyrian-Code in https://github.com/kagent-dev/kagent/pull/1979 * fix: correct package comment in v1alpha2 groupversion_info by @mesutoezdil in https://github.com/kagent-dev/kagent/pull/2183 * fix(crewai): unwrap Part before DataPart check so structured inputs are used by @anxkhn in https://github.com/kagent-dev/kagent/pull/2231 * fix(helm): expose nodeSelector and tolerations for kagent-tools subchart by @the-mentor in https://github.com/kagent-dev/kagent/pull/2213 * fix(helm): make the cluster DNS domain configurable by @shekhargit1912 in https://github.com/kagent-dev/kagent/pull/2209 * fix: parse migration filenames the same way golang-migrate does by @mesutoezdil in https://github.com/kagent-dev/kagent/pull/2194 * fix: build sandbox runtime outside QEMU emulation by @peterj in https://github.com/kagent-dev/kagent/pull/2299 * fix: set kgateway.dev/a2a as appProtoco for BYO agents by @supreme-gg-gg in https://github.com/kagent-dev/kagent/pull/2305 ### Documentation * docs: point prompt template integration link to compiler by @anxkhn in https://github.com/kagent-dev/kagent/pull/2228 * docs: add STYLE.md with Go style guide by @EItanya in https://github.com/kagent-dev/kagent/pull/2186 * docs: fix stale architecture references by @mesutoezdil in https://github.com/kagent-dev/kagent/pull/2308 ### Other Changes * chore(deps): update langsmith[otel] requirement from >=0.9.8 to >=0.10.2 in /python by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2220 * chore(deps): bump the python-minor-patch group in /python with 4 updates by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2219 * chore(deps): bump distroless/cc-debian12 from `b0ae8e9` to `ce0d66b` in /python by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2216 * chore(deps): bump node from `b16ca7b` to `e999d08` in /python by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2215 * chore: upgrade google.golang.org/adk to v2.0.0 by @yanivmn in https://github.com/kagent-dev/kagent/pull/2152 * fixes empty secretkeyref in azureopenai by @peterj in https://github.com/kagent-dev/kagent/pull/2225 * add 'none' as an option for reasoning effort, update models across by @peterj in https://github.com/kagent-dev/kagent/pull/2227 * chore: add @Charlesthebird as CODEOWNER for .github/ by @Charlesthebird in https://github.com/kagent-dev/kagent/pull/2243 * ci: read go version from go.mod in sqlc check by @mesutoezdil in https://github.com/kagent-dev/kagent/pull/2235 * feat (UI): improve UX by grouping tool calls in the chat by @peterj in https://github.com/kagent-dev/kagent/pull/2224 * mark agent as ready when at least one replica is available by @peterj in https://github.com/kagent-dev/kagent/pull/2263 * fix droping an MCP toolset when the MCP server isn't reachable at startup by @peterj in https://github.com/kagent-dev/kagent/pull/2256 * chore(deps): bump the go-minor-patch group across 1 directory with 7 updates by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2218 * clean up and move the agent creation functions into a single file by @peterj in https://github.com/kagent-dev/kagent/pull/2252 * Reference declarative agents by tag; digests only for sandbox agents by @iplay88keys in https://github.com/kagent-dev/kagent/pull/2242 * chore(substrate): Bump substrate to `v0.0.9` and remove collapsing of image env into actor env by @jmhbh in https://github.com/kagent-dev/kagent/pull/2208 * chore(ui): pin packageManager to npm@11.6.2 by @cjlg-soloio in https://github.com/kagent-dev/kagent/pull/2271 * chore(deps): bump the go-minor-patch group in /go with 6 updates by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2291 * chore(deps): bump actions/upload-artifact from 4 to 7 by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2290 * ci: improve build caching and cancel stale runs by @peterj in https://github.com/kagent-dev/kagent/pull/2301 * chore(deps): bump actions/setup-go from 6 to 7 by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2289 * chore(deps): bump actions/setup-node from 6 to 7 by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2292 * chore(deps): update langsmith[otel] requirement from >=0.10.2 to >=0.10.6 in /python by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2296 * chore(deps): bump debian from `28de087` to `020c0d2` in /python by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2288 * chore(deps): bump distroless/cc-debian12 from `ce0d66b` to `66aa873` in /python by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2287 * chore(deps): bump node from `e999d08` to `2d49d87` in /python by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2286 * chore(deps): bump the python-minor-patch group in /python with 4 updates by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2294 * chore(deps): update anthropic[vertex] requirement from >=0.116.0 to >=0.117.0 in /python by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2295 * Bump minimum python version to 3.11 by @iplay88keys in https://github.com/kagent-dev/kagent/pull/2275 * chore(deps): bump the npm-minor-patch group in /ui with 27 updates by @dependabot[bot] in https://github.com/kagent-dev/kagent/pull/2293 ## New Contributors * @Valyrian-Code made their first contribution in https://github.com/kagent-dev/kagent/pull/1979 * @elihai-risk made their first contribution in https://github.com/kagent-dev/kagent/pull/2254 * @shekhargit1912 made their first contribution in https://github.com/kagent-dev/kagent/pull/2209 * @cjlg-soloio made their first contribution in https://github.com/kagent-dev/kagent/pull/2271 **Full Changelog**: https://github.com/kagent-dev/kagent/compare/v0.10.0-beta7...v0.10.0-beta9

## 내 메모


