from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from .models import Comment
import os


def index(request : HttpRequest):
    return render(request, "Web/index.html" )

def Home(request : HttpRequest):
    return render(request, "Web/Home.html" )

def About(request : HttpRequest):
    return render(request, "Web/About.html" )


def feedback(request: HttpRequest):
    comments=Comment.objects.all()
    if request.method == "POST":
        new_comment = Comment(Name = request.POST["Name"], your_comment = request.POST["your_comment"])
        new_comment.save()
    return render(request, 'Web/feedback.html',  {"comments":comments})



def thankyou(request : HttpRequest):
    comments=Comment.objects.all()
    return render(request, 'Web/thankyou.html', {"comments":comments})