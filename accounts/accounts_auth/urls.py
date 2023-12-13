from django.urls import path

from . import views

app_name = "accounts_auth"

urlpatterns = [
    path("login/", views.AccountsLoginView.as_view(), name="login"),
    path("logout/", views.AccountsLogoutView.as_view(), name="logout"),
]
