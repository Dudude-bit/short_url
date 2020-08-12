from django.urls import path, re_path
from .views import CreateURL, GetURL, DeleteURL

urlpatterns = [
    path('create/', CreateURL.as_view()),
    re_path('^get/(?P<slug>[a-zA-z]{8})$', GetURL.as_view()),
    re_path(r'^delete/(?P<slug>[a-zA-z]{8})$', DeleteURL.as_view())
]

app_name = 'api'
