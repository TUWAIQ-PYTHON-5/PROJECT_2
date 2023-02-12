from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("about/", views.about_page, name="about_page"),
    path("freelancing/", views.freelancing_page, name="freelancing_page"),
    path("contact/", views.contact_page, name="contact_page"),
    
]