---
type: research-source
item_id: 1521
title: "ray-project/ray Ray-2.56.1"
source: "github-release"
published: "2026-07-17T23:19:47Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:e3b27353733d2a7f44246817decdb89155047c1dfb66c54b7ea7d7a943ec39b3"
url: "https://github.com/ray-project/ray/releases/tag/ray-2.56.1"
generated_by: codex-research-db
aliases:
  - "ray-project/ray Ray-2.56.1"
topics:
  - "ai-agents"
  - "cloud-infrastructure"
  - "edge-computing"
---

# ray-project/ray Ray-2.56.1

[원문 열기](https://github.com/ray-project/ray/releases/tag/ray-2.56.1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `github-release`
- 검토 상태: `pending`
- Zotero: created (`WNXBWSHP`)
- 발행일: 2026-07-17T23:19:47Z
- 저자: sai-miduthuri
- 식별자: `url:e3b27353733d2a7f44246817decdb89155047c1dfb66c54b7ea7d7a943ec39b3`

## 요약·초록

# Highlights - **Ray Data**: We added fixes for several `to_pandas` regressions introduced in 2.56: an opt-out flag (`RAY_DATA_ENABLE_ARROW_BACKED_PANDAS_CONVERSION`) for Arrow-backed conversion, an int64/`double[pyarrow]` overflow crash on concatenation, and a `TensorDtype.__from_arrow__` crash on empty tensor columns (#64793, #64794). - **Ray Core**: We added early detection for system-slice memory pressure: the memory monitor now snapshots the user and system cgroup slices together and logs an error when the system slice exceeds reserved system memory, warning users to raise `--system-reserved-memory` before it causes node deaths (#64492). - **Ray Serve**: We added protobuf 7 compatibility and a routing fix for LLM direct streaming, so body-aware routers like `PrefixCacheAffinityRouter` no longer hang when `RAY_SERVE_LLM_ENABLE_DIRECT_STREAMING=1` (#64592, #64488). # Ray Data ## 🔨 Fixes - Fixed two Arrow-backed `to_pandas` regressions: added `DataContext.enable_arrow_backed_pandas_conversion` as an opt-out, and reconciled divergent numeric column types before concatenation to avoid int64/`double[pyarrow]` overflow crashes (#64793, #64768). - Fixed a `TensorDtype.__from_arrow__` crash on zero-size tensor elements by using an explicit row count instead of numpy's `-1` dimension inference (#64794, #64767). - Fixed a crash in hash partition caused by read-only hash arrays (#64584, #64552, #64559). - Nullified `_input_dependencies` in `_get_args` so exporting operator args no longer triggers an exponential `sanitize_for_struct` call chain over fused operators (#64412, #64316). # Ray Serve ## 🔨 Fixes - Added protobuf `>=7` compatibility to `_proto_to_dict` by binding to `FieldDescriptor.is_repeated` when the deprecated `label` attribute is absent (#64592, #64362). # Ray LLM ## 🔨 Fixes - Fixed direct-streaming routing for body-aware routers: the ingress now parses the raw request body into a `SimpleNamespace` over routing-key fields (`messages`, `prompt`) so `choose_replica` receives the message body instead of raw bytes (#64488, #64328, #64326). # Ray RLlib ## 🔨 Fixes - Upgraded the ONNX example from the retired MobileNet v1 to MobileNet v3 via `torchvision` and pinned `onnxscript` in the GPU/ml-build CI dep locks, fixing ONNX export failures (#64591, #64028, #64031, #64590, #64033). # Ray Core ## 💫 Enhancements - The threshold memory monitor now snapshots both the user and system cgroup slices and logs an error when system-slice usage exceeds the reserved system memory, prompting users to raise `--system-reserved-memory` (#64492). ## 🔨 Fixes - Disabled NCCL `cuMem` host buffer registration in CI pytests to stabilize GPU test runs (#64580, #64146). # Documentation ## 📖 Documentation - Repointed the ASHA Tune example links to the renamed `README` document, fixing the `fail_on_warning` ReadTheDocs build on the release line (#64761, #64630). - Updated the Python 3.10 CPU `pip freeze` dependency list for the Ray 2.56.0 release (#64447, #64357).

## 내 메모


