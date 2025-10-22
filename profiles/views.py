from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Order
from custom_artwork_request.models import CustomArtworkRequest

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    custom_requests = CustomArtworkRequest.objects.filter(user=request.user)
    return render(request, 'profiles/profile.html', {
        'orders': orders,
        'custom_requests': custom_requests,
    })