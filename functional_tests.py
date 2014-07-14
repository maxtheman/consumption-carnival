from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestMainPages(unittest.TestCase):

    browser = webdriver.Chrome()

    def setUp(self):
        self.browser.get('http://localhost:8000/')
        time.sleep(3)

    def tearDown(self):
        self.browser.quit()

    #First user lands on landing page and decides to create an account and sign in
    def test_landing_page_can_create_account_and_redirect(self):

        class User:
            def __init__(self, name, password):
                self.name = name
                self.password = password

        account_info = self.browser.find_element_by_id("account_info")
        user_name = account_info.find_element_by_id("user_name")
        password = account_info.find_element_by_id("pass_field")

        bob = User("Killer BOB","garmonbozia")

        #There are no errors
        self.assertNotIn("Error",account_info.text, msg="There is an error present before login attempt")

        #user attempts to login
        user_name.send_keys(bob.name)
        password.send_keys(bob.password, Keys.ENTER)

        #His first attempt fails
        self.assertIn("Error", account_info.text, msg="There is NOT an error present after login failure")

        #He recalls his password and his login works
        bob.password = "flowers"

        user_name.send_keys(bob.name)
        password.send_keys(bob.password, Keys.ENTER)





if __name__ == '__main__':
    unittest.main()