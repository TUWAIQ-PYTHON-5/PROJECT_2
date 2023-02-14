from django.db import models

class POST(models.Model):
    Your_Name = models.CharField(max_length=100)
    Enter_Email = models.EmailField(max_length=200)
    Send_Message = models.CharField(max_length=100)
    
    

class Comment(models.Model):
    Name = models.CharField(max_length=100)
    your_comment = models.CharField(max_length=512)
    