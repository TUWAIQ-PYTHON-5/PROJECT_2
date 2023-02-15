from django.urls import path
from .import views

app_name='main'


urlpatterns = [
    path('',views.homePage, name='home_page'),
    path('download' , views.downloadCV , name='daownload'),
    path('contact' , views.contactMe , name='contact'),
    path('show_blog/<blog_id>' , views.show_blog , name='show_blog'),
    path('add_blog',views.add_bolg , name='add_blog') ,
    path('show/',views.show_all , name='show'),
    path('update/<blog_id>' , views.update_blog , name='update'),
    path('delete/<blog_id>',views.delet_blog , name='delete'),
    path('review/<blog_id>' , views.addReplay , name='replay'),
    path('serach/' , views.searchBlog , name ='search')
    
]
  
