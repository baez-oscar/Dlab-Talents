from django.core.management.base import BaseCommand
from users.models import User
from receipts.models import Receipt
from django.core.files import File
from django.utils.timezone import now
import os
import random

NAMES = [
    ("Ana", "Gómez"),
    ("Luis", "Martínez"),
    ("Sofía", "Ramírez"),
    ("Carlos", "Duarte"),
    ("Lucía", "Fernández"),
    ("Diego", "Torres"),
    ("María", "López"),
    ("Javier", "Acosta"),
    ("Paula", "Benítez"),
    ("Tomás", "Vera"),
]

NATIONALITIES = ["Paraguay", "Argentina", "Chile", "Uruguay"]
TYPES = ["Monthly", "Extra", "Holiday"]

class Command(BaseCommand):
    help = 'Carga 10 usuarios y recibos de ejemplo con PDFs'

    def handle(self, *args, **kwargs):
        pdf_path = os.path.join("media", "receipts", "demo.pdf")

        for i, (first, last) in enumerate(NAMES):
            username = f"user{i+1}"
            email = f"{first.lower()}.{last.lower()}@example.com"
            emp_number = 1000 + i

            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "first_name": first,
                    "last_name": last,
                    "email": email,
                    "nationality": random.choice(NATIONALITIES),
                    "employee_number": emp_number,
                }
            )
            if created:
                user.set_password("test1234")
                user.save()

            receipt = Receipt.objects.create(
                full_date=now().date(),
                year=2025,
                month=random.randint(1, 12),
                type=random.choice(TYPES),
                is_sended=random.choice([True, False]),
                is_signed=False,
                is_readed=False,
                employee=user,
                employee_full_name=f"{first} {last}",
                employee_number=emp_number,
            )

            print("Id del recibo:", receipt.id)
            print("Path del PDF:", pdf_path)
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as f:

                    receipt.file.save(f"{username}.pdf", File(f), save=True)
                #receipt.save()  # ✅ guardamos los cambios en el modelo
                print(f"PDF asociado a {username}")
            else:
                print(f"PDF no encontrado: {pdf_path}")
            self.stdout.write(self.style.SUCCESS(f"{username} y recibo creados."))

        self.stdout.write(self.style.SUCCESS("✔️ Carga completa de datos sintéticos."))
