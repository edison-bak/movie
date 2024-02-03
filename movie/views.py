# pyexpat 패키지의 messages 모듈을 가져옵니다.
from pyexpat.errors import messages
# Django의 shortcuts 모듈에서 필요한 기능을 가져옵니다.
from django.shortcuts import get_object_or_404, redirect,render
# Django의 timezone 모듈을 가져옵니다.
from django.utils import timezone
# 현재 앱(.으로 표시)의 models.py에서 모든 모델을 가져옵니다.
from .models import *
#페이징으로 페이지에 보이는 경기 갯수를 제한
from django.core.paginator import Paginator
# Django의 HTTP 응답 클래스들을 가져옵니다.
from django.http import HttpResponseRedirect
# Django의 reverse 함수를 가져옵니다.
from django.urls import reverse
# 데이터베이스의 models에서 F 객체를 가져옵니다.
# 데이터베이스에서 직접 필드 값을 가져와서 계산
from django.db.models import F

from django.http import HttpResponseNotAllowed
# 현재 앱의 forms.py에서 AnswerForm 클래스를 가져옵니다.
from .forms import AnswerForm
# Django의 login_required 데코레이터를 가져옵니다.
from django.contrib.auth.decorators import login_required

# 메인 경기페이지
def index(request):
    # 페이지
    # GET 요청의 매개변수 중 'page'라는 이름의 값을 가져옵니다. 
    # 만약 'page' 매개변수가 요청에 없다면 기본값으로 '1'을 사용
    page = request.GET.get('page', '1')
    # 데이터베이스에서 질문 목록 가져오기, 작성일시 역순으로 정렬
    question_list = Question.objects.order_by('-game_date')
    # 페이지당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    # 현재 페이지의 Question 객체들을 page_obj 변수에 저장
    page_obj = paginator.get_page(page)
    # 현재 페이지에 해당하는 Question 객체들을 'question_list'라는 변수로 
    # 템플릿에 전달
    context = {'question_list': page_obj}
    return render(request, 'movie/question_list.html', context)

# 상세 경기페이지
def detail(request, question_id):
    # primary key 각 객체를 유일하게 식별하는 주요 식별자입니다. 
    # Question 모델은 일반적으로 각 질문마다 고유한 pk를 가지고 있습니다. 
    # 사용자가 특정 질문에 접근(get)하려고 할 때, 해당 질문의 pk 값을 URL에서 
    # 가져오게 됩니다.
    question = get_object_or_404(Question, pk=question_id)
    current_time = timezone.now()
    context = {'question': question,'current_time': current_time}
    return render(request, 'movie/question_detail.html', context)

# 댓글 작성할때 로그인 필요
@login_required(login_url='common:login')
# 댓글 작성 (redirect해서 detail로 다시 이동)
# question_id는 URL 매핑에 의해 그 값이 전달된다. create/2/ 라는 페이지를
# 요청하면 매개변수 question_id에는 2라는 값이 전달된다.
def answer_create(request, question_id):
    # 우선 어떤 질문에 달린 댓글인지 알아야함
    question = get_object_or_404(Question, pk=question_id)
    # 댓글 등록(post)시
    if request.method == "POST":
        # POST 메서드로 전송된 데이터를 이용하여 AnswerForm 인스턴스를 생성
        form = AnswerForm(request.POST)
        if form.is_valid():
            # 임시 저장하여 answer 객체를 리턴받는다.
            answer = form.save(commit=False)
            # 작성자(author) 속성에 로그인 계정 저장
            answer.author = request.user
            # 실제 저장을 위해 작성일시를 설정한다.
            answer.answer_date = timezone.now()
            # 해당 질문도 저장
            answer.question = question
            answer.save()
            # 데이터베이스 저장후 다시 상세 페이지로 돌아감
            return redirect('movie:detail', question_id=question.id)
    #  답변 등록은 POST 방식만 사용되기 때문에 다른방식(GET)은 안됨
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'movie/question_detail.html', context)

# 투표(완료시 결과페이지(result)로 이동)
@login_required(login_url='common:login')
def vote(request, question_id):
    # 우선 어떤 질문에 달린 투표인지 알아야함
    question = get_object_or_404(Question, pk=question_id)
    
    # 데이터베이스에서 사용자가 해당 질문에 이미 투표했는지 확인
    # 유저가 해당질문에 이미 투표했으면, 이미 투표했다는 문구 출력
    if Userinfo.objects.filter(user=request.user, question=question).exists():
        return render(request, 'movie/question_detail.html', {'question': question, 'error_message': "이미 투표한 사용자입니다."})

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #선택 안한경우 처리
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'movie/question_detail.html', {'question': question, 'error_message': f"선택이 없습니다. id={request.POST['choice']}"})
    else:
        # F는 데이터베이스에서 현재 값을 가져와 필드 값을 업데이트하므로 다른 사용자가
        # 변경한 값을 덮어씌우지 않는다.
        selected_choice.votes = F('votes') + 1
        # 현재 로그인한 사용자를 저장
        selected_choice.user = request.user  
        selected_choice.save()
        
        # 사용자의 투표 여부 및 투표 항목 업데이트
        user_vote = Userinfo(user=request.user, question=question, choice=selected_choice)
        user_vote.save()
        # 투표 완료하면 결과페이지로 보냄. args는 "arguments"의 줄임말로, 뷰 함수나 
        # URL 패턴에 전달해야 하는 값들을 순서대로 나열하는데 사용냄
        return HttpResponseRedirect(reverse('movie:result', args=(question.id,)))

# 투표 결과페이지
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'movie/result.html', {'question': question})