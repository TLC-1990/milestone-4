from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """A view to return the shopping bag page."""
    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """A view to add a specified product to the shopping bag."""

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})
    bag[item_id] = bag.get(item_id, 0) + 1
    request.session['bag'] = bag

    messages.success(request, f'Added {product.name} to your bag.')
    
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """A view to remove a specified product from the shopping bag."""
    print("remove_from_bag called")
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]
            request.session['bag'] = bag
            print(f"Removed {product.name} from bag")
            messages.success(request, f'Removed {product.name} from your bag.')
        return redirect('view_bag')
    
    except Exception as e:
        messages.error(request, f'Error removing {product.name} from your bag.')
        return HttpResponse(status=500)
    
def set_collection_option(request):
    """
    A view to set the local collection option in the 
    checkout process and remove shipping cost.
    """
    print("set_collection_option called")
    if request.method == 'POST':
        request.session['local_collection'] = 'local_collection' in request.POST
        print("success message set for collection option")
        messages.success(request, f'You have selected to collect your order locally.')
    return redirect('view_bag')