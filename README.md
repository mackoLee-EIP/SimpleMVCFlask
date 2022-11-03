# 시작하기
## step 1. 가상환경 만들기
  - 독립적인 개발환경을 원하신다면 가상환경을 만든 후 실행 해주세요!
  - 참고로 제가 개발한 환경은 맥북 M1 Pro OS Monterey 입니다.
```shell
python3 -m venv ./venv
```

  - OS X 혹은 LINUX라면

```shell
. venv/bin/activate
```

  - WINDOW 라면

```shell
venv\scripts\activate 
```

## step 2. 라이브러리 설치하기
  - 쓰고싶은 가상환경을 완료했다면 아래명령을 실행시켜 필요한 라이브러리를 다운받습니다.

```shell
pip install -r requirements
```

## step 3. 어플리케이션 실행하기

```shell
python src/app.py
```

## tips
  - 개발
    - package 내의 python 파일이 package 를 찾지 못하는 경우 src 파일을 source root 설정 해주면 에러가 나지 않습니다.
  - 