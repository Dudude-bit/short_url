from django.forms import ModelForm
from .models import URLModel


class URLForm(ModelForm):

    class Meta:
        model = URLModel
        fields = ['url']