from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import status

class UserListAPITestCase(APITestCase):
    """
    Test case for the User List API endpoint.
    This class tests both authenticated and unauthenticated access to the user list endpoint.
    """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="employee",
            password="testpass123",
            nationality="Paraguay"
        )
        self.token = Token.objects.create(user=self.user)

    def test_user_list_authenticated(self):
        """
        Test that the user list endpoint returns a 200 status code for authenticated users.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_unauthenticated(self):
        """
        Test that the user list endpoint returns a 401 status code for unauthenticated users.
        """
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
