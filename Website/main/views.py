from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact


# def concerns_page(request : HttpRequest):
   
#     return render(request , "main/concerns.html")


def index_page(request : HttpRequest):
      if request.method == "POST":
        #to add a new entry
        new_contact = Contact(name= request.POST["name"], email = request.POST["email"], content = request.POST["content"])
        new_contact.save()
        return redirect("main:view_msg_page")


      return render(request, "main/index.html")



def gym_page(request : HttpRequest):
   
    return render(request , "main/gym.html")


def web_page(request : HttpRequest):
   
    return render(request , "main/web.html")


def graphic_page(request : HttpRequest):
   
    return render(request , "main/graphic.html")



def view_msg(request : HttpRequest):

    view_msg = Contact.objects.all()

    context = {"view_msg" : view_msg}
    return render(request, "main/contact.html", context)



def view_contact(request : HttpRequest):

    view_contact = Contact.objects.all()

    context = {"view_contact" : view_contact}
    return render(request, "main/view_contact.html", context)
