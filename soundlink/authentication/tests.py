import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status

User = get_user_model()


class JWTAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="test123",
        )

    def _get_tokens(self):
        response = self.client.post(
            "/api/login/", json.dumps(
                {
                    "username": "testuser",
                    "password": "test123"
                }
            ),
            content_type="application/json",
        )
        return response.json()
