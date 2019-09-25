from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(unique=True, error_messages={
            'unique': _('A user with that email already exists.'),
        }, db_index=True)
