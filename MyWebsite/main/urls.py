from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.Home_page, name="Home_page"),
    path("interests",views.interests_page, name="interests_page"),
    path("contact",views.contact_me, name="contect_me"),
    path("project",views.project_page, name="project_page"),
    path("about",views.about_page, name="about_page"),
    path("skills",views.skills_page, name="skills_page")
]