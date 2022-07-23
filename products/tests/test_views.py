""" Imports """
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product


class TestViews(TestCase):
    """ Test product views """

    def setUp(self):
        """ Set up """
        self.admin = User.objects.create(
            username="admin",
            password="admin",
            is_superuser=True
        )
        self.client.force_login(self.admin)

        self.category = Category.objects.create(
            name="test",
            friendly_name="Test"
        )

        self.product = Product.objects.create(
            category=self.category,
            name='Test',
            description='Test',
            price='10'
            )

    def test_all_products_view(self):
        """ Test all products view """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_view(self):
        """ Test product detail view """
        response = self.client.get(f'/products/{ self.product.id }/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_view(self):
        """ Test add product view """
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_edit_product_view(self):
        """ Test edit product view """
        response = self.client.get(f'/products/edit/{ self.product.id }/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
