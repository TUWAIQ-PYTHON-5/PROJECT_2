from django.urls import path
from . import views

app_name = "Web"

urlpatterns = [
    path("", views.index, name="index"),
    path("Home", views.Home, name="Home"),
    path("About/", views.About, name="About"),
    path("feedback/", views.feedback, name="feedback"),
    path("thankyou/", views.thankyou, name="thankyou"),




]

