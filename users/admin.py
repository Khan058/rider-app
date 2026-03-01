from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Custom_user


@admin.register(Custom_user)
class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for Custom_user.
    Organizes fields into logical fieldsets with user_type dropdown.
    """

    list_display = ('email', 'first_name', 'last_name', 'user_type', 'phone', 'is_active')
    list_filter = ('user_type', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('User Type', {'fields': ('user_type',)}),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'picture'),
        }),
        ('Location', {
            'fields': ('city', 'state', 'zip_code', 'country'),
            'classes': ('collapse',),
        }),
        ('License Details', {
            'fields': ('license_number', 'license_expiry_date', 'license_image'),
            'classes': ('collapse',),
            'description': 'Required for Riders only.',
        }),
        ('Ejari Details', {
            'fields': ('ejari_number', 'ejari_expiry_date', 'ejari_image'),
            'classes': ('collapse',),
            'description': 'Required for Riders only.',
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',),
        }),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('User Type', {'fields': ('user_type',)}),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address'),
        }),
    )
