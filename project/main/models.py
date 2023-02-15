from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=1024)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)