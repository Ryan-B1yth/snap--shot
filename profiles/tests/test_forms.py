""" Imports """
from django.test import TestCase
from profiles.forms import ProfileForm


class TestProfileForm(TestCase):
    """ Test UserProfileForm """

    def test_form_is_valid(self):
        """ Test form is valid """
        form = ProfileForm({})
        self.assertTrue(form.is_valid())