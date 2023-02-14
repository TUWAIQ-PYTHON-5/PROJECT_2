from django.db import models

# Create your models here.


class Post(models.Model):
    Your_Name = models.CharField(max_length=100)
    Enter_Email = models.EmailField(max_length=200)
    Send_Message = models.CharField(max_length=100)