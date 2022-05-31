from django.urls import path
from .views import MainView, welcome, view4_decorate_in_url
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('welcome', welcome, name='welcome'),
    path('decor_url', cache_page(30)(view4_decorate_in_url), name='decor_url'),

]
