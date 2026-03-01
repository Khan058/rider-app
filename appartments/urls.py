from django.urls import path
from . import views

urlpatterns = [
    path('tenants/', views.tenants, name='tenants'),
    path('tenants/register/', views.register_tenant, name='register_tenant'),
    path('apartments/', views.apartments, name='apartments'),
    path('apartments/register/', views.register_apartment, name='register_apartment'),
    path('apartments/<int:apartment_id>/edit/', views.edit_apartment, name='edit_apartment'),
]
