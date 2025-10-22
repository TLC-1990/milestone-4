"""Admin configuration for custom artwork requests."""
from django.contrib import admin
from .models import CustomArtworkRequest

admin.site.register(CustomArtworkRequest)
