from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin


class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

    actions = ['activate_users', 'deactivate_users']

    @admin.action(description='Activate selected users')
    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Deactivate selected users')
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)


# Unregister default User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
