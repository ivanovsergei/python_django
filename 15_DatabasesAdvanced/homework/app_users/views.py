from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_id = request.user.id
            return redirect('/')
        else:
            form.add_error('__all__', 'Пользователь под таким именем уже существует!')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


class Login(LoginView):
    template_name = 'login.html'


class Logout(LogoutView):
    next_page = 'main'
