from rest_framework import serializers
from .models import URLModel
from .services import generate_slug


class URLSerializer(serializers.ModelSerializer):

    class Meta:
        model = URLModel
        fields = ['url']

