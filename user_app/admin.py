from django.contrib import admin
from .models import CustomUser, SuperAdminGroup, AdminGroup, UserLocation

# Register your models here.

admin.site.register(SuperAdminGroup)
admin.site.register(AdminGroup)
admin.site.register(UserLocation)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ('is_seller',)
