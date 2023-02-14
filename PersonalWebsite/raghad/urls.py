from django.urls import path
from . import views

app_name="raghad"

urlpatterns = [
    path("", views.home, name="Home page"),
    path("Portfolio/", views.portfolio, name="Portfolio"),
    path("Services/", views.services, name="Services"),
    path("Contact/", views.contact, name="Contact"),
    path("about/", views.about, name="about" ),
    path("sign_up/", views.sign_up,name="sign_up" ),
    path("Sign_up_details/<user_id>/", views.detailes, name="deatils" ),
    path("sent_form/<client_id>/", views.send, name="sent" ),
   

    ]
