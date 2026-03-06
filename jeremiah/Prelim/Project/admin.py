from django.contrib import admin
from .models import AdminProfile


class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'role')


admin.site.register(AdminProfile, AdminProfileAdmin)