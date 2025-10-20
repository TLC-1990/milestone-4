from django import forms
from .models import CustomArtworkRequest

class CustomArtworkRequestForm(forms.ModelForm):
    class Meta:
        model = CustomArtworkRequest
        fields = ['category', 'description', 'size', 'material', 'surface']