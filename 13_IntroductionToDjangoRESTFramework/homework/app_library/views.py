from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView


class BookListMixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        book_title = self.request.query_params.get('title')
        book_author = self.request.query_params.get('author')
        page_count_eq = self.request.query_params.get('eq')
        page_count_gt = self.request.query_params.get('gt')
        page_count_lt = self.request.query_params.get('lt')

        if book_title:
            queryset = queryset.filter(title=book_title)
        elif book_author:
            queryset = queryset.filter(author__last_name=book_author)
        elif page_count_eq:
            queryset = queryset.filter(page_count=page_count_eq)
        elif page_count_gt:
            queryset = queryset.filter(page_count__gt=page_count_gt)
        elif page_count_lt:
            queryset = queryset.filter(page_count__lt=page_count_lt)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class AuthorListMixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        book_title = self.request.query_params.get('title')
        if book_title:
            queryset = queryset.filter(first_name=book_title)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
