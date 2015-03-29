from django.contrib import admin
from apps.gift.models import GiftPack, GiftItem

# Register your models here.

class GiftItemInline(admin.TabularInline):

	model = GiftItem
	extra = 3


class GiftPackAdmin(admin.ModelAdmin):

	inlines = [GiftItemInline]
	list_display = ['name', 'price']
	list_filter = ['price']

class GiftItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']
	list_filter = ['price']






admin.site.register(GiftPack, GiftPackAdmin)
admin.site.register(GiftItem, GiftItemAdmin)