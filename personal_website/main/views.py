from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import project

# Create your views here.

def home(request : HttpRequest):
    

    return render(request, "main/base.html") 




def skills(request : HttpRequest):
    

    return render(request, "main/skills.html") 




def about(request : HttpRequest):
    

    return render(request, "main/about.html") 
    




def contant(request : HttpRequest):

    if request.method == "POST":
        call = project(name = request.POST["name"], phone = request.POST["phone"], email = request.POST["email"], message = request.POST["message"])
        call.save()
        return redirect('main:home_page')

    return render(request,"main/contant.html")


def user_data(request : HttpRequest):

    display = project.objects.all()
    context = {"result": display}
    return render(request, "main/data.html",context)






