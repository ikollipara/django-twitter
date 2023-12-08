from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True


    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context["title"] = "Twitter - Login"
        return context



class UserLogoutView(LogoutView):
    template_name = 'auth/logout.html'

    def get_context_data(self, **kwargs):
        context = super(UserLogoutView, self).get_context_data(**kwargs)
        context["title"] = "Twitter - Logout"
        return context
