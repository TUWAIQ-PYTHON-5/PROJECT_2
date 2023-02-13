from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import POST


# Create your views here.

def index(request : HttpRequest):
    return render(request, 'faiapp/index.html')



def contact(request : HttpRequest):
    if request.method == "POST":
        new_content = POST(Your_Name= request.POST['Your_Name'], Enter_Email=request.POST['Enter_Email'], Send_Message = request.POST['Send_Message'])
        new_content.save()
        return redirect("faiapp:index")
    return render(request, 'faiapp/contact.html')


def gallery(request: HttpRequest):
    
    return render(request, "faiapp/gallery.html")
    


