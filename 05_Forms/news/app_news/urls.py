from django.urls import path
from .views import NewsListView, NewsFormView, NewsEditFormView, NewsDetailView

urlpatterns = [
    path("", NewsListView.as_view(), name='news_list'),
    path('news/news_add', NewsFormView.as_view()),
    path('news/<int:element_id>/edit', NewsEditFormView.as_view()),
    path("news/<int:pk>", NewsDetailView.as_view(), name='news-detail'),

]
