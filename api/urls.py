from django.urls import path
from .views import CreateURL

urlpatterns = [
    path('create/', CreateURL.as_view())
]


app_name = 'api'