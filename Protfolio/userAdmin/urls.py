from django.urls import path
from . import views

app_name = "userAdmin"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("add_projects/", views.add_project, name="add_projects"),
    path("contact/", views.view_contact, name="contact_page"),
    path("view/", views.view_projects, name="view_projects_page"),
    path("details/<project_id>/", views.project_detail, name="project_detail"),
    path("update/<project_id>/", views.update_project, name="update_projects"),
    path("delete/<project_id>/", views.delete_project, name="delete_project"),

    
]