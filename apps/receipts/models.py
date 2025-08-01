from django.db import models
from django.utils.timezone import now
from users.models import User
from django.core.files.storage import FileSystemStorage
receipt_storage = FileSystemStorage(location='media/receipts')

class Receipt(models.Model):
    """
    Modelo que representa un recibo asociado a un usuario.
    Incluye campos para almacenar información del recibo, como fecha, tipo, estado y archivo PDF asociado.
    """
    created_at = models.DateTimeField(default=now)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    full_date = models.DateField()
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.CharField(max_length=100)

    is_sended = models.BooleanField(default=False)
    is_readed = models.BooleanField(default=False)
    is_signed = models.BooleanField(default=False)

    sended_date = models.DateTimeField(blank=True, null=True)
    readed_date = models.DateTimeField(blank=True, null=True)
    signed_date = models.DateTimeField(blank=True, null=True)

    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receipts")
    employee_full_name = models.CharField(max_length=255)
    employee_number = models.IntegerField()

    file = models.FileField(upload_to='receipts/', storage=receipt_storage, null=True, blank=True)

    def __str__(self):
        return f"{self.year}/{self.month} - {self.employee_full_name}"