"""Form for custom artwork request app."""
from django import forms
from .models import CustomArtworkRequest


class CustomArtworkRequestForm(forms.ModelForm):
    """Form for submitting custom artwork requests."""

    class Meta:
        """Meta class for CustomArtworkRequestForm."""

        model = CustomArtworkRequest
        fields = ['name', 'email', 'phone_number',
                  'category', 'description', 'size',
                  'medium', 'surface', 'reference_image']
