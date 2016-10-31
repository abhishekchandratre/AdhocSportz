import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserInfo
class TestRegistration(TestCase):

    def test_user_registration(self):
        #response = self.client.post('/register', data=dict(username="Michael", FirstName="Tom", LastName="Mic",
           #                                                Email="mic@email.com", Password="admin123",
          #                                                 PasswordConfirmation="admin123"),
         #                           follow_redirects=True
        #                            )
        User.objects.create(username='chinm',first_name='chinm',last_name='blanc',email='chinm@gmail.com',password='zxcvbnml')
        username = 'chinm'
        print(User.objects.values())
        user = User.objects.get(username='chinm')
        #self.assertIn(b'you logged in', response.data)
        self.assertTrue(user.username == 'chinm')
        self.assertFalse(user.username == 'john')
        self.assertTrue(user.first_name == 'chinm')
        self.assertFalse(user.first_name == 'matt')
        self.assertTrue(user.last_name == 'blanc')
        self.assertFalse(user.last_name == 'chinm')
        self.assertFalse(user.email == 'matt@gmail.com')
        self.assertTrue(user.email == 'chinm@gmail.com')



    if __name__ == '__main__':
     #unittest.main()
     print("hello")


    def Testbasicinfo(self):
        UserInfo.objects.create(gender='Male', birthDate='1995-01-12', phoneNumber='9440053016', oneLinerStatus='sporty')
        username = 'chinm'
        print(User.objects.values())
        user = UserInfo.objects.get(username='chinm')
        # self.assertIn(b'you logged in', response.data)
        self.assertTrue(user.gender == 'Male')
        self.assertFalse(user.gender == 'Female')
        self.assertTrue(user.birthDate == '1995-01-12')
        self.assertFalse(user.birthDate == '1996-10-12')
        self.assertTrue(user.phoneNumber == '9440053016')
        self.assertFalse(user.phoneNumber == '7894578845')
        self.assertTrue(user.oneLinerStatus == 'sporty')





