from django.urls import path
from .import views

app_name= "main"

urlpatterns =[

    path("", views.index , name ="index"),
    path("firstproject/" , views.proj1 , name="firstproject"),
    path("secondproject/" , views.proj2 , name="secondproject"),

]