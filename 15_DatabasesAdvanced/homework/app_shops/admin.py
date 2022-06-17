from django.contrib import admin
from .models import Shop, Good, Account


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'top_sell', 'created']
    list_editable = ['price', 'stock']
    list_filter = ['created']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'balance', 'status', 'spend_money']
