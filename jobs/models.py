from django.db import models

# Create your models here.

class Jobs(models.Model):
    image       = models.ImageField(upload_to='image/')
    title       = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title 