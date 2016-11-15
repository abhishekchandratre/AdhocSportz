from django.test import TestCase
from django.core.urlresolvers import reverse
import unittest
from selenium import webdriver
from Core.forms import LoginForm


class TestURL(TestCase):
    def test_index_without_login(self):
        url = reverse("index")
        print(url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()


class TestForms(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_LoginForm_valid(self):
        data = {'username': 'test1', 'password': 'test1'}
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_LoginForm_invalid(self):
        data = {'username': '', 'password': 'test1'}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

    #def RegistrationForm(self):
    #    data = {'email':'test@gmail.com','username':, 'first_name', 'last_name', 'email', 'password1', 'password2'}

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
