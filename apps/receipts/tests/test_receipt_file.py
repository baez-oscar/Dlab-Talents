import io
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from receipts.models import Receipt

class ReceiptFileDownloadTestCase(APITestCase):
    """Test case for downloading receipt files.
    This class tests both authenticated and unauthenticated access to the receipt file download endpoint."""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="pdfuser",
            password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)

        self.fake_pdf = SimpleUploadedFile(
            "receipt.pdf", b"%PDF-1.4\n%Fake PDF content", content_type="application/pdf"
        )

        self.receipt = Receipt.objects.create(
            year=2024,
            month=8,
            type="monthly",
            is_active=True,
            full_date="2024-08-01",
            employee=self.user,
            employee_number=777,
            file=self.fake_pdf  # <- asociamos el archivo aquí
        )

    def test_download_receipt_pdf_authenticated(self):
        """
        Test that the receipt file download endpoint returns a 200 status code and the correct content type for authenticated users.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = f"/receipts/{self.receipt.id}/file/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")
        first_chunk = next(response.streaming_content)
        self.assertTrue(first_chunk.startswith(b"%PDF"))

    def test_download_receipt_pdf_unauthenticated(self):
        """
        Test that the receipt file download endpoint returns a 401 status code for unauthenticated users.
        """
        url = f"/receipts/{self.receipt.id}/file/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 401)  # Unauthorized
