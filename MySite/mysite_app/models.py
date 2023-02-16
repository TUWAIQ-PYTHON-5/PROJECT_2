from django.db import models 

# Create your models here.


class MainModel(models.Model):
    
    title = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    
    
    
class About(models.Model):
    
    title = models.CharField(max_length=1024)
    about_content = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    

class Services(models.Model):
    
    title = models.CharField(max_length=1024)
    service_content = models.TextField()
    
    
class Contact(models.Model):
    
    name = models.CharField(max_length=102)
    email = models.EmailField()
    Phone = models.CharField(max_length=50)
 
    