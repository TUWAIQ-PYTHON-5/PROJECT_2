from django.db import models

# Create your models here.

class Info(models.Model):

    name = models.CharField(max_length=1024)
    content = models.TextField()
    email = models.EmailField()


class Comment(models.Model):
    Name = models.CharField(max_length=100)
    your_comment = models.CharField(max_length=512)
