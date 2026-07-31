# Executive Summary

## 결론

**네. 다른 개인 연구자와 오픈소스 프로젝트도 거의 같은 구조를 사용하고 있습니다.** 특히 2026년 7월 공개된 `read-summarize-papers`는 arXiv·Zotero에서 자료를 가져와 SQLite에 처리 상태를 저장하고, DOI·arXiv ID·제목·콘텐츠 해시로 중복을 걸러낸 뒤, 관련도에 따라 요약 수준을 나누고 Obsidian에 구조화 노트를 생성합니다. 현재 작업공간에서 만든 수집기와 매우 가까운 독립 구현입니다. (clm_001; src_006, src_007; [read-summarize-papers](https://github.com/Angelamer/read-summarize-papers), [ResearchPilot](https://arxiv.org/abs/2603.14629))

다만 현재 구현은 아직 **수집 DB + 일일 한국어 종합** 단계입니다. 다른 구현처럼 완성하려면 자료마다 버전이 있는 한국어 요약을 저장하고, 채택한 자료마다 Obsidian 소스 노트를 하나씩 생성하는 계층이 더 필요합니다.

## 개인 연구에 권하는 역할 분담

- **SQLite:** 모든 후보 자료, 중복, 수집 이력, 관련도, AI 요약 버전, 처리 상태
- **Zotero:** 실제 보관·읽기·인용할 논문과 PDF, 서지정보와 주석
- **Obsidian:** 한국어 자료별 노트, 내 생각, 주제 간 연결, 일일·주간 종합
- **Codex:** 매일 수집, 중복 제거, 우선순위 판정, 구조화 요약, 링크 생성

Zotero를 서지·첨부물 저장소로, Obsidian을 사람이 읽고 편집하는 지식 계층으로 두는 분업은 Zotero API, Obsidian의 로컬 Markdown 구조, ZotFlow의 실제 구현과 맞습니다. (clm_002; src_001, src_002, src_005; [Zotero API](https://www.zotero.org/support/dev/web_api/v3/basics), [Obsidian data storage](https://obsidian.md/help/data-storage), [ZotFlow](https://github.com/duanxianpi/zotflow))

## 현재 구현에 대한 판정

방향은 맞습니다. 전부 새로 바꿀 필요는 없고 다음 두 가지를 추가하면 됩니다.

1. SQLite에 `item_summaries`와 사람 검토 상태를 추가한다.
2. 채택된 자료마다 `vault/Sources/`에 한국어 Markdown 노트를 생성하고 일일 브리핑은 그 노트들을 링크한다.

PDF 전체 문장을 근거로 질의응답하고 싶어질 때만 벡터/전문검색 계층을 추가하는 것이 적절합니다. PaperQA2와 OpenScholar도 서지 DB와 별개로 전문 인덱스·근거 구간·인용 추적을 둡니다. (clm_006; src_008, src_009; [PaperQA2](https://github.com/future-house/paper-qa), [OpenScholar](https://www.nature.com/articles/s41586-025-10072-4))
