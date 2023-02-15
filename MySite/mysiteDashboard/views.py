from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse 
from .models import owner
from mysite_app.models import MainModel , About , Services , Contact
from mysite_blog.models import Posts 

# Create your views here.


def info(request : HttpRequest):
    
    result = MainModel.objects.all()
    posts = Posts.objects.all()
    about = About.objects.all().order_by("-id")
    con = Contact.objects.all()
    service = Services.objects.all()
    about_index = about[0]
    for i in result:
            f_content = result[0]
            s_content = result[1]
            t_content = result[2]
    context =  { 
    "result1" : f_content ,
    "result2" : s_content ,
    "result3" : t_content ,
    "postsID" : posts,
    "about_result" :about_index,
    "contacts" : con,
    "services" : service
    
    }
            
    return render(request , "dashboards/dashboard.html" , context )



def detail_main(request : HttpRequest , detail_id):
    
        details = MainModel.objects.get(id = detail_id)
        return render(request, "AppSection/details_main.html", {"detail" : details})


def update_main(request : HttpRequest , main_id):
    
    data = MainModel.objects.get(id=main_id)
    if request.method == "POST":
        
        data.title = request.POST["title"]
        data.description = request.POST["description"]
        data.image = request.FILES["image"]
        data.save()
        return redirect("url_dashboard:info_dashboard")

    return render(request, "AppSection/update.html" , {"result" : data})
 
 
#  ------------------------------------------------------------------------------ 
    
def update_about(request : HttpRequest):
    
        if request.method == "POST":
            new_info = About(title= request.POST["title"], about_content = request.POST["content"],  image = request.FILES["image"])
            new_info.save()
            
            return redirect("url_dashboard:info_dashboard")
        return render(request, "AppSection/about_edit.html")
    
# -------------------------------------------------------------------------------
def update_service(request : HttpRequest , service_id):
    
    data = Services.objects.get(id=service_id)
    
    if request.method == "POST":
        data.title = request.POST["title"]
        data.service_content = request.POST["service_content"]
        data.save()
            
        return redirect("url_dashboard:info_dashboard")
    return render(request, "AppSection/service_edit.html")
    
# ------------------------------------------------------------------------------- 
def add_post(request : HttpRequest):
    
        if request.method == "POST":
            
            Posts(
                title= request.POST["title"],
                content = request.POST["content"] ,
                publish_date = request.POST["publish_date"], 
                image = request.FILES["image"]).save()
            
            return redirect("url_dashboard:info_dashboard")
        return render(request, "BlogSection/add_post.html" )
    
    
    
    
def post_update(request : HttpRequest , post_id ):

    post = Posts.objects.get(id = post_id)

    if request.method == "POST":
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.publish_date = request.POST["publish_date"]
            post.image = request.FILES["image"]

            post.save()
            return redirect("url_dashboard:info_dashboard")
    return render(request , "BlogSection/update_post.html" ,  {"posts" : post})



def delete_post(request : HttpRequest, details_id):
    post = Posts.objects.get(id=details_id)
    post.delete()
    return redirect("url_dashboard:info_dashboard")



# ---------------------------------------------
def display_blog(request : HttpRequest , details_id):
         
    details = Posts.objects.get(id = details_id)  
    context = {
             "posts" : details
              } 
         
    return render(request , "blogSection/details_post.html" , context )

# -------------------------------------------------------------------
def contact_details(request : HttpRequest , contact_id):
         
    contact_details = Contact.objects.get(id = contact_id) 
     
    context = {
             "contact" : contact_details
              } 
         
    return render(request , "AppSection/contact_details.html" , context )


def contact_delete(request : HttpRequest, contact_id):
    
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect("url_dashboard:info_dashboard")

