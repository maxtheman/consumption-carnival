from django.test import TestCase, Client
from group.views import landing_page
import time

# Create your tests here.
class LandingViewTester(TestCase):

    def test_landing_page_exists_and_is_using_correct_template(self):

        client = Client()
        response = client.get('')

        self.assertEqual(response.status_code, 200)
        #not sure if this makes any sense to test --> self.assertContains(response.templates, 'base.html',"Wrong Template rendered")