---
type: research-source
item_id: 1949
title: "How to Pretty-Print Your Kubernetes YAML as KYAML and Why You'd Want To"
source: "rss:Kubernetes Blog"
published: "2026-08-11T18:00:00+00:00"
first_seen: "2026-08-12"
review_status: "pending"
canonical_key: "url:6e2f08c1e60673c44510ab5b8697128769d7a8ee3ce620b7a8081708821ed490"
url: "https://kubernetes.io/blog/2026/08/11/how-to-pretty-print-kubernetes-yaml-as-kyaml/"
generated_by: codex-research-db
aliases:
  - "How to Pretty-Print Your Kubernetes YAML as KYAML and Why You'd Want To"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# How to Pretty-Print Your Kubernetes YAML as KYAML and Why You'd Want To

[원문 열기](https://kubernetes.io/blog/2026/08/11/how-to-pretty-print-kubernetes-yaml-as-kyaml/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-08-12|2026-08-12]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- Zotero: created (`G8KTTRC8`)
- 발행일: 2026-08-11T18:00:00+00:00
- 식별자: `url:6e2f08c1e60673c44510ab5b8697128769d7a8ee3ce620b7a8081708821ed490`

## 요약·초록

YAML has been the standard way to write Kubernetes manifests for years. Every example, tutorial, and configuration file you come across is written in it. The problem isn't that YAML is a bad format. It's that YAML gives you a lot of choices, and not all of them are equally good for writing Kubernetes manifests. Some features make files harder to read, some are easy to misuse and others can lead to surprising behavior. The interesting part is that Kubernetes doesn't actually need most of those features. It only relies on a small subset of YAML. This led to a simple question: if Kubernetes only needs a small part of YAML, why not standardize on that part and avoid the rest? Instead of introducing a new configuration language, SIG CLI introduced KYAML , a stricter, more consistent way to write YAML. What is KYAML? KYAML is a strict subset (or "dialect") of standard YAML, designed to be parseable by the existing ecosystem without any changes, as proposed in KEP 5295 . It does not introduce a new format or a new parser. It just narrows the scope of choices you make when writing YAML, so everyone ends up making the same ones. Think of it less like a new language and more like an agreed-upon style. Everything valid in KYAML is valid YAML. How KYAML solves it Standard YAML has a few well-known traps and JSON is not without its own. Whitespace sensitivity. Indentation defines structure in YAML, which means a wrongly indented file can remain syntactically valid while representing a different object than intended. This gets especially painful with templating tools like Helm, where you are manipulating indentation from outside the YAML context. Silent type coercion. String quoting is optional in YAML, which sounds convenient until it is not. Some values that look like strings get coerced into other types without warning. The classic example is the "Norway Bug" . country : NO In standard YAML, NO is parsed as a boolean false , not the string "NO" and it has caught more than a few people off guard. JSON is not the answer either. It lacks comment support, is strict about trailing commas, and requires every key to be quoted, none of which makes for a good config writing experience. KYAML addresses all of these by making structure and types explicit: Does not depend on whitespace for structure Always quotes value strings so no silent type coercion Always uses {} for maps and structs Always uses [] for lists Allows comments and trailing commas, unlike JSON Includes a --- header to distinguish it from JSON at a glance, since both start with { YAML calls this flow style , as opposed to the conventional block style most people use. KYAML sits halfway between JSON and YAML, more explicit than default YAML, friendlier than JSON. Here is the same Pod manifest written in both formats for comparison. Standard YAML apiVersion : v1 kind : Pod metadata : name : my-pod labels : app : demo spec : containers : - name : nginx image : nginx:1.20 KYAML --- { apiVersion : "v1" , kind : "Pod" , metadata : { name : "my-pod" , labels : { app : "demo" , } , } , spec : { containers : [ { name : "nginx" , image : "nginx:1.20" , } ], } , } Notice the double-quoted string values, the braces around every mapping, the brackets around the list and the trailing commas. The additional syntax makes the document structure explicit instead of relying on indentation. How to pretty print YAML as KYAML There are different ways to get KYAML output. Option 1: kubectl -o kyaml Since Kubernetes 1.34, kubectl supports KYAML as a native output format. # Kubernetes 1.35+ (beta; feature enabled by default, still requires -o kyaml CLI param) kubectl get deployment my-app -o kyaml # Kubernetes 1.34 (alpha, opt-in) export KUBECTL_KYAML = true kubectl get deployment my-app -o kyaml To save the output to a file: kubectl get deployment my-app -o kyaml > my-app.yaml There are currently no plans to make KYAML the default output format. If you prefer using KYAML by default, you can configure your preferred default with kuberc . For more details, see the kuberc documentation . # Kubernetes 1.36+ kubectl kuberc set --section defaults --command get --option output = kyaml # Kubernetes 1.33–1.35 (alpha prefix still required) kubectl alpha kuberc set --section defaults --command get --option output = kyaml Option 2: Kubernetes' yamlfmt sigs.k8s.io/yaml ships a yamlfmt tool that can convert files to KYAML. Install via Go: go install sigs.k8s.io/yaml/yamlfmt@latest Running it against a file prints the KYAML version to stdout . It also accepts a directory, in which case it converts and prints every file in that directory. So you'll need to redirect the output to a file (or files) if you want the conversion to stick. yamlfmt -o = kyaml my-deployment.yaml It can also show you a diff instead of a full conversion: yamlfmt -o = kyaml -d my-deployment.yaml Option 3: Google's yamlfmt For converting existing files, Google's yamlfmt added a dedicated kyaml formatter in v0.21.0. Install via Go, or grab a binary from the releases page : go install github.com/google/yamlfmt/cmd/yamlfmt@latest It is also available as a pre-commit hook and as a Docker image for CI pipelines. Add a .yamlfmt config to your project root: formatter : type : kyaml Preview the output without modifying your file: yamlfmt -dry my-deployment.yaml then apply: yamlfmt my-deployment.yaml To convert an entire directory: yamlfmt ./k8s/ The kyaml formatter takes no additional configuration and does not share options with the default formatter so mixing them will cause an error. For more on the available modes and flags, check the command usage docs . Is KYAML worth adopting? Every valid KYAML file is a valid YAML file. So whatever you write in KYAML, your existing tools, your kubectl , your CI pipelines, none of them need to change. You can even pass KYAML as input to any version of kubectl , not just 1.34+, because at the end of the day it is just YAML. KYAML is not strictly necessary. You can keep writing block-style YAML and things will work. But it is a deliberate choice to make your configs less error-prone and more consistent especially across a team or a larger repo. It is less of a migration and more of a better habit.

## 내 메모


