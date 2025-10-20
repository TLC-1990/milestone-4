from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomArtworkRequest
from .forms import CustomArtworkRequestForm

# Create your views here.

@login_required
def custom_artwork_request(request):
    """ A view to handle custom artwork requests """

    if request.method == 'POST':
        form = CustomArtworkRequestForm(request.POST)
        if form.is_valid():
            custom_request = form.save(commit=False)
            custom_request.user = request.user
            custom_request.save()
            return redirect('request_success')
        else: 
            form = CustomArtworkRequestForm()
            return render(request, 'custom_artwork_request/custom_artwork_request_form.html', {'form': form})

@login_required
def my_requests(request):
    """
    Display all custom artwork requests for the logged-in user.
    """
    requests = CustomArtworkRequest.objects.filter(user=request.user)
    return render(request, 'custom_artwork_request/my_requests.html', {'requests': requests})
