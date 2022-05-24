from django.contrib import admin
from .models import Blog, File


@admin.register(Blog)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'username', 'created_at']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
