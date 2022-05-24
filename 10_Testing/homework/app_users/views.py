from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View

from .forms import RegisterForm, UserForm
from .models import Profile
from django.contrib.auth.views import LoginView, LogoutView


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            description = form.cleaned_data.get('description')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                description=description,
                city=city
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            form.add_error('__all__', 'Пользователь под таким именем уже существует!')
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})


class UserEditFormView(View):
    def get(self, request, user_id):
        if not request.user.is_authenticated:
            raise PermissionDenied()
        user = Profile.objects.get(id=user_id)
        user_form = UserForm(instance=user)
        return render(request, 'users/user_edit.html', context={'user_form': user_form,
                                                                'user_id': user_id})

    def post(self, request, user_id):
        user = Profile.objects.get(id=user_id)
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user.save()
        return render(request, 'users/user_edit.html', context={'user_form': user_form,
                                                                'user_id': user_id})


class Login(LoginView):
    template_name = 'users/login.html'


class Logout(LogoutView):
    template_name = 'users/logout.html'
    next_page = 'main'
