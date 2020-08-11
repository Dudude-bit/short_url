from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

regex = r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\(\)\*\+,;=.]+$'


class URLModel(models.Model):
    url = models.CharField(max_length=1023, validators=[RegexValidator(regex=regex)])
    slug = models.CharField(max_length=8)
