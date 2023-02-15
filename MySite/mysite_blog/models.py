from django.db import models

# Create your models here.


class Posts(models.Model):

    title = models.CharField(max_length=1024)
    content =  models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    publish_date = models.DateTimeField(auto_now_add=True)
    
    
class Comment(models.Model):

    post_name = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=102)
    content =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
