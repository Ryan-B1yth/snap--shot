""" Imports """
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class TestProfileModels(TestCase):
    """ Test product models """
    def setUp(self):
        """ Set up """
        self.user = User.objects.create(
                username="test",
                password="testpassword"
            )
        self.userprofile = Profile.objects.get(user=self.user)

    def test_profile_created_successfully(self):
        """ Test profile created successfully """
        self.assertTrue(self.userprofile)
