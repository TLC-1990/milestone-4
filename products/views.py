"""Views for products in the e-commerce store."""
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_products(request):
    """Return a view to show all products, including sorting."""
    products = Product.objects.filter(sold=False)
    categories = None
    
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.get('category').split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
    context = {
        'products': products,
        'current_categories': categories,
    }
    return render(request, 'products/products.html', context)
   
def product_detail(request, product_id):
    """Return a view to show a single product's details."""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    
    }

    return render(request, 'products/product_detail.html', context)