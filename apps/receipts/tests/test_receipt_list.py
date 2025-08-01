from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import status
from receipts.models import Receipt

class ReceiptListAPITestCase(APITestCase):
    """
    Test case for the Receipt List API endpoint.
    This class tests both authenticated and unauthenticated access to the receipt list endpoint.
    """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="employee2",
            password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        Receipt.objects.create(
            year=2024,
            month=8,
            type="monthly",
            is_active=True,
            employee=self.user,
            employee_number=12345,
            full_date="2024-08-01"
        )


    def test_receipt_list_authenticated(self):
        """
        Test that the receipt list endpoint returns a 200 status code for authenticated users.
        It also checks that the response contains at least one receipt.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get("/receipts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_receipt_list_unauthenticated(self):
        """
        Test that the receipt list endpoint returns a 401 status code for unauthenticated users.
        This ensures that the endpoint is protected and requires authentication.
        """
        response = self.client.get("/receipts/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
