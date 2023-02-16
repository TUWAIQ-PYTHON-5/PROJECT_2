from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse 
from .models import MainModel , About , Services , Contact

# Create your views here.

def index(request : HttpRequest):
    
    result = MainModel.objects.all()
    services = Services.objects.all()
    
    
    f_content = result[0] 
    s_content = result[1]
    t_content = result[2]


    f_service = services[0]
    s_service = services[1]
    t_service = services[2]
            
    context = {
        "content1" : f_content,
        "content2" : s_content,
        "content3" : t_content,
        "services1" : f_service,
        "services2" : s_service,
        "services3" : t_service,
        
        }
         
    return render(request , "main/index.html" , context )



def about(request : HttpRequest):

    result = About.objects.all().order_by("-id")
    
    last_content = result[0]        
    context = {
        "results" : last_content,
        }

    return render(request , "main/about.html" , context )


def contact(request : HttpRequest):

    if request.method == "POST":
            new_contact = Contact(name = request.POST["name"], email = request.POST["email"],  Phone = request.POST["phone"])
            new_contact.save()
            
            return redirect("url_main:index_page")
    return render(request, "main/contact.html")
    

   
        

