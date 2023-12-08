from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class UserListView(ListView):
    model = User
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context["title"] = "Twitter - All Users"
        return context

class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/show.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["title"] = f"Twitter - @{self.model.username}"
        return context

class UserCreateView(CreateView):
    model = User
    template_name = 'accounts/new.html'
    form_class = UserCreationForm

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context["title"] = "Twitter - Create Account"
        return context
