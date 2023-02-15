from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.

def login_page(request :HttpRequest):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('main:home_page')
        else:
            messages.success(request ,("Sory username or password are not correct "))
            return redirect( 'user:login')
    else:
        return render(request , 'authenticate/login.html')

def log_out_user(request :HttpRequest):
    logout(request)
    return redirect('main:home_page')




