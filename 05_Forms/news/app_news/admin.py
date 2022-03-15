from django.contrib import admin
from app_news.models import User, News, Comment
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

