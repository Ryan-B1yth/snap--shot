""" Imports """
from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Testimony
from home.forms import TestimonyForm


class TestTestimonyForm(TestCase):
    """ Test Testimony """

    def setUp(self):
        """ Set up """
        self.user = User.objects.create(
                username="test",
                password="testpassword"
            )

        self.testimony = Testimony.objects.create(
                user=self.user,
                body="Test-imony"
            )

    def test_empty_form_invalid(self):
        """ Test empty form invalid """
        form = TestimonyForm({})
        self.assertFalse(form.is_valid())

    def test_form_invalid_without_user(self):
        """ Test form without user """
        form = TestimonyForm({
            'user': '',
            'body': 'Test-imony'
            })
        self.assertFalse(form.is_valid())

    def test_form_invalid_without_body(self):
        """ Test form without body """
        form = TestimonyForm({
            'user': self.user,
            'body': ''
            })
        self.assertFalse(form.is_valid())
