"""URL configuration for the bag app."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('set-collection-option/', views.set_collection_option, name='set_collection_option'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]
