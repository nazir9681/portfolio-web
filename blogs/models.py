from django.db import models
from datetime import datetime


# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="image/")
    def __str__(self):
        return self.title

    def summary(self):
        data =  self.body.split()[:40]
        str1 = " "  
        for ele in data:  
            return (str1.join(data))    

    def timeBlog(self):
        return self.pub_date.strftime("%d %b, %Y")