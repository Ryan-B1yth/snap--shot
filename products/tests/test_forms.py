""" Imports """
from django.test import TestCase
from products.forms import ProductForm
from products.models import Category


class TestProductForm(TestCase):
    """ Test ProductForm """

    def setUp(self):
        """ Set up """
        self.category = Category.objects.create(
            name='test',
            friendly_name='Test',
        )

    def test_empty_form_invalid(self):
        """ Test empty form invalid """
        form = ProductForm({})
        self.assertFalse(form.is_valid())

    def test_form_invalid_without_category(self):
        """ Test form without category """
        form = ProductForm({
            'category': None,
            'name': 'Test'
            })
        self.assertFalse(form.is_valid())

    def test_form_invalid_without_name(self):
        """ Test form without name """
        form = ProductForm({
            'category': self.category,
            'name': ''
            })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_form_invalid_without_price(self):
        """ Test form without price """
        form = ProductForm({
            'category': self.category,
            'name': 'Test',
            'price': ''
            })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
