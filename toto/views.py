from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect,render
from django.utils import timezone
from .models import *
#페이징으로 페이지에 보이는 경기 갯수를 제한
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from django.http import HttpResponseNotAllowed
from .forms import AnswerForm
from django.contrib.auth.decorators import login_required

# 메인 경기페이지
def index(request):
    # 페이지
    # GET 요청의 매개변수 중 'page'라는 이름의 값을 가져옵니다. 
    # 만약 'page' 매개변수가 요청에 없다면 기본값으로 '1'을 사용
    page = request.GET.get('page', '1')
    # 질문 리스트를 작성일시 역순으로 정렬
    question_list = Question.objects.order_by('-game_date')
    # 페이지당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    # question_list.html에 question_list 변수 전달하기위해 만든 딕셔너리
    context = {'question_list': page_obj}
    return render(request, 'toto/question_list.html', context)

# 상세 경기페이지
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    current_time = timezone.now()
    context = {'question': question,'current_time': current_time}
    return render(request, 'toto/question_detail.html', context)

# 댓글 작성 (따로 페이지는 없고 redirect해서 detail로 다시 이동한다)
# 답변 등록시 텍스트창에 입력한 내용은 answer_create 함수의 첫번째 매개변수인
# request 객체를 통해 읽을 수 있다.
# question_id는 URL 매핑에 의해 그 값이 전달된다. create/2/ 라는 페이지를
# 요청하면 매개변수 question_id에는 2라는 값이 전달된다.
# 댓글 작성할때 로그인 필요
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # 임시 저장하여 answer 객체를 리턴받는다.
            answer = form.save(commit=False)
            # author 속성에 로그인 계정 저장
            answer.author = request.user
            # 실제 저장을 위해 작성일시를 설정한다.
            answer.answer_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('toto:detail', question_id=question.id)
    #  답변 등록은 POST 방식만 사용되기 때문에 다른방식(GET)은 안됨
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'toto/question_detail.html', context)

# 투표(완료시 결과페이지(result)로 이동)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # (미구현) 모델에 user를 구현하고 그 정보를 받음
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # author 속성에 로그인 계정 저장

        # (미구현) 선행작업 : post 신호를 줄때, user 정보도 함께 넘겨야함
        # 유저 정보를 get하고 저장해놈, 경기 결과가 끝나면
        # 이정보를 이용해 user의 재산을 업데이트해줌

    #선택 안한경우 처리
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'toto/question_detail.html', {'question': question, 'error_message': f"선택이 없습니다. id={request.POST['choice']}"})
    else:
        # F는 데이터베이스에서 현재 값을 가져와 필드 값을 업데이트하므로 다른 사용자가
        # 변경한 값을 덮어씌우지 않는다.
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # voter_list.voter.add(request.user)
        # 투표 완료하면 결과페이지로 보냄. args는 "arguments"의 줄임말로, 뷰 함수나 
        # URL 패턴에 전달해야 하는 값들을 순서대로 나열하는데 사용냄
        return HttpResponseRedirect(reverse('toto:result', args=(question.id,)))

# 투표 결과페이지
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'toto/result.html', {'question': question})