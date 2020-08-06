from rest_framework import generics
from .serializers import URLSerializer
from .services import generate_slug


class CreateURL(generics.CreateAPIView):
    serializer_class = URLSerializer

