from django.db import models

# Create your models here.
class Client(models.Model):
    first_name=models.CharField(max_length=700)
    last_name=models.CharField(max_length=700)
    email=models.EmailField()
    message=models.TextField()


class Sign_up(models.Model):
   full_name=models.TextField()
   email=models.EmailField()
   phone_number=models.IntegerField()
   

 


