from django.db import models
# 사용자 모델로 회원가입시 데이터 저장 등에 사용
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

# 경기
class Question(models.Model):
    # 경기제목
    # verbose_name='경기' 는 관리자 화면에서 열이름으로 쓰임
    subject = models.CharField(max_length=200, verbose_name='경기')
    # 경기내용
    content = models.TextField()
    # 경기날짜(실제 데이터로 대체예정)
    game_date = models.DateTimeField(verbose_name='경기시간')

    # 관리자 화면에서 was_published_recently 열이름을 '오늘경기'로 대체
    @admin.display(boolean=True, description='오늘경기')
    # 하루내에 게시됐는지를 표시
    def was_published_recently(self):
        return self.game_date >= timezone.now() - datetime.timedelta(days=1)
    # 경기 내용과 날짜를 표시
    def __str__(self):
        return f'경기 : {self.subject}, 날짜: {self.game_date}'

# 선택
class Choice(models.Model):
    # 선택을 경기와 묶어줌, 경기가 삭제되면 선택도 삭제되게 설정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 선택팀 텍스트(토트넘 등등) 
    choice_text = models.CharField(max_length=200)
    # 투표수    
    votes = models.IntegerField(default=0)

    # [토트넘vs 맨유] 토트넘
    def __str__(self):
        return f'[{self.question.subject}] {self.choice_text}'

# 댓글
class Answer(models.Model):
    # 질문에 해당하는 댓글들을 연결, 질문 지우면 댓글들도 지워짐
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 댓글 내용 작성 부분
    content = models.TextField()
    # 댓글 작성 날짜
    answer_date = models.DateTimeField(auto_now_add=True)
    # 작성자 속성,기존에 저장된 값들은 null 처리
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# 유저의 모델 
class Userinfo(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
