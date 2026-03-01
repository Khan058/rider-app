from django.contrib import admin
from .models import Apartment


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    """Admin configuration for Apartment model."""

    list_display = ('unit_number', 'building_name', 'floor', 'status', 'monthly_rent', 'tenant')
    list_filter = ('status', 'city', 'bedrooms')
    search_fields = ('unit_number', 'building_name', 'address', 'tenant__first_name', 'tenant__last_name')
    ordering = ('-created_at',)

    fieldsets = (
        ('Apartment Details', {
            'fields': ('unit_number', 'building_name', 'floor', 'bedrooms', 'bathrooms', 'area_sqft', 'image'),
        }),
        ('Location', {
            'fields': ('address', 'city'),
        }),
        ('Financial', {
            'fields': ('monthly_rent',),
        }),
        ('Assignment', {
            'fields': ('tenant', 'status'),
        }),
    )
