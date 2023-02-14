from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("about/", views.about_page, name="about_page"),
    path("projects/", views.view_projects, name="projects_page"),
    path("contact/", views.contact_page, name="contact_page"),
    path("contact/add/", views.add_contact, name="add_contact"),
    path("details/<project_id>/", views.project_detail, name="project_detail"),
    
]