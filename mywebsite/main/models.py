from django.db import models

# Create your models here.


class Person(models.Model):
    name= models.CharField(max_length=1024)
    number=models.IntegerField()
    email=models.EmailField()
class Comment(models.Model):
       name= models.CharField(max_length=1024)
       comment=models.TextField()

