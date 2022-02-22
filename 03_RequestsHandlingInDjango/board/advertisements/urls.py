from django.urls import path
from . import views

urlpatterns = [
    # path('', views.advertisement_list, name='advertisement_list'),
    path('', views.Main.as_view()),
    path("contacts/", views.contacts, name='contacts'),
    path("about/", views.about, name='about'),
    path("categories/", views.categories, name='categories'),
    path("regions1/", views.regions1, name='regions1'),
    path("regions2/", views.Regions2.as_view()),
    path("advertisements/", views.Advertisements.as_view()),
    path("tv_contacts/", views.Contacts.as_view()),
    path("tv_about/", views.About.as_view())

]
