from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from hashid_field import HashidField

from users.managers import UserManager


class Users(AbstractUser):
    id = HashidField(primary_key=True)
    username = None
    email = models.EmailField(('email address'), unique=True)
    disabled = models.BooleanField(default=False)
    email_confirm = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email