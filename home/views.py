"""Views for the home app."""
from django.shortcuts import render


def index(request):
    """Return a view to show the index page."""
    return render(request, 'home/index.html')


def artist_biography(request):
    """Return a view to show the artist biography page."""
    return render(request, 'home/artist_biography.html')
