from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'name',
            'email',
            'phone_number',
            'address1',
            'address2',
            'city',
            'country',
            'county'
            'postcode',
            )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'city': 'City',
            'address1': 'Address line 1',
            'address2': 'Address line 2',
            'county': 'County',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
