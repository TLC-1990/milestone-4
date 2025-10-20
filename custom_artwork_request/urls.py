from django.urls import path
from . import views

urlpatterns = [
    path('custom-artwork-request/', views.custom_artwork_request, name='custom_artwork_request'),
]