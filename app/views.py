from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.http import HttpRequest,HttpResponse,JsonResponse
from .models import Question,Users
from random import randrange
import json

class Task(ListView):
    model=Question
    a=randrange(1,100)
    b=randrange(1,100)
    c=randrange(1,100)
    Question.objects.create(
        a=bin(a)[2:],
        b=bin(b)[2:],
        c=bin(c)[2:]
    )
    template_name="index.html"

    def __str__(self):
        return self.c

def sign_up(request:HttpRequest):
    if request.method=="POST":
        user=json.loads(request.body)
        first_name=user.get("first_name",False)
        last_name=user.get("last_name",False)
        user_name=user.get("user_name",False)
        password=user.get("password",False)
        email=user.get("email",False)

        if not first_name:
            return JsonResponse({"result":"please fill in the first name field"})
        if not last_name:
            return JsonResponse({"result":"please fill in the last name field"})
        if not user_name:
            return JsonResponse({"result":"please fill in the user name field"})
        if not password:
            return JsonResponse({"result":"please fill in the password field"})
        if not email:
            return JsonResponse({"result":"please fill in the email field"})
        
        Users.objects.create(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            password=password,
            email=email
        )
        return JsonResponse({"result":"Ok"})
    else:
        return JsonResponse({"result":"only post method"})


def send_question(request):
    model=Question
    a=randrange(1,100)
    b=randrange(1,100)
    c=randrange(1,100)
    Question.objects.create(
        a=bin(a)[2:],
        b=bin(b)[2:],
        c=bin(c)[2:]
    )

    template_name="index.html"

# Create your views here.
