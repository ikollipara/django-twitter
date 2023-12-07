"""
models.py
Ian Kollipara <ian.kollipara@cune.edu>
2023-12-07

This file contains the models for the accounts app.
"""

from django.db import models

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
    """
    # The use of ... is to give a body to the class,
    # but not actually add anything to it.
    # If you prefer `pass`, that is fine too.
    ...
