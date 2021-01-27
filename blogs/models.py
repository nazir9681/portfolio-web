from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="image/")
    def __str__(self):
        return self.title
