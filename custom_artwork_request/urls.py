""""URL configuration for custom artwork request app."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_artwork_request, name='custom_artwork_request'),
]