"""
config 프로젝트의 Django 설정 파일입니다.

Django 4.0.3 버전을 사용하여 'django-admin startproject' 명령으로 생성되었습니다.

더 많은 설정 파일 정보는 다음 링크에서 확인하세요:
https://docs.djangoproject.com/en/4.0/topics/settings/

전체 설정 목록 및 값은 다음 링크에서 확인하세요:
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# 프로젝트 내부에서 경로를 구성할 때 이렇게 사용합니다: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# 빠른 개발 환경 설정 - 운영에는 사용하지 않습니다.
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: 실제 운영에서 사용할 때에는 비밀 키를 보호하세요!
SECRET_KEY = 'django-insecure-gb9$dmul_xcb2*d0$bks5@$r3%uj01x_b%88^8jr81nf8v_!f0'

# SECURITY WARNING: 운영 시에는 디버그 모드를 비활성화하세요!
DEBUG = True

# 허용된 호스트 목록 - [] 서버는 모든 호스트로부터의 요청을 허용(개발환경에서 쓰는설정)
'''실제 운영 환경에서는 특정 도메인이나 IP 주소를 명시적으로 설정하는 것이 안전합니다. 
Nginx를 사용하는 경우, 해당 도메인이나 IP 주소를 ALLOWED_HOSTS에 추가하는 것이 일반적'''
ALLOWED_HOSTS = []

# 애플리케이션 정의
# INSTALLED_APPS 설정은 이러한 앱들을 등록하여 Django가 해당 앱을 식별하고 
# 사용할 수 있도록 합니다.
INSTALLED_APPS = [
    # common 앱의 CommonConfig 클래스를 사용
    'common.apps.CommonConfig',
    # movie 앱의 movieConfig 클래스를 사용
    'movie.apps.movieConfig',
    # 장고 rest 프레임워크
    'rest_framework',
    # Django 관리자 기능을 사용하기 위한 앱
    'django.contrib.admin',
    # 사용자 인증 및 권한 관리를 담당하는 앱
    'django.contrib.auth',
    # 컨텐츠 유형(content type)을 위한 앱
    'django.contrib.contenttypes',
    # 세션 관리를 위한 앱
    'django.contrib.sessions',
    # 메시지 프레임워크를 사용하기 위한 앱
    'django.contrib.messages',
    # 정적 파일 서빙을 위한 앱
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    # 보안과 관련된 설정을 다루는 미들웨어입니다.
    'django.middleware.security.SecurityMiddleware',
    # 세션 관리를 담당하는 미들웨어입니다.
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 여러 기능을 갖춘 미들웨어로, 예를 들어 URL 리디렉션과 같은 기능을 수행
    'django.middleware.common.CommonMiddleware',
    # CSRF(Cross-Site Request Forgery) 보호를 위한 미들웨어입니다.
    'django.middleware.csrf.CsrfViewMiddleware',
    # 사용자 인증을 처리하는 미들웨어입니다.
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 메시지 프레임워크를 사용하기 위한 미들웨어입니다.
    'django.contrib.messages.middleware.MessageMiddleware',
    # 클릭재킹을 방어하기 위한 미들웨어입니다.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# config.urls'는 프로젝트의 루트 URL 패턴을 정의한 파일입니다. 일반적으로 Django 프로젝트의 루트 디렉터리에 있는 urls.py 파일이라고 생각할 수 있다
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        # Django의 기본 템플릿 엔진을 사용함을 지정
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 템플릿 파일들을 찾을 디렉터리 설정
        'DIRS': [BASE_DIR / 'templates'],
        # 앱 내의 'templates' 디렉터리를 자동으로 탐색하도록 설정
        'APP_DIRS': True,

        # 템플릿 엔진에 대한 기타 옵션들을 설정
        'OPTIONS': {
            'context_processors': [
                # 디버그 모드 여부를 템플릿에 전달
                'django.template.context_processors.debug',
                # 현재 요청(Request) 객체를 템플릿에 전달
                'django.template.context_processors.request',
                # 인증 관련 컨텍스트를 템플릿에 전달
                'django.contrib.auth.context_processors.auth',
                # 메시지 프레임워크의 메시지를 템플릿에 전달
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI 애플리케이션 설정
WSGI_APPLICATION = 'config.wsgi.application'


# 데이터베이스 설정
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Django 인증 비밀번호 유효성 검사 설정 부분입니다.
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # 사용자 이름과 유사한 비밀번호를 허용하지 않음
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # 비밀번호의 최소 길이를 검사
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # 자주 사용되는 비밀번호 패턴을 체크하여 피해야 할 보편적인 비밀번호를 차단
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    # 비밀번호에 숫자가 포함되어 있는지 검사
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 국제화 설정
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

# 국제화 사용 여부를 지정합니다. True로 설정 시, 다국어 지원이 활성화됩니다.
USE_I18N = True

# 시간대 사용 여부를 지정합니다. True로 설정 시, 시간대가 활성화됩니다.
USE_TZ = True


# 정적 파일 설정 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
'''이 설정은 일반적으로 웹 페이지에서 사용하는 정적 파일(이미지, 스타일시트, 자바스크립트 등)에 대한 URL을 생성할 때 필요합니다.
 현재 static 폴더를 생성하고 그 안에 css, js 를 넣었기 때문에 static/으로 url을 설정했다.
 
 예를 들어, CSS 파일이 static 디렉토리에 위치하고 style.css라는 이름을 가진 경우, 이 파일에 접근하기 위한 URL은 '/static/style.css'가 됩니다.'''
STATIC_URL = '/static/'

# 정적 파일은 프로젝트 루트 디렉토리에 있는 static_root 디렉토리에 저장
# 정적 파일들을 한 곳에 모아 서빙하면 웹 서버(예: Nginx, Apache)가 해당 디렉터리를 통해 정적 파일을
# 효율적으로 서빙할 수 있다.
STATIC_ROOT = BASE_DIR / 'static_root'

# 스타일시트 파일은 static으로 한다.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# static 폴더와 static_root의 차이
# static은 개발 중에 사용되며, Django 개발 서버가 정적 파일을 제공하는 데 사용됨
# 예를 들어, 개발 서버에서는 http://localhost:8000/static/로 접근하여 정적 파일에 액세스
# STATIC_ROOT 설정은 프로덕션 환경에서 사용됨
# python manage.py collectstatic 명령어를 실행하면 각 Django 애플리케이션의 static 디렉토리에서 정적 파일을 수집하여 STATIC_ROOT 디렉토리에 복사
# 프로덕션 환경에서는 보통 웹 서버(Nginx, Apache 등)에서 STATIC_ROOT에 위치한 정적 파일을 서빙하여 더 효율적으로 처리


# 기본 기본 키 필드 유형 설정
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
# Django 모델의 기본 키 필드에 대한 자동 생성 시 사용되는 데이터베이스 필드 유형을 설정
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 로그인 성공후 이동하는 URL
LOGIN_REDIRECT_URL = '/'

# 로그아웃시 이동하는 URL
LOGOUT_REDIRECT_URL = '/'

