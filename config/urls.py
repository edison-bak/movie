from django.contrib import admin
from django.urls import path, include
from toto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # /toto/ 링크가 오면 toto의 urls로
    path('toto/',include('toto.urls')),

    path('common/', include('common.urls')),

    path('', views.index, name='index'),  # '/' 에 해당되는 path

]

