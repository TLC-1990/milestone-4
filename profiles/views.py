"""Views for the profiles app."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from custom_artwork_request.models import CustomArtworkRequest
from checkout.models import Order

@login_required
def profiles(request):
    """Display the user's profile, orders, and custom artwork requests."""
    if request.user.is_superuser:
        orders = Order.objects.all().order_by('-date')
        user_requests = CustomArtworkRequest.objects.all()
    else:
        orders = Order.objects.filter(user_profile__user=request.user).order_by('-date')
        user_requests = CustomArtworkRequest.objects.filter(user=request.user)
    profile = request.user.userprofile
    context = {
        'orders': orders,
        'user_requests': user_requests,
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', context)

