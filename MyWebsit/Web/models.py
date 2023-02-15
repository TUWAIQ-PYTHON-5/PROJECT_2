from django.db import models

# Create your models here.

class Comment(models.Model):
    Name = models.CharField(max_length=100)
    your_comment = models.CharField(max_length=512)
