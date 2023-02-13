from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Message


# Create your views here.

def homepage(request : HttpRequest):
    return render(request, "main/homepage.html")

def projects(request : HttpRequest):
    return render(request, "main/projects.html")

def about_me(request : HttpRequest):
    return render(request, "main/about_me.html")

def contact_me(request : HttpRequest):
    if request.method == "POST":
        new_message = Message(name=request.POST["name"], email= request.POST["email"], message= request.POST["message"])
        new_message.save()
    return render(request, "main/contact_me.html")
