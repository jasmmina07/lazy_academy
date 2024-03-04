from django.contrib import admin
from django.urls import path,include
from .views import send_question,Task,sign_up

urlpatterns = [
    path('',send_question),
    path("class/",Task.as_view()),
    path("sign_up/",sign_up)
]