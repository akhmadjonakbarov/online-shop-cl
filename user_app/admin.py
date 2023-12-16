from django.contrib import admin
from .models import CustomUser, SuperAdminGroup, AdminGroup, UserLocation

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(SuperAdminGroup)
admin.site.register(AdminGroup)
admin.site.register(UserLocation)
