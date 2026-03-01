"""
Centralized form definitions for the users app.
Validation is handled here — views and services stay clean.
"""
from django import forms
from .models import Custom_user


class UserRegistrationForm(forms.ModelForm):
    """
    ModelForm for user registration wizard.
    Supports both Rider and Tenant user types.
    Leverages Django's built-in validation (unique email, required fields, etc.)
    """

    class Meta:
        model = Custom_user
        fields = [
            'user_type',
            'first_name', 'last_name', 'email', 'phone', 'address', 'picture',
            'license_number', 'license_expiry_date', 'license_image',
            'ejari_number', 'ejari_expiry_date', 'ejari_image',
        ]
        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Custom_user.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Custom_user.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A user with this phone number already exists.")
        return phone
