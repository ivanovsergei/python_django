from django.contrib import admin
from .models import Shop, Client, Promotion


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
