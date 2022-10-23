from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from hashid_field import HashidAutoField

from users.managers import UserManager


class Users(AbstractUser):
    id = HashidAutoField(primary_key=True)
    username = None
    email = models.EmailField(('email address'), unique=True)
    disabled = models.BooleanField(default=True)
    email_confirm = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(Users, null= True, on_delete = models.SET_NULL, related_name='profile')
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}  Profile'