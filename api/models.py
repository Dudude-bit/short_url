from django.db import models

# Create your models here.


class URLModel(models.Model):
    url = models.CharField(max_length=1023)
    slug = models.CharField(max_length=8)
