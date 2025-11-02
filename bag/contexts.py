from decimal import Decimal
from django.conf import settings
#from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    """ A context processor to add the shopping bag contents to the context. """
    
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    for item_id in list(bag):
        try:
            product = Product.objects.get(pk=item_id)
            total += product.price
            product_count += 1
            bag_items.append({
               'item_id': item_id,
               'product': product,
       })
        except Product.DoesNotExist:
            del bag[item_id]
            request.session['bag'] = bag
            continue
        
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total
    
    local_collection = request.session.get('local_collection', False)
    delivery = 0 if local_collection else total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'local_collection': local_collection,
        'grand_total': grand_total,
    }
    return context
