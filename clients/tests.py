from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ClientTests(APITestCase):
    def test_create_client(self):
        url = reverse("client-list")
        data = {
            "name": "Test Client",
            "email": "client@example.com",
            "city": "Moscow",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
