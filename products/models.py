from django.db import models


# Create your models here.

class Category(models.Model):
    """
    Represents a category for grouping products.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name=models.CharField(max_length=254)
    friendly_name=models.CharField(max_length=254,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    """
    Represents the fields of a product in the e-commerce store.
    """
    category=models.ForeignKey('Category',null=True,blank=True,on_delete=models.SET_NULL)
    name=models.CharField(max_length=254)
    description=models.TextField()
    dimensions=models.CharField(max_length=254)
    material=models.CharField(max_length=254)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(null=True,blank=True)
    # featured_image removed (was CloudinaryField)
    
    def __str__(self):
        return self.name
