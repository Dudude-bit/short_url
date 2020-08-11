from django.urls import path
from .views import CreateURL, GetURL

urlpatterns = [
    path('create/', CreateURL.as_view()),
    path('get/<str:slug>', GetURL.as_view())
]

app_name = 'api'
