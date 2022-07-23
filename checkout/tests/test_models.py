""" Imports """
from django.test import TestCase
from products.models import Category, Product
from checkout.models import Order, OrderLineItem


class TestOrderModels(TestCase):
    """ Test order models """
    def setUp(self):
        """ Set up """
        self.category = Category.objects.create(
                name='test',
                friendly_name="Test"
            )

        self.product = Product.objects.create(
            category=self.category,
            name='Test1',
            description='Test1',
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

    def test_order_number(self):
        """ Test order number """
        self.assertTrue(self.order.order_no)

    def test_grand_total(self):
        """ Test grand total"""
        self.assertEqual(str(round(self.order.grand_total, 2)), '11.00')

    def test_lineitem_total(self):
        """ Test line item total """
        self.assertTrue(self.lineitem.lineitem_total)
        self.assertEqual(self.lineitem.lineitem_total, '10')
