from django.contrib import admin
from .models import Maids

# Register your models here.

@admin.register(Maids)
class MaidsAdmin(admin.ModelAdmin):
    list_display = ('maid', 'work_location', 'salary', 'company_pay', 'experience', 'salary_paid', 'created_at', 'updated_at')
    list_filter = ('salary_paid', 'work_location', 'experience')
    search_fields = ('maid__first_name', 'maid__last_name', 'work_location')