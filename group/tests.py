from django.test import TestCase, Client
from group.views import landing_page
import time

# Create your tests here.
class LandingViewTester(TestCase):

    client = Client()

    def test_landing_page_exists_and_renders_correctly(self):

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(["landing.html","base.html"], [t.name for t in response.templates])

    def test_landing_can_return_errors(self):

        response = self.client.post('', {"username": "The Arm", "password": "lauriepalmer1"})
        code = response.status_code

        self.assertEqual(code, 200, msg="status code is equal to %s, not 200" % code)
        self.assertTrue(response.context["username"] != None , msg="Username doesn't exist")
        self.assertTrue(response.context["username"] != "" , msg="Username is empty")
        self.assertTrue(response.context["password"] != None , msg="Password doesn't exist")
        self.assertTrue(response.context["password"] != "" , msg="Password doesn't exist")

        self.assertIn("Error", response.context["error"])
