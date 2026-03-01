from django.db import models
from django.conf import settings


class Apartment(models.Model):
    STATUS_CHOICES = [
        ('VACANT', 'Vacant'),
        ('OCCUPIED', 'Occupied'),
        ('MAINTENANCE', 'Under Maintenance'),
    ]

    # Tenant assignment
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='apartments',
        limit_choices_to={'user_type': 'TENANT'},
    )

    # Apartment details
    unit_number = models.CharField(max_length=20, unique=True)
    building_name = models.CharField(max_length=100)
    floor = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    area_sqft = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Location
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100, default='Dubai')

    # Financial
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)

    # Status
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='VACANT')

    # Apartment image
    image = models.ImageField(upload_to='apartments/', null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.building_name} - Unit {self.unit_number}"
