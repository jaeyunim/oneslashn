from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.


def index(request):

    """notice 목록 출력"""

    question_list = Question.objects.order_by("create_date")
    context = {"question_list": question_list}
    return render(request, "notice/question_list.html", context)


def detail(request, question_id):

    """notice 내용 출력"""

    question = Question.objects.get(id=question_id)
    context = {"question": question}
    return render(request, "notice/question_detail.html", context)
