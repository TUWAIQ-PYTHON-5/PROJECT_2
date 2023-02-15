from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import News, Comment , Usr
# Create your views here.



################################################################
def index(request : HttpRequest):
    news = News.objects.all()
    context = {"news" : news}
    return render(request, "main/index.html", context)
################################################################
def addNews(request : HttpRequest):
    if request.method == "POST":
        newNews = News(title= request.POST["title"], content = request.POST["content"])
        newNews.save()
        return redirect("main:index")
    news = News.objects.all()
    context = {"news" : news}
    return render(request, "main/edit.html", context)
################################################################
def newDetails(request : HttpRequest, new_id):
    new = News.objects.get(id= new_id)
    comments = Comment.objects.filter(new=new)
    return render(request, "main/newDetails.html", {"new" : new, "comments" : comments})
################################################################
def comment(request : HttpRequest, new_id):
    if request.method == "POST":
        new = News.objects.get(id=new_id)
        newComment = Comment(new = new, name= request.POST["name"], content = request.POST["content"])
        newComment.save()
    return redirect("main:newDetails", new_id=new_id)
################################################################
def newsDelete(request : HttpRequest, new_id):
    new = News.objects.get(id=new_id)
    new.delete()
    return redirect("main:edit")
################################################################
def bio(request : HttpRequest):
    return render(request, "main/bio.html")
################################################################
def pro(request : HttpRequest):
    return render(request, "main/pro.html")
################################################################
def contact(request : HttpRequest):
    return render(request, "main/contact.html")
################################################################
def intell(request : HttpRequest):
    return render(request, "main/intell.html")
################################################################
def addUser(request : HttpRequest):
    if request.method == "POST":
        newusr = Usr(usrname= request.POST["usrname"], password = request.POST["password"])
        newusr.save()
        return redirect("main:index")
    news = Usr.objects.all()
    context = {"news" : news}
    return render(request, "main/edit.html", context)
################################################################
def auth(request : HttpRequest):
    if request.method == "POST":
        authUser = Usr(usrname= request.POST["usrname"], password = request.POST["password"])
        usersDict = Usr.objects.all()
        if(authUser in usersDict):
            flag:int=1
            return (redirect("main:edit"),flag)
        else:
            return redirect("main:index")
    return render(request, "main/index.html")
################################################################