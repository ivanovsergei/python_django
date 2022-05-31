from django.contrib import admin
from .models import Shop, Client, Promotion, Balance, PaymentHistory


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user']


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['amount', 'user']


@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ['good', 'price', 'user']
