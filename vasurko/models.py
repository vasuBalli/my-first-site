from django.db import models

# Create your models here.
class userdata(models.Model):
    name = models.CharField(max_length=255)
class Title(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField()
    def __str__(self):
        return self.title