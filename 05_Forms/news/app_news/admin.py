from django.contrib import admin
from app_news.models import News, Comment
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

