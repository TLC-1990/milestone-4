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
    MEDIUM_CHOICES = [
        ('acrylics', 'Acrylics'),
        ('artists_choice', "Artist's Choice"),
        ('oil_paints', 'Oil Paints'),
        ('oil_pastels', 'Oil Pastels'),
        ('chalk_pastels', 'Chalk Pastels'),
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
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='portrait')
    description = models.TextField(required=True)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default='small')
    medium = models.CharField(max_length=20, choices=MEDIUM_CHOICES, default='artists_choice')
    surface = models.CharField(max_length=20, choices=SURFACE_CHOICES, default='canvas')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='under_consideration')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reference_image = models.ImageField(upload_to='custom_artwork_references/', blank=True, null=True)

    def __str__(self):
        return f"Custom Artwork Request by {self.user.username} - {self.category} ({self.status})"