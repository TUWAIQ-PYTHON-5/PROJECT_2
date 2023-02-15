from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.ImageField(upload_to="images/", default="images/default.svg")
    commentDate = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    message = models.CharField(max_length=512)