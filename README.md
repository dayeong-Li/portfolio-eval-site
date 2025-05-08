# 포트폴리오 평가 웹사이트

Django 기반의 웹 애플리케이션으로, 사용자들이 포트폴리오 프로젝트에 점수를 매기고 평균 점수를 확인할 수 있습니다.

## 주요 기능
- 프로젝트 목록 및 상세 페이지 조회
- 점수 평가 기능 (1점 ~ 5점)
- 평균 점수 계산 및 리스트 출력

## 실행 방법

### 🔹 도커(Docker)로 실행
```bash
git clone https://github.com/dayeong-Li/portfolio-eval-site.git
cd portfolio-eval-site
sudo docker-compose up --build
```

### 🔹 가상환경에서 직접 실행
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

접속 주소: http://localhost:8000

## 개발 환경
- Python 3.10
- Django 5.2.1
- Docker / Docker Compose

## 라이선스
MIT License
