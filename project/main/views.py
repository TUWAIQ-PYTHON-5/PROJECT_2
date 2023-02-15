from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Comment


def index(request : HttpRequest):
    
    return render(request,"main/index.html")



def prodect(request : HttpRequest):

    return render(request,"main/prodect.html")


def tasi(request : HttpRequest):

    return render(request,"main/tasi.html")






def comment(request : HttpRequest):

    comments_list = Comment.objects.all()
    context = {"comment" : comments_list}

    return render(request,"main/comment.html",context)



def add_comment(request : HttpRequest):
    if request.method == "POST":
        new_comment = Comment(name=request.POST["name"],comment=request.POST["comment"])
        new_comment.save()
        return redirect("main:index_page")

    return render(request,"main/add_comment.html")