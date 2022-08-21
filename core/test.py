from urllib import response
from django.test import TestCase

class TestPage(TestCase):
    def test_index_page_working(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        self.assertContains(response, 'BookTime')