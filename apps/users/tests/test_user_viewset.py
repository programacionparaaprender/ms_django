from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.users.infraestructure.models import User

class UserViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(name='Luis', email='luis@example.com')

    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_create_user(self):
        url = reverse('user-list')
        data = {'name': 'Ana', 'email': 'ana@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user.id])
        data = {'name': 'Luis Editado', 'email': 'luis@example.com'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, 'Luis Editado')

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
