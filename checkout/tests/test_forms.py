""" Imports """
from django.test import TestCase
from checkout.forms import OrderForm


class TestOrderForm(TestCase):
    """ Test OrderForm """

    def test_empty_form_invalid(self):
        """ Test empty form invalid """
        form = OrderForm({})
        self.assertFalse(form.is_valid())

    def test_form_invalid_wthout_name(self):
        """ Test form invalid without name """
        form = OrderForm({
            'name': '',
            'email': 'email@email.com',
            'phone_number': '123123',
            'address_1': 'test',
            'address_2': 'test',
            'city': 'test',
            'country': 'test',
            'county': 'test',
            'postcode': 'test',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_form_invalid_without_email(self):
        """ Test form invalid without email """
        form = OrderForm({
            'name': 'test',
            'email': '',
            'phone_number': '123123',
            'address_1': 'test',
            'address_2': 'test',
            'city': 'test',
            'country': 'test',
            'county': 'test',
            'postcode': 'test',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())

    def test_form_invalid_without_phone_number(self):
        """ Test form invalid without phone number """
        form = OrderForm({
            'name': 'test',
            'email': 'email@email.com',
            'phone_number': '',
            'address_1': 'test',
            'address_2': 'test',
            'city': 'test',
            'country': 'test',
            'county': 'test',
            'postcode': 'test',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())

    def test_form_invalid_without_address_1(self):
        """ Test form invalid without address 1 """
        form = OrderForm({
            'name': 'test',
            'email': 'email@email.com',
            'phone_number': '123123',
            'address_1': '',
            'address_2': 'test',
            'city': 'test',
            'country': 'test',
            'county': 'test',
            'postcode': 'test',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('address_1', form.errors.keys())

    def test_form_invalid_without_address_2(self):
        """ Test form invalid without address 2 """
        form = OrderForm({
            'name': 'test',
            'email': 'email@email.com',
            'phone_number': '123123',
            'address_1': 'test',
            'address_2': '',
            'city': 'test',
            'country': 'test',
            'county': 'test',
            'postcode': 'test',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('address_2', form.errors.keys())

    def test_form_invalid_without_city(self):
        """ Test form invalid without city"""
        form = OrderForm({
            'name': 'test',
            'email': 'email@email.com',
            'phone_number': '123123',
            'address_1': 'test',
            'address_2': 'test',
            'city': '',
            'country': 'test',
            'county': 'test',
            'postcode': 'test',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('city', form.errors.keys())

    def test_form_invalid_without_country(self):
        """ Test form invalid without country"""
        form = OrderForm({
            'name': 'test',
            'email': 'email@email.com',
            'phone_number': '123123',
            'address_1': 'test',
            'address_2': 'test',
            'city': 'test',
            'country': '',
            'county': 'test',
            'postcode': 'test',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
