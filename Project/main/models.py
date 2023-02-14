from django.db import models

# Create your models here.
class Form(models.Model):
      name=models.CharField(max_length=50)
      email=models.EmailField()
      phone=models.IntegerField()
      gender=models.BooleanField()
      is_student=models.BooleanField()
      state=models.CharField(max_length=50)

    
      