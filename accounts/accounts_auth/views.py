from typing import Any
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, resolve_url

from django.contrib.auth.views import LoginView, LogoutView
from django.template.response import TemplateResponse
from accounts.models import User

# Create your views here.


class AccountsLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        if self.kwargs.get("next"):
            return self.request.kwargs.get("next")
        return resolve_url("user_detail", self.request.user.pk)


class AccountsLogoutView(LogoutView):
    template_name = "auth/logout.html"

    def post(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> TemplateResponse:
        response = super().post(request, *args, **kwargs)
        response["HX-Refresh"] = True
        return response
