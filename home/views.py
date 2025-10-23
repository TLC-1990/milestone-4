from django.shortcuts import render

def index(request):
    """A view to return the index page."""
    return render(request, 'home/index.html')

def artist_biography(request):
    """A view to return the artist biography page."""
    return render(request, 'home/artist_biography.html')