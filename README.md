# 🏅 PROJECT_HOLLA | 홀라
-------------------------

### 프로젝트 소개 및 선정 이유

- HOLLA 는 오디오북 구매 서비스 사이트인 윌라(http://www.welaaa.com/)을 클론 하였습니다.
- 기간의 제약으로 인해 전체 클론보다는 핵심적인 기능 위주로 클론하였으며,
  기획 단계에서 배포까지 프로젝트를 진행하였습니다. 

-------------------------

### 🎯 HOLLA UI/UX/API 메인 서비스

+ 카카오 소셜 로그인 서비스를 제공합니다.
+ 기간별(월 단위) 추천 오디오북 서비스를 제공합니다.
+ 유저 구매 목록을 기반으로 관심있는 장르 오디오북 추천 서비스를 제공합니다.
+ 실시간 댓글이 달린 오디오북 추천 서비스를 제공합니다.
+ 오디오북에 대한 별점을 줄 수 있고 전체 평균값을 제공합니다.
+ 댓글 기능으로 오디오북에 대한 소감 및 평가를 작성할 수 있습니다.
+ 장바구니 기능을 통해 원하는 오디오북을 구매할 수 있습니다.

-------------------------

### 🎀 TEAM_HOLLA

* 개발 기간
    * 기간: 2021년 11월 15일 ~ 2021년 11월 26일(12일간)

* MEMBER
    * 개발인원 : 프론트엔드 4명, 백엔드 2명
        * Project Master : 유병문
        * Front-end : 장세영, 이수경, 정지후, 설혜린
        * Back-end  : 김봉철, 유병문

* 적용 기술
    * Front-end: JavaScript, React.js, SASS, React-Router-Dom, React-icons
    * Back-end: Django, Python, MySQL, jwt, bcrypt, AWS RDS, EC2, Docker
    * 협업툴: Trello, Slack, Notion, Git, Ddiagram, Postman

-------------------------

### 🎫 구현 기능 및 개인 역할

* 김봉철
    * DB 모델링, DB 구현, CSV 제작 관리 및 최신화    
    * KaKao Social 로그인/회원가입, 인증/인가 API 구현
    * 메인페이지
        * 오디오북을 랜덤하게 추천하는 API 구현
        * 구매한 상품의 장르를 기반으로 하는 추천 API 구현
        * 실시간 감상평을 기준으로 화면에 보여주는 API 구현
    * 리뷰페이지
        * 상품별 별점 등록 및 출력 API 구현
        * 리뷰 등록 및 출력 API 구현
    * Unit Test 구현

* 유병문
    * PROJECT 기획 및 기간 별 TRELLO 관리
    * DB 모델링, DB 구현, db_uploader 구현, CSV 제작 관리 및 최신화
    * 상세페이지
        * 오디오북 정보 및 작가 정보 API 구현
    * 장바구니 페이지
        * 오디오북 상품 등록 API 구현
        * 상품 총 갯수 및 총 가격 API 구현
    * Unit Test 구현

TEAM HOLLA [시연 영상](https://drive.google.com/file/d/1bLdBu8gRKcWSNu3r1vyPwUhUobkm4Qt-/view?usp=sharing)

-------------------------

### 레퍼런스
이 프로젝트는 윌라 사이트를 참조하여 학습목적으로 만들었습니다.
실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.