from django.urls import path
from . import views

app_name = "main"

urlpatterns = [ 
 path("", views.home, name="home_page"),
 path("about_me", views.about_me, name="about_me_page"),
 path("achievements/", views.achievements, name="achievements_page"),
 path("my_writings/", views.my_writings, name="my_writings_page"),
 path("contact/", views.contact_me, name="contact_page"),
 path("messages/", views.messages, name="messages_page"),
]