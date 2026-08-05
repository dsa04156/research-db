# 개인 연구 DB

Codex가 매일 논문, 공식 기술 블로그, 업계 분석, GitHub 릴리스를 수집해
SQLite에 합치고 한국어 Markdown 브리핑을 만드는 개인 연구 시스템입니다.
Zotero는 읽기 목록과 인용 관리용 동기화 대상으로 사용합니다.

## 수집 범위

- Self-evolving harness, harness engineering, context engineering
- AI agent, tool use, memory, evaluation, observability
- Kubernetes, cloud-native AI infrastructure, GPU scheduling
- Cloud, serverless, distributed systems, platform engineering
- Edge computing, edge AI, distributed inference

기준 시드는 Lilian Weng의
[Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/)입니다.

자료 유형과 품질 표시는 다음과 같습니다.

- A: 논문 메타데이터, 공식 프로젝트·벤더 블로그, 공식 GitHub 릴리스
- B: 편집형 업계 분석과 검증된 커뮤니티 기술 글
- 웹 트렌드: 매일 최근 24시간, 화요일에는 최근 7일의 원문과 날짜를 확인해 보강 수집

RSS에는 Kubernetes, CNCF, Cloudflare, NVIDIA, GitHub AI/ML, Docker,
Red Hat Developer, Hugging Face, The New Stack, InfoQ가 포함됩니다.
OpenAI, Anthropic, Google DeepMind, AWS, Google Cloud와 독립 기술 블로그는
매일 웹 검색으로 보강합니다. 범용 피드는 제목과 본문이 관심 키워드에 실제로
맞을 때만 저장합니다.

## 중복 제거와 저장 구조

같은 자료는 다음 순서로 한 항목에 합칩니다.

1. DOI
2. arXiv ID
3. 추적 파라미터를 제거한 canonical URL
4. 정규화 제목과 연도

원시 자료와 발견 이력은 `data/research.db`, 사람이 읽는 결과는
`vault/Daily/YYYY-MM-DD.md`에 저장됩니다. 같은 자료가 다른 출처에서 다시
발견되면 새 항목 대신 `sightings`만 늘어납니다.

SNS는 Threads, LinkedIn, Reddit, Hacker News, YouTube, TikTok, Instagram까지 최근 30일 신호를
확장 수집합니다. X는 사용자 선택에 따라 제외되어 있습니다. SNS 글은 기본적으로
`metadata.evidence_role=lead_only`로 저장되어 사실 근거가 아니라 트렌드 신호로
취급합니다.

- 글이 논문, 공식 블로그, 릴리스를 링크하면 `url`에는 원문을, `source_url`에는
  SNS 글을 넣습니다. 기존 원문과 일치하면 새 자료를 만들지 않고 `sightings`만
  추가합니다.
- SNS 자체 글만 있으면 DB에는 남지만 원문 확인 전 신호로 표시되고 Zotero에는
  보내지 않습니다.
- 나중에 같은 URL의 공식 자료가 들어오면 SNS 전용 상태가 해제되고 공식 자료로
  승격됩니다.
- LinkedIn은 공식 API의 임의 공개 글 전체검색이 아니라 공개 검색엔진 색인 범위,
  Threads는 공개 키워드 검색 범위이므로 완전한 전수조사는 아닙니다.

`last30days`의 stable agent JSON 결과는 다음처럼 병합합니다.

Threads처럼 짧은 검색어만 안정적으로 처리하는 플랫폼에는 긴 공통 질의를
그대로 넘기지 않습니다. `config/research.json`의 `platform_queries`에 핵심
검색어를 여러 개 정의하고 다음 명령으로 결정적인 실행 계획을 만듭니다.

```powershell
python scripts\research_db.py social-plan --platform threads
```

출력되는 각 검색어는 Threads의 2단어 제한에 맞으며 원래 질의, 축약 여부,
주제 힌트를 함께 보존합니다. 특정 공개 계정을 계속 관찰할 때는
`social_research.watch_queries`에 `platform`, `query`, `topic_hints`를 추가하면
같은 계획에 포함됩니다.

```powershell
python scripts\research_db.py ingest-social-report `
  --input tmp\social-agent-harness.json `
  --topics self-evolving-harness,ai-agents
```

자동화가 SNS 글의 외부 원문을 확인했다면 JSON 결과 항목에 `primary_url`을
추가한 뒤 병합합니다. 그러면 원문은 DB의 대표 URL, SNS 글은 발견 이력으로
보존됩니다.

## 트렌드 레이더

고정 검색어 수집과 별개로, `last30days` 발견 모드를 사용해 관심 분야에서 갑자기
언급이 늘어난 기술·프로젝트·논쟁을 찾습니다. 매일은 최근 24시간을 직전 14일과
비교해 최대 3개만 브리핑에 싣고, 화요일에는 최근 7일 흐름을 최대 7개까지
심층 확인합니다. X는 모든 트렌드 조사에서 제외합니다.

