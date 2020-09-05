from django.test import TestCase, SimpleTestCase
# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        print('home test')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about/')
        print('about test')
        self.assertEqual(response.status_code, 200)
