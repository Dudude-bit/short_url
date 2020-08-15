from rest_framework import serializers
from main_app.models import URLModel
from . import services


class URLSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=services.CurrentUserDefault())

    class Meta:
        model = URLModel
        fields = '__all__'
