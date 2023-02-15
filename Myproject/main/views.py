from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Info , Comment

# Create your views here.

def index_page(request : HttpRequest):
      if request.method == "POST":
        #to add a new entry
        new_contact = Info(name= request.POST["name"], email = request.POST["email"], content = request.POST["content"])
        new_contact.save()
        

        return redirect("main:contact")


      return render(request, "main/index.html")
 




def contact_me (request : HttpRequest):

    return render (request,"main/contact.html")



def my_journey (request : HttpRequest):
    comments=Comment.objects.all()
    if request.method == "POST":
        new_comment = Comment(Name = request.POST["Name"], your_comment = request.POST["your_comment"])
        new_comment.save()
        return redirect("main:journey")
    return render (request,"main/journey.html", {"comments":comments})



def view(request : HttpRequest):

    view = Info.objects.all()

    context = {"view" : view}
    
    return render(request, "main/view.html", context)