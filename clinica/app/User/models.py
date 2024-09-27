from django.db import models

class User(AbstractUser):
    ROLES = (
        ('medico', 'Médico'),
        ('enfermera', 'Enfermera'),
        ('admin', 'Administrativo'),
    )
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLES)

    def __str__(self):
        return self.username
