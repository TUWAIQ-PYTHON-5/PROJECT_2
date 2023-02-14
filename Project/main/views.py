from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Form
# Create your views here.


def home_page(request:HttpRequest):
    return render(request,'main/home.html')

def about_me(request:HttpRequest):
    redirect("main:about_me_page")

    return render(request,"main/about_me.html")
def interest_page(request:HttpRequest):
    redirect("main:interest_page")
    return render(request,"main/interest.html")

def work_page(request:HttpRequest):
    redirect("main:work_page")
    return render(request,"main/work.html")

def project_page(request:HttpRequest):
    redirect("main:project_page")
    return render(request,"main/project.html")


def survices_page(request:HttpRequest):
    redirect("main:survices_page")
    return render(request,"main/survices.html")

def form_page(request:HttpRequest):
     if request.method == "POST":
        new_form=Form(name=request.POST["name"],email=request.POST["email"], phone=request.POST["phone"],gender=request.POST["gender"],is_student=request.POST["is_student"],state=request.POST["state"])
        new_form.save()

        return redirect("main:latest_form_page")
     return render(request,"main/form.html")

def latest_form(request:HttpRequest):
    latest_form= Form.objects.all()
    context = {"latest_form" : latest_form}
    return render(request, "main/index.html", context)
def form_detail(request:HttpRequest,form_id):

    form = Form.objects.get(id=form_id)
    return render(request, "main/detail.html", {"form" : form})


def book_page(request:HttpRequest):
    redirect("main:book_page")
    return render(request,"main/book.html")

def horse_page(request:HttpRequest):
    redirect("main:horse_page")
    return render(request,"main/horse.html")

