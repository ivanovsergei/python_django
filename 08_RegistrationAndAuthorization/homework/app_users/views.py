from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .models import Profile
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            telephone = form.cleaned_data.get('telephone')
            Profile.objects.create(
                user=user,
                city=city,
                telephone=telephone,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            form = RegisterForm()
            return render(request, 'users/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})


class LoginView(LoginView):
    template_name = 'users/login.html'


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
