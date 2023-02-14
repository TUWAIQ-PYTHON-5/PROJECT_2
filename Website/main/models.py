from django.db import models

class Contact(models.Model):

    name = models.CharField(max_length=1024)
    email= models.EmailField()
    content = models.TextField()
