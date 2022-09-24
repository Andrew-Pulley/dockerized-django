from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    """Custom User model.  Changing to an email-based login."""

    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_name_or_email(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.email

    def __str__(self):
        return self.get_name_or_email()
