from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    #auto_now_add{Only add time and date in first time it will added to data base ,after that no changes , unless change it manually}
    #auto_now{add date time in first add , and updated each time i do updating}
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")

class replay(models.Model):
    name = models.CharField(max_length=512)
    replayMsg = models.TextField()
    replay_for_blog = models.ForeignKey(blog ,on_delete=models.CASCADE)
    replay_date = models.DateField(auto_now_add=True) 


class contactMeData(models.Model):

    cf_name = models.CharField(max_length=512)
    cf_email = models.CharField(max_length=512)
    cf_message = models.TextField()




