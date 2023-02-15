from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("card/", views.card, name="card_page"),
    path("projects/", views.projects, name="projects_page"),
    path("about_me/", views.about_me, name="about_me_page"),
    path("contact/", views.contact_me, name="contact_me_page"),
    path("messages/", views.messages, name="messages_page"),
    path("delete/<message_id>/", views.delete_message, name="delete_page"),
]