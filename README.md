# 유튜브 mp3 다운로더

## Getting Started / 어떻게 시작하나요?

### Prerequisites / 선행 조건

아래 사항들이 설치가 되어있어야합니다.

```
youtube-dl==2021.6.6
wget==3.2
google-api-python-client==2.10.0
oauth2client==4.1.3
youtube-search-python==1.4.6
```

### Installing / 설치

아래 사항들로 현 프로젝트에 관한 모듈들을 설치할 수 있습니다.

pip install -r requirements.txt

### 구현방법

```
youtubesearchpython 라이브러리로 유튜브 api 키 없이
영상 mp3를 추출할수있도록 만들었습니다.

만약 유뷰브링크를 입력하지않고 영상제목을 입력했을때는
youtube_dl라이브러리를 사용하여 영상 제목에대한 url id를 추출하여
다운로드를 진행하게 됩니다.
```

### 테스트는 이런 식으로 작성하시면 됩니다

```
유튜브 링크 or 영상제목
```

## License / 라이센스

이 프로젝트는 AGPL-3.0 License 라이센스가 부여되어 있습니다.