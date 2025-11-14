"""URL configuration for the home app."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('biography/', views.artist_biography, name='artist_biography'),
]
