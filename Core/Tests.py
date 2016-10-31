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
        User.objects.create(username='chinm',first_name='chinm',last_name='chinm',email='chinm@gmail.com',password='zxcvbnml')
        username = 'chinm'
        print(User.objects.values())
        user = User.objects.get(username='chinm')
        #self.assertIn(b'you logged in', response.data)
        self.assertTrue(user.username == 'chinm')
        self.assertTrue(user.first_name == 'chinm')
        self.assertTrue(user.last_name == 'chinm')
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
     self.assertTrue(user.birthDate == '1995-01-12')
     self.assertTrue(user.phoneNumber == '9440053016')
     self.assertTrue(user.oneLinerStatus == 'sporty')



