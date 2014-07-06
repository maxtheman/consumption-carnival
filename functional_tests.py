from selenium import webdriver
import unittest

class TestLandingPage(unittest.TestCase):

    browser = webdriver.Chrome()

    def setUp(self):
        self.browser.get('http://localhost:8000/')

    def tearDown(self):
        self.browser.quit()

    def test_nothing(self):
        self.assertTrue(1==2)

if __name__ == '__main__':
    unittest.main()