from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Client,Sign_up

# Create your views here.

def home(request : HttpRequest):
    return render(request,'raghad/home.html')


def portfolio(request : HttpRequest):
    return render(request,'raghad/portfolio.html')




def services(request : HttpRequest):
    return render(request,'raghad/services.html')


def send(request : HttpRequest,client_id):
    client_fname=Client.objects.get(id=client_id)
    return render(request,'raghad/sent.html',{"client_fname":client_fname})



def contact(request : HttpRequest):
    if request.method == "POST":
        add_client =Client(first_name= request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"], message = request.POST["message"])
        add_client.save()
        return redirect("raghad:sent",client_id=add_client.id)
    return render(request,"raghad/contact.html")



def about(request : HttpRequest):
    return render(request,'raghad/about.html')


def sign_up(request : HttpRequest):
    if request.method == "POST":
        add_client =Sign_up(full_name= request.POST["full_name"], email = request.POST["email"], phone_number = request.POST["phone_number"])
        add_client.save()
        return redirect("raghad:deatils", user_id = add_client.id)
    return render(request,'raghad/sign_up.html')



def detailes(request : HttpRequest,user_id):
    info=Sign_up.objects.get(id=user_id)
    return render(request, "raghad/detail.html",{"info":info})






