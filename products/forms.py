""" Imports """
from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """ Product form """
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'description',
            'price',
            'rating',
            'image'
            ]

    image = forms.ImageField(
        label='Image',
        required=False
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class ReviewForm(forms.ModelForm):
    """ Review form """
    class Meta:
        model = Review
        fields = '__all__'

        widgets = {
            'user': forms.HiddenInput(),
            'product': forms.HiddenInput()
        }
