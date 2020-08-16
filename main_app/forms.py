from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField

from .models import URLModel


class URLForm(forms.ModelForm):
    class Meta:
        model = URLModel
        fields = ['url']


class UserRegistrationForm(forms.ModelForm):
    username = UsernameField(min_length=1, max_length=255)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8, label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError(message='Не совпадают два пароля')
        if len(password2) < 8:
            raise ValidationError(message='Слишком короткий пароль')
        return password2

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        return user


class URLForm(forms.ModelForm):
    url = forms.CharField(label='url')
    slug = forms.CharField(label='slug', disabled=True)

    class Meta:
        model = URLModel
        fields = ('url', 'slug',)
