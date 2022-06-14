from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainShopListView.as_view(), name='main'),
    path('account/', views.account, name='account'),
    path('account/account_refill', views.AccountRefillView.as_view(), name='account_refill'),

]
