from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=15,
        unique=True,
        help_text="Required and unique",
        error_messages={"unique": "A user with that username already exists"},
    )
    email = models.EmailField(
        unique=True,
        help_text="Required and unique",
        error_messages={"unique": "A user with that email already exists"},
    )

    def __str__(self):
        return self.username
