from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse 
from .models import Posts , Comment 

# Create your views here.

def display(request : HttpRequest):
         
    posts = Posts.objects.all()
         
    context = {
             "result" : posts
              } 
         
    return render(request , "blogs/blog.html" , context )




def detail_post(request : HttpRequest , post_id ):
    
    details = Posts.objects.get(id = post_id)
    

    return render(request , "blogs/details_post.html" , {"details" : details})

