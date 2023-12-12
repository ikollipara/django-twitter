from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.AccountsLoginView.as_view(), name="user_login"),
    path("logout/", views.AccountsLogoutView.as_view(), name="user_logout"),
]
