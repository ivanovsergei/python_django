from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainShopListView.as_view(), name='main'),
    path('account/', views.account, name='account'),
    path('account/account_refill', views.AccountRefillView.as_view(), name='account_refill'),
    path('good_detail/<int:id>', views.good_detail, name='good_detail'),
    path('good_filter/<int:pk>', views.good_filter, name='good_filter'),

]
