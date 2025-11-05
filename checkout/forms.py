from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone_number', 
                  'country', 'postcode', 'town_or_city', 
                  'street_address1', 'street_address2', 'county']
        
    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto-generated 
        labels and set autofocus on first field."""
        
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }
        
        def clean(self):
            cleaned_data = super().clean()
            country = cleaned_data.get('country')
            postcode = cleaned_data.get('postcode')
            if country and country != 'UK':
                self.add_error('country', 'Currently, we only ship to the United Kingdom.')
        
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False