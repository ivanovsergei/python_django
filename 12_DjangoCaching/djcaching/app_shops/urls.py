from django.urls import path
from . import views


urlpatterns = [
    path('page_with_cached_fragment', views.page_with_cached_fragment, name='page_with_cached_fragment'),
    path('login/', views.Login.as_view(), name='login'),
    path('promotions/', views.promotions, name='promotions'),

]
