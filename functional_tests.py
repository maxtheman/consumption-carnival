from selenium import webdriver
import unittest

class TestLandingPage(unittest.TestCase):

    browser = webdriver.Chrome()

    def setUp(self):
        self.browser.get('http://localhost:8000/')

    def tearDown(self):
        self.browser.quit()

    #First user lands on landing page and decides to create an account and sign in
    def test_landing_page_can_create_account_and_redirect(self):

        class User:
            def __init__(self, name, password):
                self.name = name
                self.password = password

        account_info = self.browser.find_element_by_tag_name("account_info")
        user_name = account_info.find_element_by_tag_name("user_name")
        password = account_info.find_element_by_tag_name("pass_field")

        bob = User("Killer BOB")

        user_name.send_keys(bob.name)
        password.send_keys(bob.password, Keys.ENTER)


if __name__ == '__main__':
    unittest.main()