"""App configuration for custom artwork request app."""
from django import forms
from .models import CustomArtworkRequest

class CustomArtworkRequestForm(forms.ModelForm):
    class Meta:
        model = CustomArtworkRequest
        fields = ['category', 'description', 'size', 'material', 'surface', 'reference_image']
        