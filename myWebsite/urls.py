from django.contrib import admin
from django.urls import path
from . import views

app_name = "myWebsite"

urlpatterns = [
    path("", views.homePage, name="home"),
    path("browse/details/<int:id>/", views.questionDetails, name="q_details"),
    path("browse/submitPage/<int:id>/", views.submitAction, name="submitPage"),
    path("browse/results/", views.results, name="results"),
]
