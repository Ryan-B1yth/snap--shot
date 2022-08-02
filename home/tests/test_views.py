""" Imports """
from django.test import TestCase


class TestViews(TestCase):
    """ Test home view """
    def test_home_view(self):
        """ Test home view """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_testimony_view(self):
        """ Test testimony view """
        response = self.client.get('/testimonies/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/testimonies.html')
