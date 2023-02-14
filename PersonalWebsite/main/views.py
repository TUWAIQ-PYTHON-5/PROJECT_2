from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def index(request :HttpRequest):
    return render (request, 'main/index.html')


def proj1(request :HttpRequest):
    return render (request, 'main/proj1.html')

def proj2(request :HttpRequest):
    return render (request, 'main/proj2.html')

def proj3(request :HttpRequest):
    return render (request, 'main/proj3.html')

def contact(request : HttpRequest):
    if request.method == "POST":
        new_content = Post(Your_Name= request.POST['Your_Name'], Enter_Email=request.POST['Enter_Email'], Send_Message = request.POST['Send_Message'])
        new_content.save()
    return render(request, 'main/index.html')