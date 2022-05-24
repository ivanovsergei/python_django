from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('user/<int:user_id>/edit', views.UserEditFormView.as_view()),

]
