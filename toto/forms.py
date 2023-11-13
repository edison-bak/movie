
# 폼은 쉽게 말해 페이지 요청시 전달되는 파라미터들을 쉽게 관리하기 위해
# 사용하는 클래스이다. 폼은 필수 파라미터의 값이 누락되지 않았는지, 
# 파라미터의 형식은 적절한지 등을 검증할 목적으로 사용

from django import forms
from toto.models import  Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }