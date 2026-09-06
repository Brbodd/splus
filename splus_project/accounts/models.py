from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    phone_number = models.CharField(
        max_length=11,
        unique=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.phone_number