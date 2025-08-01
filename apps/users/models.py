from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class User(AbstractUser):

    """
    m¿modelo de usuario personalizado que extiende AbstractUser
    y agrega campos adicionales específicos de la aplicación.
    """
    nationality = models.CharField(max_length=100, blank=True, null=True)
    employee_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    required_password_changed_done = models.BooleanField(default=False)
    has_pending_receipts_to_sign = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(default=now)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self) -> str:
        """
        Devuelve el nombre completo del usuario.
        """
        return f"{self.first_name} {self.last_name}".strip()