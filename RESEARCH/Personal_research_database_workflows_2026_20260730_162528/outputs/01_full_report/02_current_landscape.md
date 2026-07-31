# 2. 다른 사람들의 실제 구성

## Zotero → Obsidian 분업

기존 Obsidian Zotero Integration은 Zotero의 인용·서지·주석·PDF annotation을 Obsidian으로 가져오는 역할을 한다. 최근 ZotFlow는 한 단계 더 나아가 항목마다 템플릿 기반 Markdown 소스 노트를 만들고 양방향 동기화와 충돌 처리를 제공한다. (src_004, src_005; [Obsidian Zotero Integration](https://github.com/obsidian-community/obsidian-zotero-integration), [ZotFlow](https://github.com/duanxianpi/zotflow))

검증된 결론은 다음과 같다. **Zotero는 서지정보와 첨부물의 기준 저장소로, Obsidian은 사람이 읽고 편집하는 지식 계층으로 분리하는 것이 현재 도구 생태계와 맞는다.** (clm_002; src_001, src_002, src_005)

## 현재 구현과 거의 동일한 개인 프로젝트

`read-summarize-papers`의 파이프라인은 다음과 같다.

```text
arXiv/Zotero
   ↓
SQLite 처리 상태
   ↓
개인 연구 프로필 기반 관련도 판정
   ↓
초록 요약 또는 PDF 상세 분석
   ↓
Obsidian 자료별 노트 + 연구 그래프
```

이 프로젝트는 DOI·arXiv ID·제목 지문·콘텐츠 해시로 재실행을 멱등하게 만들고, 각 Zotero key를 하나의 Obsidian 노트에 대응시킨다. ResearchPilot 역시 검색, 자료별 구조화 추출, 교차 문헌 합성, 초안 작성을 분리하며 SQLite와 Qdrant에 이력을 남긴다. 따라서 **개인 연구용으로 수집·상태 관리는 SQLite에 두고, 자료별 결과는 Obsidian Markdown으로 내보내는 공개 구현이 실제로 존재한다.** (clm_001; src_006, src_007; [read-summarize-papers](https://github.com/Angelamer/read-summarize-papers), [ResearchPilot](https://arxiv.org/abs/2603.14629))

확인된 범위에서 **두 로컬 우선 구현은 검색·수집 단계를 자료별 추출과 교차 자료 합성보다 앞에 두는 단계형 파이프라인을 사용한다.** 이는 전체 생태계의 보편 법칙이라는 뜻이 아니라, 이번에 확인한 두 구현의 공통 구조다. (clm_003; src_006, src_007)

## 문헌 검토용 AI 시스템

PaperQA2는 로컬 PDF를 인덱싱하고 Crossref·Semantic Scholar 등에서 메타데이터를 보강한 뒤, 질문별로 근거 구간을 검색·재순위화하여 인용이 있는 답을 만든다. OpenScholar도 과학 문헌 데이터 저장소, 검색기, 인용 기반 합성, 자기 피드백 루프를 별도로 둔다. (src_008, src_009; [PaperQA2](https://github.com/future-house/paper-qa), [OpenScholar](https://www.nature.com/articles/s41586-025-10072-4))
