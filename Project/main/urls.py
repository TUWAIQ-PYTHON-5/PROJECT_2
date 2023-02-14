from django.urls import path 
from . import views


app_name='main'
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('about_me/',views.about_me,name='about_me_page'),
    path('interest/',views.interest_page,name='interest_page'),
    path('work/',views.work_page,name="work_page"),
    path('project/',views.project_page,name='project_page'),
    path('survices/',views.survices_page,name='survices_page'),
    path('form/',views.form_page,name='form_page'),
    path('book/',views.book_page, name='book_page'),
    path('horse/',views.horse_page,name='horse_page'),
    path('latest/', views.latest_form, name='latest_form_page'),
    path('detail/<form_id>/',views.form_detail,name='form_detail'),
  
]