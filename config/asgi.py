"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# 이 함수는 Django 프로젝트의 ASGI 애플리케이션을 반환
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

#  Django 프로젝트의 ASGI 애플리케이션을 가져와 application 변수에 할당
application = get_asgi_application()
