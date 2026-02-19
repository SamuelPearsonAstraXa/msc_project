from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    username = models.CharField(_('username'), unique=True, default='')
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(upload_to='accounts/avatars', default='accounts/avatars/avatar.png', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email