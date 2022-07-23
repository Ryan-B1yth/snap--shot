""" Imports """
from django.test import TestCase
from django.shortcuts import reverse
from products.models import Category, Product


class TestViews(TestCase):
    """ Test basket views """
    def setUp(self):
        """ Set up """
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

        self.basket = {
            f'{self.product.id}': "5",
        }

    def test_basket_view(self):
        """ Test basket view """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_basket_url(self):
        """ Test basket url """
        response = self.client.get(reverse('basket'))
        self.assertEqual(response.status_code, 200)
