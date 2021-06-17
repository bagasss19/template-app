from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    media = models.CharField(max_length=60)
    content = models.CharField(max_length=1000)