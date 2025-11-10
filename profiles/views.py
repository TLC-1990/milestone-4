from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from custom_artwork_request.models import CustomArtworkRequest
from checkout.models import Order

@login_required
def profiles(request):
    orders = Order.objects.filter(user_profile__user=request.user).order_by('-date')
    user_requests = CustomArtworkRequest.objects.filter(user=request.user)
    context = {
        'orders': orders,
        'user_requests': user_requests,
    }
    return render(request, 'profiles/profile.html', context)