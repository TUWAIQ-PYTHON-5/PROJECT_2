from django.urls import path
from . import views


app_name = "url_dashboard"

urlpatterns = [
    
    path("dashboard/", views.info , name= "info_dashboard"),
    path("dashboard/mine/detail/<detail_id>", views.detail_main , name= "main_edit"),
    path("dashboard/mine/contact/<contact_id>/", views.contact_details , name= "contact_details"),
    path("dashboard/update/<main_id>/" , views.update_main , name= "Update_info"),
    path("dashboard/about/" , views.update_about , name= "update_about"),
    path("dashboard/service/<service_id>" , views.update_service , name= "update_service"),
    path("dashboard/add/post" , views.add_post , name= "add_post"),
    path('dashboard/post/details/<details_id>/' , views.display_blog , name="details_post"),
    path('dashboard/post/update/<post_id>/' , views.post_update , name="update_post"),
    path("dashboard/post/delete/<details_id>/" , views.delete_post , name= "delate_post"),
    path("dashboard/contact/delete/<contact_id>/" , views.contact_delete , name= "delate_contact"),
   
    
    
  
]