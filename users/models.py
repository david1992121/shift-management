from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Account(AbstractBaseUser):
    """
    A model for users

    It simply has the three fields `username`, `password`, `last_login`.
    In addition, it has several shifts.
    """
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
