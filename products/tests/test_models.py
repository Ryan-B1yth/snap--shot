""" Imports """
from django.test import TestCase
from products.models import Category, Product


class TestProductModels(TestCase):
    """ Test product models """
    def setUp(self):
        """ Generate test data """
        self.category = Category.objects.create(
                name='test',
                friendly_name="Test"
            )

        self.product = Product.objects.create(
            category=self.category,
            name='Test',
            description='Test',
            price='10'
            )

    def test_category_string(self):
        """ Test category string method """
        self.assertEqual(str(self.category), 'Test')

    def test_category_friendly(self):
        """ Test category friendly_name string method """
        self.assertEqual(str(self.category.friendly_name), 'Test')

    def test_product_string(self):
        """ Test product string method """
        self.assertEqual(str(self.product), "Test")

    def test_product_price(self):
        """ Test product price """
        self.assertEqual(str(self.product.price), '10')
