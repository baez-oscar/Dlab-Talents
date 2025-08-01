from rest_framework import serializers
from .models import Receipt

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = [
            'id', 'created_at', 'modified_at', 'is_active',
            'full_date', 'year', 'month', 'type',
            'is_sended', 'is_readed', 'is_signed',
            'sended_date', 'readed_date', 'signed_date',
            'employee', 'employee_full_name', 'employee_number'
        ]
