"""
models.py
Ian Kollipara <ian.kollipara@cune.edu>
2023-12-07

This file contains the models for the accounts app.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

# In Django, there is already a built-in User model,
# however, it is recommended to subclass, even if
# you don't add any additional fields, as it allows
# for easier customization in the future.
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    The User model is a subclass of the built-in
    AbstractUser model. This allows for easier
    customization in the future.

    The AbstractUser model already has the following
    fields:
        - username
        - first_name
        - last_name
        - email
        - password
        - groups
        - user_permissions
        - is_staff
        - is_active
        - is_superuser
        - last_login
        - date_joined
        - _avatar
    """
    # The use of ... is to give a body to the class,
    # but not actually add anything to it.
    # If you prefer `pass`, that is fine too.

    _avatar = models.ImageField(_("Avatar"), upload_to="avatars", blank=True)
    bio = models.TextField(_("Bio"), blank=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def __str__(self) -> str:
        return f"@{self.username}"

    @property
    def avatar(self):
        return self._avatar if self._avatar else {"url": f"https://ui-avatars.com/api/?name={self.first_name}+{self.last_name}&size=256"}

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
