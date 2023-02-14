from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request :HttpRequest):
    return render (request, 'main/index.html')


def proj1(request :HttpRequest):
    return render (request, 'main/proj1.html')

def proj2(request :HttpRequest):
    return render (request, 'main/proj2.html')

def proj3(request :HttpRequest):
    return render (request, 'main/proj3.html')