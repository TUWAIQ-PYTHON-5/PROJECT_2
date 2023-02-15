from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact

# Create your views here.
def home(request : HttpRequest):
    return render(request, "my_website/home.html")

def about(request : HttpRequest):
    return render(request, "my_website/about.html")

def content(request : HttpRequest):
    return render(request, "my_website/content.html")

def callme(request : HttpRequest):
    if request.method == "POST":
        new_contact = Contact(user_name=request.POST["user_name"], email=request.POST["email"], massage=request.POST["massage"])
        new_contact.save()
        redirect("my_website:home-page")

    return render(request, "my_website/callme.html")

