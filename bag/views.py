from django.shortcuts import redirect, render

def view_bag(request):
    """A view to return the shopping bag page."""
    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """A view to add a specified product to the shopping bag."""

    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})
    bag[item_id] = bag.get(item_id, 0) + 1
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)