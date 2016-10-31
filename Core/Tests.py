import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserInfo

class TestRegistration(TestCase):
 def test_user_registration(self):

        User.objects.create(username='kann',first_name='kann',last_name='kann',email='kann@gmail.com',password='lkjhgfds')
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
  UserInfo.objects.create(gender='Female', birthDate='2016-01-01', phoneNumber='9440053016', oneLinerStatus='west')
  username = 'kann'
  print(UserInfo.objects.values())
  user = UserInfo.objects.get(username='kann')
  self.assertTrue(user.gender == 'Female')
  self.assertTrue(user.birthDate == '2016-01-01')
  self.assertTrue(user.phoneNumber == '9440053016')
  self.assertTrue(user.oneLinerStatus == 'west')

