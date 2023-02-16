from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Message
# Create your views here.



def home(request : HttpRequest):
    return render(request, "main/home.html")

def about_me(request : HttpRequest):
    return render(request, "main/about_me.html")

def achievements(request : HttpRequest):
    return render(request, "main/achievements.html")

def my_writings(request : HttpRequest):
    return render(request, "main/my_writings.html")

def contact_me(request : HttpRequest):
    if request.method == "POST":
        new_message = Message(name=request.POST["name"], email= request.POST["email"], message= request.POST["message"])
        new_message.save()
    return render(request, "main/contact.html")

def messages( request : HttpRequest):
    messages = Message.objects.all()
    context = {"messages" : messages}

    return render(request, "main/messages.html", context)



    





