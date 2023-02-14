from django.db import models

# Create your models here.
class Projects(models.Model):

    title = models.CharField(max_length=1024)
    content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    

class UsersContact(models.Model):

    name = models.CharField(max_length=512)
    email = models.EmailField()
    subject = models.CharField(max_length=512)
    message = models.TextField()


