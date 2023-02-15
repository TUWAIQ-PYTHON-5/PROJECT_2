from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=1024)
    email = models.EmailField(max_length = 254)
    message = models.TextField()