from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home_page"),
    path("about/",views.about, name="about_page"),
    path("contant/",views.contant, name="contant_page"),
    path("skills/",views.skills, name="skills_page"),
    path("data/",views.user_data, name="data_page"),
]