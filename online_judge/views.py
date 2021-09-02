from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
    return render(request,'online_judge/index.html')


def problems(request):
    latest_problem_list = Question.objects.all()[:5]
    return render(request,'online_judge/problems.html',{'latest_problem_list':latest_problem_list})

def problem_details(request,problem_name):
    problem = get_object_or_404(Question,question_name=problem_name)
    return render(request,'online_judge/details.html',{'problem':problem})
