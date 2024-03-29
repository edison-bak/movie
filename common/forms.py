# 계정 생성시 사용할 유저폼

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 유저 생성 모듈 이용
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")