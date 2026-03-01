"""
Centralized form definitions for the appartments app.
Validation is handled here — views and services stay clean.
"""
from django import forms
from .models import Apartment


class ApartmentForm(forms.ModelForm):
    """
    ModelForm for apartment creation and editing.
    Leverages Django's built-in validation.
    """

    class Meta:
        model = Apartment
        fields = [
            'unit_number', 'building_name', 'floor', 'bedrooms', 'bathrooms',
            'area_sqft', 'address', 'city', 'monthly_rent', 'status',
            'tenant', 'image',
        ]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'tenant': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_unit_number(self):
        unit_number = self.cleaned_data.get('unit_number')
        qs = Apartment.objects.filter(unit_number=unit_number)
        # Exclude current instance when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("An apartment with this unit number already exists.")
        return unit_number

    def clean(self):
        cleaned_data = super().clean()
        tenant = cleaned_data.get('tenant')
        status = cleaned_data.get('status')

        # Auto-manage status based on tenant presence
        if tenant and status != 'OCCUPIED':
            cleaned_data['status'] = 'OCCUPIED'
        elif not tenant and status == 'OCCUPIED':
            cleaned_data['status'] = 'VACANT'
            
        return cleaned_data
