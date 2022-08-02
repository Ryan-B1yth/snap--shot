""" Imports """
from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Testimony


class TestTestimonyModels(TestCase):
    """ Test product models """
    def setUp(self):
        """ Generate test data """
        self.user = User.objects.create(
                username="test",
                password="testpassword"
            )
        self.testimony = Testimony.objects.create(
                user=self.user,
                body="Test-imony"
            )

    def test_testimony_string(self):
        """ Test product string method """
        self.assertEqual(str(self.testimony), "test: Test-imony")
