from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'page_count', 'isbn']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
