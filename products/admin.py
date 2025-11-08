from django.contrib import admin
from .models import Product,Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image', 'material', 'dimensions', 'sold')
    search_fields = ('name', 'description', 'material')
    list_filter = ('category',)
    
    ordering = ('category', 'name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    search_fields = ('friendly_name', 'name')

admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)
