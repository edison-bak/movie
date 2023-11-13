from django.urls import path

from . import views

#다른 프로젝트와 꼬이지 않게 이름지정
app_name='toto'

urlpatterns = [
    # /toto 링크를 입력하면, view.py 의 index 메서드 연결
    path('', views.index,name='index'),
    
    # /toto/숫자/ 링크를 입력하면, view.py 의 detail 메서드 연결
    path('<int:question_id>/', views.detail ,name='detail'),
    
    # /toto/숫자/vote/ 링크를 입력하면, view.py 의 vote 메서드 연결
    path('<int:question_id>/vote/', views.vote, name='vote'), 
    
    # /toto/숫자/result/ 링크를 입력하면, view.py 의 result 메서드 연결
    path('<int:question_id>/result/', views.result, name='result'),

    # /toto/answer/create/숫자/ 링크를 입력하면, view.py 의 answer_create 메서드 연결
    # 이건 보통 링크를 입력해 접속하지 않고 투표하면 자동으로 이동한다. 
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]