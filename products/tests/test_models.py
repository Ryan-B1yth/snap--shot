""" Imports """
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product, Review


class TestProductModels(TestCase):
    """ Test product models """
    def setUp(self):
        """ Generate test data """
        self.user = User.objects.create(
                username="test",
                password="testpassword"
            )

        self.category = Category.objects.create(
                name='test',
                friendly_name="Test"
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

    def test_review_text(self):
        """ Test product text """
        self.assertEqual(str(self.review.text), 'Test review')

    def test_review_product(self):
        """ Test review product """
        self.assertEqual(str(self.product.description), 'test')
