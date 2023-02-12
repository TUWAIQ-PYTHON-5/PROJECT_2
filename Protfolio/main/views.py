from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def main_page(request : HttpRequest):
    
    return render(request, 'main/index.html')

def about_page(request : HttpRequest):
    
    return render(request, 'main/about.html')

def freelancing_page(request : HttpRequest):
    
    return render(request, 'main/freelancing.html')

def contact_page(request : HttpRequest):
    
    return render(request, 'main/contact.html')
