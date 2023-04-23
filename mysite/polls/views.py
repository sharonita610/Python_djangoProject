from urllib import request

from polls.models import Question
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def index(request):
    lastest_questions = Question.objects.all().order_by('-pub_date')[:5]


context = {'questions': latest_questions}

return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/detail.html", {"question": question})
