from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("",                    views.index,            name="index"),
    path("auth/",               views.auth,             name="auth"),
    path("edit/",               views.addNews,          name="edit"),
    path("bio/",                views.bio,              name="bio"),
    path("pro/",                views.pro,              name="pro"),
    path("contact/",           views.contact,         name="contact"),
    path("intell/",             views.intell,           name="intell"),
    path("details/<new_id>/",   views.newDetails,       name="newDetails"),
    path("review/<new_id>/",    views.comment,          name="comment"),
    path("delete/<new_id>/",    views.newsDelete,       name="newsDelete"),
   
    path("addUser/",            views.addUser,          name="addUser"),
]