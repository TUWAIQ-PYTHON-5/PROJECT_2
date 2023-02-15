from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.base_page, name="base_page"),
    path("profile/", views.profile_page, name="profile_page"),
    path("interests/", views.interests_page, name="interests_page"),
    path("services/", views.services_page, name="services_page"),
    path("content/", views.content_page, name="content_page"),
    path("display/", views.display_page, name="display_page"),
    path("add/", views.add_page, name="add_page"),


]