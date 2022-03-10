from django.contrib import admin
from ads.models import Advertisement, AdvertisementAuthor
# Register your models here.


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'closed_at')


@admin.register(AdvertisementAuthor)
class AdvertisementAuthor(admin.ModelAdmin):
    pass
