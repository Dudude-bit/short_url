from django.http import HttpResponse
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .serializers import URLSerializer
from .services import generate_slug, normalize_url, delete_slug
from main_app.models import URLModel
from .permission_classes import IsOwner
from rest_framework.permissions import IsAuthenticated


class CreateURL(generics.CreateAPIView):
    serializer_class = URLSerializer

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if not request.data:
            return HttpResponse(status=400)
        else:
            request.data._mutable = True
            request.data['url'] = normalize_url(request.data.get('url', None))
            if request.data['url']:
                request.data['slug'] = generate_slug()
            request.data._mutable = False
        try:
            return super(CreateURL, self).post(request, *args, **kwargs)
        except ValidationError as e:
            slug = request.data['slug']
            delete_slug(slug)
            raise e


class GetURL(generics.RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = URLSerializer
    queryset = URLModel.objects.all()


class DeleteURL(generics.DestroyAPIView):
    lookup_field = 'slug'
    serializer_class = URLSerializer
    queryset = URLModel.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def delete(self, request, *args, **kwargs):
        delete_slug(request.data.get('slug'))
        return super(DeleteURL, self).delete(request, *args, **kwargs)