단일 SNS 글이나 조회 수만으로는 트렌드로 확정하지 않습니다. 서로 독립적인 공개
플랫폼 2곳 이상에서 확인되거나, 공식 원문과 커뮤니티 반응이 함께 있을 때만
확인된 흐름으로 표시합니다. 나머지는 `lead_only` 약한 신호로 분리하고 Zotero에는
보내지 않습니다. 믿을 만한 신규 흐름이 없으면 브리핑에 `뚜렷한 신규 트렌드 없음`이라고
짧게 기록합니다.

## 초기 DB 구축

초기 자료는 최근 3년을 1년 단위로 나눠 수집하는 것을 권장합니다. 연도별로
나누면 API가 최신 결과만 반환해서 과거 자료가 빠지는 문제를 줄일 수 있습니다.
`--max-results`는 해당 실행에만 적용되므로 매일 실행되는 가벼운 수집량에는
영향을 주지 않습니다.

```powershell
python scripts\research_db.py collect --since 2023-07-30 --until 2024-07-29 --max-results 100
python scripts\research_db.py collect --since 2024-07-30 --until 2025-07-29 --max-results 100
python scripts\research_db.py collect --since 2025-07-30 --until 2026-07-30 --max-results 100
python scripts\research_db.py reclassify
python scripts\research_db.py digest
```

DB에는 전체 자료를 보존하고, 일일 Markdown에는 주제별 관련도 상위
`digest_max_per_topic`개만 표시합니다.

## 기본 명령

```powershell
python scripts\research_db.py init
python scripts\research_db.py ingest-jsonl --input config\seeds.jsonl
python scripts\research_db.py collect --days 7
python scripts\research_db.py reclassify
python scripts\research_db.py digest
python scripts\research_db.py obsidian-export
python scripts\research_db.py status
```

`digest`는 기본적으로 Obsidian 그래프 내보내기도 함께 실행합니다. DB의 활성
자료는 `vault/Sources/`, 관심 분야 허브는 `vault/Topics/`, 시작점은
`vault/Research Graph.md`에 생성됩니다. 개별 자료 노트의 `내 메모` 아래에
작성한 개인 메모는 다음 자동 갱신에서도 보존됩니다.

매일 자동화는 신규 자료 중 핵심 5개를 골라 한국어 분석을 일일 노트에 작성하고,
주간 자동화는 화요일마다 `vault/Synthesis/YYYY-Www.md`에 합의점, 충돌,
인프라 영향과 다음 조사 질문을 종합합니다.

매일 읽을 화면은 `vault/오늘의 브리핑.md` 하나입니다. 이 노트는 최신
`vault/Briefings/YYYY-MM-DD.md`를 바로 보여주며, 긴 원본 다이제스트를
아래까지 내릴 필요가 없습니다.

## Zotero 연결

Zotero 웹 설정에서 개인 라이브러리 읽기·쓰기 권한이 있는 전용 API 키를 만든 뒤,
작업 폴더 터미널에서 다음 명령을 실행합니다.

```powershell
python scripts\research_db.py zotero-configure
```

숨겨진 입력 프롬프트에 키를 붙여넣으면 다음 Windows 사용자 환경변수로
영구 저장됩니다. 키는 명령 기록이나 프로그램 출력에 표시되지 않습니다.

- `ZOTERO_USER_ID`
- `ZOTERO_API_KEY`

연결과 동기화:

```powershell
python scripts\research_db.py zotero-status
python scripts\research_db.py zotero-sync --date 2026-07-30
python scripts\research_db.py zotero-sync --limit 100
```

동기화는 Zotero의 `Codex Research Inbox` 컬렉션을 사용합니다. 기존 Zotero
항목과 DOI, arXiv ID, URL, 정규화 제목, Codex 키를 비교하여 이미 있는 자료는
다시 만들지 않습니다. 논문은 journal article/preprint, 블로그는 blog post,
릴리스와 기타 웹 자료는 webpage로 저장합니다. PDF 첨부 파일은 자동 업로드하지
않습니다.

기타 선택 환경변수:

- `OPENALEX_API_KEY`
- `GITHUB_TOKEN`
- `CROSSREF_MAILTO`

## 매일 자동 실행

Codex 자동화는 매일 오전 8시에 다음을 수행합니다.

1. 정형 API, RSS, GitHub 릴리스를 수집합니다.
2. 출처 유형과 품질 등급을 보존하며 중복을 합칩니다.
3. 최근 24시간 자료와 직전 14일을 비교해 상승 중인 트렌드를 최대 3개 찾습니다.
4. 한국어 일일 브리핑과 `트렌드 레이더`를 작성합니다.
5. Obsidian 주제·자료 노트와 그래프 링크를 갱신합니다.
6. 새 자료를 Zotero에 중복 없이 동기화합니다.
7. 신규·중복·필터·오류·Zotero 결과를 보고합니다.

화요일에는 이 일일 실행 뒤에 최근 7일 심층 조사와 주간 종합을 추가로 수행합니다.
