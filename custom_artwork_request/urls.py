"""URL configuration for custom artwork request app."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_artwork_request, name='custom_artwork_request'),
    path('success/', views.request_submission_success, name='request_submission_success'),
]
