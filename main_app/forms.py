from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.core.validators import MinLengthValidator
from .models import URLModel

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8, label='Пароль', widget=forms.PasswordInput, validators=[
        MinLengthValidator(8, message='Ваш пароль должен быть длиннее 8 символов'), ])
    password2 = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput, validators=[
        MinLengthValidator(8, message='Ваш пароль должен быть длиннее 8 символов'), ])

    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError(message='Не совпадают два пароля')
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
