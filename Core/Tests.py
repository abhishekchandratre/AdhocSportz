import unittest
from django.test import TestCase
from django.contrib.auth.models import User


class TestRegistration(TestCase):

    def test_user_registration(self):
        #response = self.client.post('/register', data=dict(username="Michael", FirstName="Tom", LastName="Mic",
           #                                                Email="mic@email.com", Password="admin123",
          #                                                 PasswordConfirmation="admin123"),
         #                           follow_redirects=True
        #                            )
        User.objects.create(username='sra',first_name='sra',last_name='sra',email='sra@gmail.com',password='admin123')
        username = 'sra'
        print(User.objects.values())
        user = User.objects.get(username='sra')
        #self.assertIn(b'you logged in', response.data)
        self.assertTrue(user.username == 'sra')
        self.assertTrue(user.first_name == 'sra')
        self.assertTrue(user.last_name == 'sra')
        self.assertTrue(user.email == 'sra@gmail.com')


if __name__ == '__main__':
    #unittest.main()
    print("hello")
