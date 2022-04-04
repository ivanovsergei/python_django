from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('another_login/', views.AnotherLoginView.as_view(), name='another_login'),
    path('another_logout/', views.AnotherLogoutView.as_view(), name='another_logout'),
]
