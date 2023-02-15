from django.urls import path
from .import views

app_name='user'


urlpatterns =[
    path('',views.login_page,name='login'),
    path('logout_user' , views.log_out_user,name='logout')

]