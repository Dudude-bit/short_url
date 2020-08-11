from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import URLSerializer
from .services import generate_slug, normalize_url
from .models import URLModel


class CreateURL(generics.CreateAPIView):
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data._mutable = True
        serializer.initial_data['slug'] = generate_slug()
        serializer.initial_data._mutable = False
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['url'] = normalize_url(serializer.validated_data['url'])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetURL(generics.RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = URLSerializer
    queryset = URLModel.objects.all()
