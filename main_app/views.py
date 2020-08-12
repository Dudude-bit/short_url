from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from api.models import URLModel


class RedirectURL(View):

    def get(self, request, slug):
        url = get_object_or_404(URLModel, slug=slug).url
        return redirect(url)
