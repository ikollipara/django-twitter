"""
forms.py
Ian Kollipara <ian.kollipara@cune.edu>
2023-12-07

This file contains the forms for the accounts app.
"""

# In Django, this file is often created to hold all forms used in the application.
# You can think of forms as the validation layer of the tool, with the added benefit
# of creating the HTML for you.
# Forms often pull from the models, but they don't have to, and can be used to
# handle data that needs some level of validation.

from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    image = forms.ImageField(required=False)
