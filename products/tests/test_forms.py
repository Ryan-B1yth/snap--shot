""" Imports """
from django.test import TestCase
from django.contrib.auth.models import User
from products.forms import ProductForm, ReviewForm
from products.models import Category, Review, Product


class TestProductForm(TestCase):
    """ Test ProductForm """

    def setUp(self):
        """ Set up """
        self.user = User.objects.create(
                username="test",
                password="testpassword"
            )

        self.category = Category.objects.create(
            name='test',
            friendly_name='Test',
            )

        self.product = Product.objects.create(
            category=self.category,
            name='Test',
            description='test',
            price='10'
            )

        self.review = Review.objects.create(
            user=self.user,
            text="Test review",
            product=self.product
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

    def test_empty_review_form_invalid(self):
        """ Test empty review form invalid """
        form = ReviewForm({})
        self.assertFalse(form.is_valid())
    
    def test_review_form_invalid_without_user(self):
        """ Test review form invalid without user """
        form = ReviewForm({
            'user': '',
            'test': 'Test review',
            'product': self.product
        })
