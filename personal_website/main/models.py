from django.db import models

# Create your models here.

class project(models.Model):

    name = models.CharField(max_length=1024)
    phone = models.TextField()
    email = models.TextField()
    message = models.TextField(blank=True , null=True)
