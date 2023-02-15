from django.urls import path
from . import views

app_name = "main"

urlpatterns =[
    path("", views.index, name="index_page"),
    path("prodect/", views.prodect, name="prodect_page"),
    path("comment/", views.comment, name="comment_page"),
    path("add/", views.add_comment, name="add_comment_page"),
    path("Recommendations/", views.tasi, name="Recommendations_page"),

]