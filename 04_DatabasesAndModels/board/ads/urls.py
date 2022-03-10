from django.urls import path
from . import views
from .views import AdvertisementListView, AdvertisementDetailView


urlpatterns = [
    path("", views.advertisement, name='advertisement'),
    path("advertisements", AdvertisementListView.as_view(), name='advertisement_list'),
    path("advertisements/<int:pk>", AdvertisementDetailView.as_view(), name='advertisement-detail'),
]
