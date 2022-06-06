from django.urls import path
from .views import BookListMixin, AuthorListMixin


urlpatterns = [
    path('books/', BookListMixin.as_view(), name='books'),
    path('authors/', AuthorListMixin.as_view(), name='authors'),

]
