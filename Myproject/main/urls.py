from django.urls import path
from . import views

app_name = "main"


urlpatterns = [

    path('', views.index_page, name="index_page"),
    path('contact/', views.contact_me, name="contact"),
    path('journey/', views.my_journey, name="journey"),
    path('view/', views.view, name="view"),

 

   
]