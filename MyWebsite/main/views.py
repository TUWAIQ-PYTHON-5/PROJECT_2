from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from.models import Message


# Create your views here.


def Home_page(request : HttpRequest):
    return render(request, "main/Home.html")

def about_page(request : HttpRequest):
    return render(request, "main/about.html")

def skills_page(request : HttpRequest):
    return render(request, "main/skills.html")

def interests_page(request : HttpRequest):
    return render(request, "main/interests.html")

def contact_page(request : HttpRequest):
    return render(request, "main/contact.html")

def project_page(request : HttpRequest):
    return render(request, "main/project.html")




def contact_me(request : HttpRequest):
    comments=Message.objects.all()
    if request.method == "POST":
        new_message = Message(name=request.POST["name"], email= request.POST["email"], message= request.POST["message"])
        new_message.save()
    return render(request, "main/contact.html",{"comments":comments})



