from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import UsersContact


# Create your views here.

def main_page(request : HttpRequest):
    
    return render(request, 'main/index.html')

def about_page(request : HttpRequest):
    
    return render(request, 'main/about.html')

def projects_page(request : HttpRequest):
    
    return render(request, 'main/projects.html')

def contact_page(request : HttpRequest):
    
    return render(request, 'main/contact.html')

def add_contact(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_contact = UsersContact(name= request.POST["name"], email = request.POST["email"], subject = request.POST["subject"], message = request.POST["message"],)
        new_contact.save()
        return redirect("main:contact_page")


    return render(request, "main/contact.html")
