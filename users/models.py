from django.db import models
from django.contrib.auth.models import AbstractUser


class Custom_user(AbstractUser):
    USER_TYPE_CHOICES = [
        ('RIDER', 'Rider'),
        ('TENANT', 'Tenant'),
    ]

    # User type — determines which fields are relevant
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default='RIDER',
    )

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)

    # Location fields
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    # Rider-specific fields (optional for Tenants)
    license_number = models.CharField(max_length=100, blank=True, default='')
    license_expiry_date = models.DateField(null=True, blank=True)
    license_image = models.ImageField(upload_to='licenses/', null=True, blank=True)
    ejari_number = models.CharField(max_length=100, null=True, blank=True)
    ejari_expiry_date = models.DateField(null=True, blank=True)
    ejari_image = models.ImageField(upload_to='ejaris/', null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
