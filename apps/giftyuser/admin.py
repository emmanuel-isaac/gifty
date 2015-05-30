from django.contrib import admin
from apps.giftyuser.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'activation_key', 'is_staff', 'is_active', 'phone']
    list_filter = ['is_superuser', 'is_staff']

admin.site.register(User, UserAdmin)

