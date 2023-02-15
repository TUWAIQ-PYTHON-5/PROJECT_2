from django.urls import path
from . import views

app_name = "my_website"

urlpatterns = [
    path('', views.home, name="home-page"),
    path('about/', views.about, name="about-page"),
    path('content/', views.content, name="content-page"),
    path('callme/', views.callme, name="callme-page")
]

