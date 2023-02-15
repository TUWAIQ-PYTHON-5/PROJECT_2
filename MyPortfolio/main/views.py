from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,FileResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import os
from django.core.mail import send_mail
from . models import blog , replay,contactMeData
from django.contrib import messages
import os





# Create your views here.
def homePage(request : HttpRequest):
    latest_news = blog.objects.all().order_by('-publish_date')[0 : 4]

    return render(request , 'main/home.html' ,{'latest_news' :latest_news} )

def downloadCV(request :HttpRequest):
    file = os.path.join ( settings.BASE_DIR, 'PDF/main/Ahmed.pdf')

    fileOpean =open(file,'rb')
    return FileResponse(fileOpean)  

def contactMe(request : HttpRequest):
    if request.method =='POST':
        name = request.POST['cf-name']
        email= request.POST['cf-email']
        message = request.POST['cf-message']
        newContactMeMsg=contactMeData(cf_name=name , cf_email=email , cf_message=message )
        newContactMeMsg.save()

        ##sending confirmation to user email
        send_mail(
            subject='ahmed portfolio',
            message= f' i recive your message and i will contact you soon {name} on your email : {email}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]    
         )
        #sending notfication to my  email
        send_mail(
            subject=name,
            message= f' message :  {message} sender is: {email}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['alhisan.swe@gmail.com'])
        return render(request , 'main/contactMe.html' , {'name':name , 'email':email} )    
    else:
    
        return render(request , 'main/contactMe.html' ) 



def searchBlog(request : HttpRequest ):
    
    if 'Search' in request.GET:
        searched_blog = blog.objects.filter(title__contains=request.GET["Search"])
    else:
        searched_blog = blog.objects.all()
    return render(request , 'main/search_blog.html' , {'searched_blog':searched_blog})  




def add_bolg(request :HttpRequest):
    if request.method =='POST':
        new_blog = blog(title= request.POST['title'] ,description = request.POST['description'], image = request.FILES['image'] )
        new_blog.save()
        messages.success(request ,(" BLOG Added successfully "))
        return redirect('main:add_blog')      
    return render(request, 'main/add_bost.html')



def show_blog (request :HttpRequest , blog_id):
    the_blog = blog.objects.get(id = blog_id)
    all_replay = replay.objects.filter(replay_for_blog=the_blog)

    

    return render(request , 'main/blog-detail.html',{'blog':the_blog , 'allreplay':all_replay})


def show_all(request :HttpRequest):
    if 'Search' in request.GET:
        searches_bost = blog.objects.filter(title__contains=request.GET['Search'])
    else:
        searches_bost = blog.objects.all()    
    return render(request , 'main/control_blog.html',{'searches_bost' : searches_bost})    


def delet_blog(request:HttpRequest , blog_id): 
    deleted_blog = blog.objects.get(id = blog_id)
    deleted_blog.delete()
    messages.success(request , "BLOG deleted successfully")
    return redirect('main:show')

def update_blog(request : HttpRequest , blog_id):
    updated_blog = blog.objects.get(id=blog_id)
    updated_blog.publish_date=updated_blog.publish_date.isoformat(" ")
    
    if request.method == 'POST':
        updated_blog.title = request.POST['title']
        updated_blog.image = request.FILES['image']
        updated_blog.description = request.POST['description']
        updated_blog.save()
        messages.success(request , " Blog successfully Updated ")
        return redirect ('main:show')
    return render(request , 'main/update_blog.html',{'updated_blog':updated_blog})  

def addReplay(request : HttpRequest , blog_id):

    if request.method == 'POST':
        blog_assign = blog.objects.get(id=blog_id)
        new_replay = replay(replay_for_blog = blog_assign , name =request.POST['name'] ,replayMsg =  request.POST['replayMsg'])
        new_replay.save()
        messages.success(request , 'Replay added successfully')
    return redirect( 'main:show_blog' , blog_id = blog_id)    



 


    