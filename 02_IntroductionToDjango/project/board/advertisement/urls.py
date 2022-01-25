from django.urls import path
from .import views

urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path("advertisement", views.advertisement, name='advertisement'),
    path("programming", views.programming, name='programming'),
    path("design", views.design, name='design'),
    path("marketing", views.marketing, name='marketing'),
    path("management", views.management, name='management'),
    path("games", views.games, name='games')

]
