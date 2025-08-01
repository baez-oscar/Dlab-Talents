from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.http import FileResponse, Http404
from .models import Receipt
from .serializers import ReceiptSerializer

class ReceiptListView(ListAPIView):
    """
    view to list all receipts with filtering options.
    requires authentication and supports filtering by year, month, and employee number.
    """
    queryset = Receipt.objects.all().order_by('-year', '-month')
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['year', 'month', 'employee_number']

class ReceiptFileView(APIView):
    """
    View to download a receipt's PDF file.
    Requires authentication and returns a FileResponse with the PDF content.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            receipt = Receipt.objects.get(pk=pk)
            if not receipt.file:
                raise Http404("Receipt has no file.")
            return FileResponse(receipt.file.open(), content_type='application/pdf')
        except Receipt.DoesNotExist:
            raise Http404("Receipt not found.")