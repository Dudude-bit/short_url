from rest_framework import generics
from .serializers import URLSerializer

class CreateURL(generics.CreateAPIView):
    serializer_class = URLSerializer
