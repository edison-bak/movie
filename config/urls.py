from django.contrib import admin
from django.urls import path, include
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # /movie/ 링크가 오면 movie의 urls로
    path('movie/',include('movie.urls')),

    path('common/', include('common.urls')),

    path('', views.index, name='index'),  # '/' 에 해당되는 path

    path('rest/', include('movie_api.urls')),
]

