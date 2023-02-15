from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Message


# Create your views here.

def homepage(request : HttpRequest):
    return render(request, "main/homepage.html")

def card(request : HttpRequest):
    return render(request, "main/card.html")

def projects(request : HttpRequest):
    return render(request, "main/projects.html")

def about_me(request : HttpRequest):
    return render(request, "main/about_me.html")

def contact_me(request : HttpRequest):
    if request.method == "POST":
        new_message = Message(name=request.POST["name"], email= request.POST["email"], message= request.POST["message"])
        new_message.save()

    return render(request, "main/contact_me.html")

def messages( request : HttpRequest):
    messages = Message.objects.all()
    context = {"messages" : messages}

    return render(request, "main/messages.html", context)

def delete_message(request : HttpRequest, message_id):
    
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect("main:messages_page")


