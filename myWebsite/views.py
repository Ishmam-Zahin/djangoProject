from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MyTable

def myfunc(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def aboutMe(request):
    template = loader.get_template("aboutMe.html")
    first_person = MyTable.objects.all()[0]
    context = {
        "first_person": first_person
    }
    return HttpResponse(template.render(context, request))

def skills(request):
    template = loader.get_template("skills.html")
    second_person = MyTable.objects.all()[1]
    context = {
        "second_person": second_person
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
