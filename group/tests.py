from django.test import TestCase, Client
from group.views import landing_page

# Create your tests here.
class LandingViewTester(TestCase):

    def test_landing_page_exists_and_is_using_correct_template(self):

        c = Client()

        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response.templates, 'base.html')