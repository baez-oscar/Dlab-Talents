from django.urls import path
from .views import ReceiptListView, ReceiptFileView

urlpatterns = [
    path('', ReceiptListView.as_view(), name='receipt-list'),
    path('<int:pk>/file/', ReceiptFileView.as_view(), name='receipt-file'),
]