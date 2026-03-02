"""
Centralized form definitions for the bikes app.
Validation is handled here — views and services stay clean.
"""
from django import forms
from .models import Bike


class BikeForm(forms.ModelForm):
    """
    ModelForm for bike creation and editing.
    Leverages Django's built-in validation for max_length and FK validity.
    """

    class Meta:
        model = Bike
        fields = ['model', 'registration', 'rider']
        widgets = {
            'rider': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_registration(self):
        registration = self.cleaned_data.get('registration')
        qs = Bike.objects.filter(registration__iexact=registration)
        # Exclude current instance when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A bike with this registration number already exists.")
        return registration
