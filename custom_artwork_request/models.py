"""Models for custom artwork requests."""
from django.db import models
from django.contrib.auth.models import User

class CustomArtworkRequest(models.Model):
    """
    Represents a custom artwork request made by a user.
    """
    
    CATEGORY_CHOICES = [
        ('portrait', 'Portrait'),
        ('landscape', 'Landscape'),
        ('animals', 'Animals'),
        ('still_life', 'Still Life'),
    ]
    SIZE_CHOICES =[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('extra_large', 'Extra Large'),
    ]
    MATERIAL_CHOICES = [
        ('acrylics', 'Acrylics'),
        ('mixed_media', 'Mixed Media'),
        ('oil_paints', 'Oil Paints'),
        ('oil_pastels', 'Oil Pastels'),
        ('pencil', 'Pencil'),
        ('watercolors', 'Watercolors'),
    ]
    SURFACE_CHOICES = [
        ('canvas', 'Canvas'),
        ('paper', 'Paper'),
        ('board', 'Board'),
    ]
    
    STATUS_CHOICES = [
        ('under_consideration', 'Under Consideration'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
    ]
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=2000)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    surface = models.CharField(max_length=20, choices=SURFACE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='under_consideration')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Custom Artwork Request by {self.user.username} - {self.category} ({self.status})"