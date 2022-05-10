from django.contrib import admin
from .models import Item, File


class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'price')


admin.site.register(Item, ItemAdmin)


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')


admin.site.register(File, FileAdmin)
