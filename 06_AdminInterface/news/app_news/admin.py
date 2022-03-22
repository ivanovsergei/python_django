from django.contrib import admin
from app_news.models import News, Comment
# Register your models here.


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'status')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('status',)
    inlines = [CommentInLine]

    actions = ['mark_as_published', 'mark_as_not_published']

    def mark_as_published(self, request, queryset):
        queryset.update(status='p')

    def mark_as_not_published(self, request, queryset):
        queryset.update(status='n')

    mark_as_published.short_description = 'Перевести в статус "Опубликован"'
    mark_as_not_published.short_description = 'Перевести в статус "Неопубликован"'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'comment', 'status')
    list_filter = ('user_name',)

    actions = ['mark_as_active', 'mark_as_not_deleted_by_admin']

    def mark_as_active(self, request, queryset):
        queryset.update(status='a')

    def mark_as_not_deleted_by_admin(self, request, queryset):
        queryset.update(status='d')

    mark_as_active.short_description = 'Перевести в статус "Активно"'
    mark_as_not_deleted_by_admin.short_description = 'Перевести в статус "Удалено Администратором"'
