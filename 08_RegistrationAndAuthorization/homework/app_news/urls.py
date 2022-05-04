from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainNewsListView.as_view(), name='news_list'),
    path('news/news_add', views.NewsFormView.as_view()),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name='news-detail'),
    path('comment/comment_add/<int:news_pk>', views.CommentFormView.as_view(), name='comment_add'),

]
