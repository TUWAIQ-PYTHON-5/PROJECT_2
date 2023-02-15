from django.db import models

# Create your models here.
class Contact(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    massage = models.TextField(max_length=500)


