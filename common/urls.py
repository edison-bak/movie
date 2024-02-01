from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    # 로그인,LoginView 클래스를 사용하여 사용자 인증을 처리합니다.
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    
    # 로그아웃
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # 회원가입요청시 views의 signup 실행
    path('signup/', views.signup, name='signup'),
]