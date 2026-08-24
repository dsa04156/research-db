---
type: research-source
item_id: 2154
title: "How Kubernetes probes work"
source: "web:ngrok"
published: "2026-08-19"
first_seen: "2026-08-20"
review_status: "pending"
canonical_key: "url:25126c6c8bf935b4cd06017f26bcaf1236d699d09f2614bdf8086db1f0d71e38"
url: "https://ngrok.com/blog/probes"
generated_by: codex-research-db
aliases:
  - "How Kubernetes probes work"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# How Kubernetes probes work

[원문 열기](https://ngrok.com/blog/probes)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-08-20|2026-08-20]]
- 수집 채널: `web:ngrok`
- 검토 상태: `pending`
- Zotero: created (`ZJVG7UAQ`)
- 발행일: 2026-08-19
- 저자: ngrok
- 식별자: `url:25126c6c8bf935b4cd06017f26bcaf1236d699d09f2614bdf8086db1f0d71e38`

## 요약·초록

Kubernetes startup·readiness·liveness probe의 실제 동작과 잘못된 설정이 만드는 CrashLoopBackOff, rollout 중 요청 손실, graceful termination 문제를 브라우저 내 시뮬레이션과 k3s 비교로 설명한다. probe 종류마다 시작 허용 시간, Service 트래픽 포함 여부, 컨테이너 재시작 여부가 다르므로 같은 health check로 취급하면 안 된다는 운영 지침이다.

## 내 메모


