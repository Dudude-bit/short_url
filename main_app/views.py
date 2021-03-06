from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from main_app.models import URLModel
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView


class RedirectURL(View):

    def get(self, request, slug):
        url = get_object_or_404(URLModel, slug=slug).url
        return redirect(url)


class MainPageView(View):

    def get(self, request):
        return render(request, 'main_page.html')


class CreateUser(FormView):
    form_class = UserRegistrationForm
    template_name = 'create_user.html'
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super(CreateUser, self).form_valid(form)


class Login(LoginView):
    template_name = 'create_user.html'
