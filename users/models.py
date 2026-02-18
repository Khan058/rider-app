from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_user(AbstractUser):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    license_expiry_date = models.DateField()
    license_image = models.ImageField(upload_to='licenses/')
    ejari_number = models.CharField(max_length=100, null=True, blank=True)
    ejari_expiry_date = models.DateField(null=True, blank=True)
    ejari_image = models.ImageField(upload_to='ejaris/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    # add other fields as needed

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
