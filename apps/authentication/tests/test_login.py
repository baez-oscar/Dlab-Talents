from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

class LoginAPITestCase(APITestCase):
    """
    Test case for the Login API endpoint.
    This class tests both successful and failed login attempts.
    """
    def setUp(self):
        self.username = "testuser"
        self.password = "testpass123"
        self.user = get_user_model().objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_success(self):
        """
        Test that the login endpoint returns a 200 status code and a token for valid credentials.
        """
        response = self.client.post("/auth/login/", {
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_login_fail(self):
        """
        Test that the login endpoint returns a 400 status code for invalid credentials.
        """
        response = self.client.post("/auth/login/", {
            "username": self.username,
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
