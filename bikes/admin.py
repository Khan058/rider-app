from django.contrib import admin
from .models import Bike, Maintenance

# Register your models here.

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('model', 'registration', 'rider', 'created_at', 'updated_at')

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('bike', 'description', 'cost', 'status', 'date', 'previous_maintenance_date', 'next_maintenance_date', 'created_at', 'updated_at')
    list_filter = ('status', 'date')
    search_fields = ('bike__registration', 'description')