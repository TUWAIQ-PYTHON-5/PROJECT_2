from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from.models import Person,Comment

# Create your views here.

def base_page(request:HttpRequest):
    
    return render(request,"main/base.html")

def profile_page(request:HttpRequest):
    
    return render(request,"main/profilepersonly.html")

def interests_page(request:HttpRequest):
    
    return render(request,"main/interests.html")

def services_page(request:HttpRequest):
    if request.method=="POST":
     new_post=Person(name=request.POST["name"],number=request.POST["number"],email=request.POST["email"])
     new_post.save()
     return redirect("main:display_page")
    
    return render(request,"main/services.html")

def content_page(request:HttpRequest):
    if request.method=="POST":
     new_comment=Comment(name=request.POST["name"],comment=request.POST["comment"])
     new_comment.save()
     return redirect("main:display_page")
    
    return render(request,"main/content.html")

def display_page(request:HttpRequest):
    posts=Person.objects.all()
    post=Comment.objects.all()
    context={'post':posts,'postcomment':post}

    return render(request,"main/display.html",context)

def add_page(request : HttpRequest):
    if request.method=="POST":
        new_post=Person(name=request.POST["name"],content=request.POST["content"],number=request.POST["number"],emil=request.POST["emil"])
        new_post.save()

    return render(request,"main/add.html")





