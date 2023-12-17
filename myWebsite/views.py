from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice

def homePage(request):
    template = loader.get_template("index.html")
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return HttpResponse(template.render(context, request))

def questionDetails(request, id):
    question = Question.objects.get(id = id)
    choices = question.choice_set.all()
    context = {
        "choices": choices,
        "question": question
    }
    template = loader.get_template("details.html")
    return HttpResponse(template.render(context, request))

def submitAction(request, id):
    question = Question.objects.get(id = id)
    selcted_choice = question.choice_set.get(pk = request.POST["choice"])
    selcted_choice.votes += 1
    selcted_choice.save()
    template = loader.get_template("submittedPage.html")
    return HttpResponse(template.render(None, request))

def results(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    template = loader.get_template("results.html")
    return HttpResponse(template.render(context, request))
