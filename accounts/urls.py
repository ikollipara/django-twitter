"""
urls.py
Ian Kollipara <ian.kollipara@cune.edu>
2023-12-07

This file contains the URL patterns for the accounts app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('create', views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/edit', views.UserUpdateView.as_view(), name='user_update'),
    path('', views.UserListView.as_view(), name='user_index'),
]
