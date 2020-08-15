from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, AnonymousUser

# Create your models here.

regex = r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\(\)\*\+,;=.]+$'


class URLModel(models.Model):
    url = models.CharField(max_length=1023, validators=[RegexValidator(regex=regex)], null=False)
    slug = models.CharField(max_length=8, unique=True, db_index=True, null=False)
    _user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE)