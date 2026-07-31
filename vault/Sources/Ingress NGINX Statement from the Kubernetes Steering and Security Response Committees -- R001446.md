---
type: research-source
item_id: 1446
title: "Ingress NGINX: Statement from the Kubernetes Steering and Security Response Committees"
source: "rss:Kubernetes Blog"
published: "2026-01-29T00:00:00+00:00"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:d6c2e09dde0d19d225383ab58eafcb1ca3d8b548112fc335158bce11239cb66b"
url: "https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/"
generated_by: codex-research-db
aliases:
  - "Ingress NGINX: Statement from the Kubernetes Steering and Security Response Committees"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Ingress NGINX: Statement from the Kubernetes Steering and Security Response Committees

[원문 열기](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- Zotero: created (`SPEXKWAC`)
- 발행일: 2026-01-29T00:00:00+00:00
- 식별자: `url:d6c2e09dde0d19d225383ab58eafcb1ca3d8b548112fc335158bce11239cb66b`

## 요약·초록

In March 2026, Kubernetes will retire Ingress NGINX, a piece of critical infrastructure for about half of cloud native environments. The retirement of Ingress NGINX was announced for March 2026, after years of public warnings that the project was in dire need of contributors and maintainers. There will be no more releases for bug fixes, security patches, or any updates of any kind after the project is retired. This cannot be ignored, brushed off, or left until the last minute to address. We cannot overstate the severity of this situation or the importance of beginning migration to alternatives like Gateway API or one of the many third-party Ingress controllers immediately. To be abundantly clear: choosing to remain with Ingress NGINX after its retirement leaves you and your users vulnerable to attack. None of the available alternatives are direct drop-in replacements. This will require planning and engineering time. Half of you will be affected. You have two months left to prepare. Existing deployments will continue to work, so unless you proactively check, you may not know you are affected until you are compromised. In most cases, you can check to find out whether or not you rely on Ingress NGINX by running kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx with cluster administrator permissions. Despite its broad appeal and widespread use by companies of all sizes, and repeated calls for help from the maintainers, the Ingress NGINX project never received the contributors it so desperately needed. According to internal Datadog research, about 50% of cloud native environments currently rely on this tool, and yet for the last several years, it has been maintained solely by one or two people working in their free time. Without sufficient staffing to maintain the tool to a standard both ourselves and our users would consider secure, the responsible choice is to wind it down and refocus efforts on modern alternatives like Gateway API . We did not make this decision lightly; as inconvenient as it is now, doing so is necessary for the safety of all users and the ecosystem as a whole. Unfortunately, the flexibility Ingress NGINX was designed with, that was once a boon, has become a burden that cannot be resolved. With the technical debt that has piled up, and fundamental design decisions that exacerbate security flaws, it is no longer reasonable or even possible to continue maintaining the tool even if resources did materialize. We issue this statement together to reinforce the scale of this change and the potential for serious risk to a significant percentage of Kubernetes users if this issue is ignored. It is imperative that you check your clusters now. If you are reliant on Ingress NGINX, you must begin planning for migration. Thank you, Kubernetes Steering Committee Kubernetes Security Response Committee

## 내 메모


