from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .serializers import URLSerializer
from .services import generate_slug, normalize_url, delete_slug
from main_app.models import URLModel
from .permission_classes import IsOwner
from rest_framework.permissions import IsAuthenticated


class CreateURL(generics.CreateAPIView):
    serializer_class = URLSerializer


    @csrf_exempt
    def post(self, request, *args, **kwargs):
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
            detail = e.detail.get('url', None)
            if detail:
                if detail[0].code == 'unique':
                    obj = URLModel.objects.filter(url=request.data['url'])[0]
                    serializer = self.get_serializer(obj)
                    headers = self.get_success_headers(serializer.data)
                    return Response(serializer.data, status = status.HTTP_201_CREATED, headers=headers)
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
