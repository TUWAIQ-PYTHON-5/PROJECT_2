from django.db import models

# Create your models here.
class News(models.Model):

    title       = models.CharField(max_length=200)
    content     = models.TextField()
    writingDate = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):

    new        = models.ForeignKey(News, on_delete=models.CASCADE)
    name        = models.CharField(max_length=512)
    content     = models.TextField()
    writingDate  = models.DateTimeField(auto_now_add=True)

class Usr(models.Model):

    usrname         = models.CharField(max_length=12)
    password        = models.CharField(max_length=12)