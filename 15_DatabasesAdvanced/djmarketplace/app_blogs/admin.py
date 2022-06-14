from django.contrib import admin
from .models import Blog, Author, Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


