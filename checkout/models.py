import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

COUNTRY_CHOICES = [('UK', 'United Kingdom')]

class Order(models.Model):
    order_number = models.CharField(max_length=32, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True)
    county = models.CharField(max_length=80, blank=True, choices=COUNTRY_CHOICES, default='UK')
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    original_bag = models.TextField()
    stripe_pid = models.CharField(max_length=254)

    def _generate_order_number(self):
        """Generate a random, unique order number using UUID"""
        
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """Override the original save method to set the order number if it hasn't been set already."""
        
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def update_total(self):
        """Update grand total each time a line item is added, accounting for delivery costs."""
        
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    
class OrderLineItem(models.Model):
    
    """A line item within an order, representing a specific product and quantity."""
    
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey('products.Product', null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Item: {self.product.name} on order {self.order.order_number}'