from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    description = forms.CharField(max_length=1000, help_text='О себе')
    city = forms.CharField(max_length=36, required=False, help_text='Город')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'description',)
