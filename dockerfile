# 베이스 이미지
FROM python:3.12

# 환경 변수 설정
# 요약: 배포 시나리오에 최적화하기 위해 파일 쓰기를 최소화하고 버퍼링 없이 즉시 출력을 보장
# Python이 디스크에 pyc 파일(바이트코드)을 쓰지 않도록 합니다. 1로 설정되면 Python이 
# 컴파일된 바이트코드 파일을 생성하지 않도록 하며, 이는 불필요한 파일 쓰기를 줄이고 성능을 향상
ENV PYTHONDONTWRITEBYTECODE 1
# Python에 대한 버퍼 없는 모드를 활성화하기 위해 1로 설정됩니다. 버퍼 없는 모드에서는 Python이 
# 표준 스트림(stdout 및 stderr)을 버퍼링하지 않으므로 즉시 출력
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 소스 코드 및 Python 파일들 복사
COPY . /app/

# SQLite3 설치
RUN apt-get update && apt-get install -y sqlite3

# 데이터베이스 초기화
RUN python manage.py migrate

# collectstatic 명령은 Django 애플리케이션에서 사용하는 정적 파일들을 한 곳에 모아주는 역할을 합니다. 
# 이는 개발 환경에서는 불필요할 수 있지만, 프로덕션 환경에서는 필요한 과정
# 정적 파일들을 한 곳에 모아 서빙하면 웹 서버(예: Nginx, Apache)가 해당 디렉터리를 통해 정적 파일을
# 효율적으로 서빙할 수 있습니다. 여러 파일들이 분산된 상태로 서빙하는 것보다 성능상 이점이 있습니다.
RUN python manage.py collectstatic --noinput

# Node.js 및 npm 설치
# RUN apt-get install -y nodejs npm

# gunicorn 설치 : Nginx는 Gunicorn과 같은 WSGI 서버를 프록시로 사용하여 파이썬 애플리케이션을 처리한다.
RUN pip install gunicorn

# 실행 명령
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
