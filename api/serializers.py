from rest_framework import serializers
from .models import URLModel
from .services import generate_slug


class URLSerializer(serializers.ModelSerializer):
    slug = generate_slug()

    class Meta:
        model = URLModel
        fields = '__all__'

