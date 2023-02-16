from django.db import models

# Create your models here.


class owner(models.Model):

    title = models.CharField(max_length=102)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

