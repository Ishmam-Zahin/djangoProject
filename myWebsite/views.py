from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def myfunc(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def aboutMe(request):
    template = loader.get_template("aboutMe.html")
    return HttpResponse(template.render())

def skills(request):
    template = loader.get_template("skills.html")
    return HttpResponse(template.render())

# Create your views here.
