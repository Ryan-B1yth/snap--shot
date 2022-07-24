""" Imports """
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from checkout.models import Order, OrderLineItem
from products.models import Category, Product


class TestViews(TestCase):
    """ Test profile views """
    def setUp(self):
        """ Set up """
        self.user = User.objects.create(
            username="test",
            password="testpassword"
            )

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

        self.order = Order.objects.create(
            name='test_name',
            email='email@email.com',
            phone_number='123123',
            address_1='test',
            address_2='test',
            city='test',
            country='test',
            county='test',
            postcode='test',
            )

        self.lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

        self.client.force_login(self.user)

    def test_profile_view(self):
        """ Test profile view"""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_url(self):
        """ Test profile url """
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
