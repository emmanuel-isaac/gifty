from django.contrib import admin
from apps.gift.models import GiftPack, GiftItem

# Register your models here.

class GiftPackAdmin(admin.ModelAdmin):

	list_display = ['name', 'packaging_cost', 'pack_price', 'items']
	list_filter = ['name']

class GiftItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']
	list_filter = ['price']






admin.site.register(GiftPack, GiftPackAdmin)
admin.site.register(GiftItem, GiftItemAdmin)