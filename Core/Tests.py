import unittest
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import UserInfo


class TestRegistration(TestCase):
    def test_user_registration(self):

        User.objects.create(username='kann', first_name='kann', last_name='kann', email='kann@gmail.com',
                            password='lkjhgfds')
        username = 'kann'
        print(User.objects.values())
        user = User.objects.get(username='kann')
        self.assertTrue(user.username == 'kann')
        self.assertTrue(user.first_name == 'kann')
        self.assertTrue(user.last_name == 'kann')
        self.assertTrue(user.email == 'kann@gmail.com')

    if __name__ == '__main__':
        # unittest.main()
        print("hello")

    def Testbasicinfo(self):
        UserInfo.objects.create(gender='Female', birthDate='1995-01-30', phoneNumber='9440053016',
                                oneLinerStatus='west',country='US',state='NC',region='Charlotte')
        username = 'kann'
        print(UserInfo.objects.values())
        user = UserInfo.objects.get(username='kann')
        self.assertTrue(user.gender == 'Female')
        self.assertTrue(user.birthDate == '2016-01-30')
        self.assertTrue(user.phoneNumber == '9440053016')
        self.assertTrue(user.oneLinerStatus == 'west')
        self.assertTrue(user.country == 'US')
        self.assertTrue(user.state == 'NC')
        self.assertTrue(user.region == 'Charlotte')

    def TestLogin(self):
        c=Client()
        c.post('/core/accounts/login/',
               {'username':'kann','password':'lkjhgfds'})
        response = c.post('/core/',
                          {'username':'kann','password':'llkjhgfds'})
        val=False
        if "Invalid username" not in response.content:
            val=True
            self.assertEqual(val,True)

    def TestLoginSuccess(self):
        c=Client()
        c.post('/core/accounts/login/',
               {'username': 'kann', 'password': 'lkjhgfds'})
        response = c.post('/core/',
                          {'username': 'kann', 'password': 'llkjhgfds'})
        self.assertEqual(response.status_code,200)

    def TestLoginFail(self):
        c=Client()
        c.post('/core/accounts/login/',
               {'username': 'kann', 'password': 'lkjhgfds'})
        response = c.post('/core/accounts/login/',
                          {'username': 'kann', 'password': 'llkjhgfds'})
        val = False
        if "Invalid username" in response.content:
            val=True
        self.assertEqual(val,True)





