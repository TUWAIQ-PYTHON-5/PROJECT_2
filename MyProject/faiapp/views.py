from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import POST, Comment


# Create your views here.

def index(request : HttpRequest):
    comments=Comment.objects.all()
    return render(request, 'faiapp/index.html', {"comments":comments})




def contact(request : HttpRequest):
    if request.method == "POST":
        new_content = POST(Your_Name= request.POST['Your_Name'], Enter_Email=request.POST['Enter_Email'], Send_Message = request.POST['Send_Message'])
        new_content.save()
        return redirect("faiapp:msg")
    return render(request, 'faiapp/contact.html')




def gallery(request: HttpRequest):
    if request.method == "POST":
        new_comment = Comment(Name = request.POST["Name"], your_comment = request.POST["your_comment"])
        new_comment.save()
        return redirect("faiapp:index")
    return render(request, "faiapp/gallery.html")




def msg(request: HttpRequest):
    return render(request, "faiapp/msg.html")

