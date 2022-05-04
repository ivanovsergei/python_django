from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    city = forms.CharField(help_text='Город')
    telephone = forms.CharField(help_text='Номер телефона')

    class Meta:
        model = User
        fields = ('username', 'city', 'telephone', 'password1', 'password2',)
