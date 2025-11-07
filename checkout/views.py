from django.shortcuts import redirect, render, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    """ A view to return the checkout page """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51SBM0DRx0Cgi5lo6FwlDbCeqadUVxMGYI0TXS38dzDXbEaDIHUeRxHekWG49n6fvM1iJ037KjCb4RK0dgQI1D44l00sdIdvD6M',
        'client_secret': 'test_client_secret_123',
    }
    return render(request, template, context)
