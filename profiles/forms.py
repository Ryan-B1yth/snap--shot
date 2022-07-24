""" Imports """
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """ Profile form """
    class Meta:
        """ Meta data """
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_country': '',
            'default_city': 'City',
            'default_address_1': 'Address line 1',
            'default_address_2': 'Address line 2',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
