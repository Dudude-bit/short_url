from rest_framework import generics
from .serializers import URLSerializer
from .services import generate_slug, normalize_url


class CreateURL(generics.CreateAPIView):
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['slug'] = generate_slug()
        request.data['url'] = normalize_url(request.data.get('url'))
        request.data._mutable = False
        return super().create(request, *args, **kwargs)
