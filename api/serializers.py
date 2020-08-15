from rest_framework import serializers
from main_app.models import URLModel
from .services import generate_slug


class URLSerializer(serializers.ModelSerializer):
    _user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = URLModel
        fields = '__all__'
