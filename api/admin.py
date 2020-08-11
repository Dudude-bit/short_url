from django.contrib import admin
from .models import URLModel


# Register your models here.

@admin.register(URLModel)
class URLModelAdmin(admin.ModelAdmin):
    pass
