from django.urls import path
from . import views


app_name = "url_blog"

urlpatterns = [
    
    path('blogs/' , views.display , name="blog_page"),
    # path('blogs/Add' , views.add_post , name="add_post"),
    path("blogs/details/<post_id>", views.detail_post, name="details_post"),
  
]