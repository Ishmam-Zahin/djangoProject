from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.myfunc),
    path("aboutMe/", views.aboutMe),
    path("skills/", views.skills),
    path('admin/', admin.site.urls),
]
