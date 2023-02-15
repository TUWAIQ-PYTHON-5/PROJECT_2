from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from main.models import Contact


def home_page(request:HttpRequest):
    return render(request,'main/home_page.html')

def project_page(request:HttpRequest):  
    return render(request,'main/service_page.html')

def about_page(request:HttpRequest):
    return render(request,'main/about_page.html')

def contact_page(request:HttpRequest):
    if request.method == 'POST':
        info = Contact(name = request.POST['name'],phone_number=request.POST['phone'],email=request.POST['email'],message = request.POST['message'])
        info.save()
        return render(request,'main/contact_page.html')
    
    return render(request,'main/contact_page.html')

def coffee_project_detail(request:HttpRequest):
    return render(request,'main/coffee_project_detail.html')

def alphabet_project_detail(request:HttpRequest):
    return render (request,'main/alphabet_project_detail.html')
