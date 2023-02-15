from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('project/',views.project_page,name='project_page'),
    path('about/',views.about_page,name='about_page'),
    path('contact/',views.contact_page,name='contact_page'),
    path('coffee/detail/',views.coffee_project_detail,name='coffee_project_detail'),
    path('alphabet/detail/',views.alphabet_project_detail,name='alphabet_project_detail'),
    
]