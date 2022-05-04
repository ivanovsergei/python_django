from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
