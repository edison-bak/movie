from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# forms에서 UserForm 가져옴
from common.forms import UserForm


def signup(request):
    # 회원가입 내용 입력하고 POST 눌렀을때.
    if request.method == "POST":
        # 회원가입 모듈로 회원 생성 
        form = UserForm(request.POST)
        # 만약 잘 입력했으면 저장
        if form.is_valid():
            form.save()
            # 가입후 자동 로그인 하기 위해 정보 불러옴
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 인증
            user = authenticate(username=username, password=raw_password) 
            # 로그인
            login(request, user)
            # 'index'라는 이름의 URL로 리다이렉트 path('', views.index,name='index')
            return redirect('index')
    # 회원가입 페이지에 접근했을때(GET 요청)일 경우 빈 회원가입 폼 생성
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})