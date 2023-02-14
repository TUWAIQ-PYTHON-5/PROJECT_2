from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    path("", views.index_page, name="index_page"),
    # path("concerns/", views.concerns_page, name="concerns_page"),
    path("concerns/gym/", views.gym_page, name="gym_page"),
    path("concerns/website/", views.web_page, name="web_page"),
    path("concerns/graphic/", views.graphic_page, name="graphic_page"),
    path("view/", views.view_msg, name="view_msg_page" ),
    path("view_contact/", views.view_contact, name="view_contact" ),
    


]