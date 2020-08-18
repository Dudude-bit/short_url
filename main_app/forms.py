from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField

from api.services import generate_slug
from .models import URLModel


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    username = UsernameField(min_length=1, max_length=255)
    password1 = forms.CharField(min_length=8, label='Пароль', widget=forms.PasswordInput, error_messages={
        'min_length': 'Ваш пароль слишком короткий'
    })
    password2 = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput, error_messages={
        'min_length': 'Ваш пароль слишком короткий'
    })

    class Meta:
        model = User
        fields = ('username',)

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError(message='Не совпадают два пароля')
        return password1

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)


class URLForm(forms.ModelForm):
    url = forms.CharField(label='url')
    slug = forms.CharField(label='slug', widget=forms.TextInput(attrs=
                                                                {'readonly': 'readonly'}))

    class Meta:
        model = URLModel
        fields = ('url', 'slug',)
