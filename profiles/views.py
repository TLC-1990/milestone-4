from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from custom_artwork_request.models import CustomArtworkRequest

@login_required
def profiles(request):
    user_requests = CustomArtworkRequest.objects.filter(user=request.user)
    context = {
        'user_requests': user_requests,
    }
    return render(request, 'profiles/profile.html', context)