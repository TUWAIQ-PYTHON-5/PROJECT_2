from django.urls import path
from . import views


app_name = "url_main"

urlpatterns = [
    
    path("" , views.index , name= "index_page"),
    path("About/" , views.about , name= "about_page"),
    # path("Services/" , views.services , name= "services_page"),
    path("Contact/" , views.contact , name= "contact_page"),
]