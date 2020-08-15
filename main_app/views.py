from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from main_app.models import URLModel
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class RedirectURL(View):

    def get(self, request, slug):
        url = get_object_or_404(URLModel, slug=slug).url
        return redirect(url)


class CreateUser(FormView):
    form_class = UserCreationForm
    template_name = 'create_user.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        User.objects.create_user(username=username, password=password)
        return super(CreateUser, self).form_valid(form)


class Login(LoginView):
    template_name = 'create_user.html'
