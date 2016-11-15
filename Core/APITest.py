from django.contrib.auth.models import User
from Core.models import Events
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CreateUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson'}

    def test_can_create_user(self):
        response = self.client.post(reverse('userCollection'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john1', 'john1@snow.com', 'john1password')
        self.client.login(username='john1', password='john1password')
        self.user = User.objects.create(username="mike")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('userCollection'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('user/', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateEventTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson'}

    def test_can_create_user(self):
        response = self.client.post(reverse('userCollection'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadEventTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john1', 'john1@snow.com', 'john1password')
        self.client.login(username='john1', password='john1password')
        self.user = User.objects.create(username="mike")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('userCollection'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('user/', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
