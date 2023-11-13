from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    # POST 요청인 경우에는 화면에서 입력한 데이터로 사용자를 생성
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        # form.cleaned_data.get 폼의 입력값을 개별적으로 얻고 싶은 경우에 사용
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 사용자 인증
            user = authenticate(username=username, password=raw_password) 
            # 로그인
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})