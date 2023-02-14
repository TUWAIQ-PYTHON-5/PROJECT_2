from django.urls import path
from . import views

app_name = "faiapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('msg', views.msg, name='msg'),
    
]