from django.contrib import admin
from .models import News, Comment


class CommentInLine(admin.StackedInline):
    model = Comment
    exclude = ['user_name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    inlines = [CommentInLine]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_comment')
    list_filter = ('user_name',)
