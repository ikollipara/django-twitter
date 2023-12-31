from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import UserUpdateForm, UserCreationForm

# Create your views here.


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "accounts/index.html"

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context["title"] = "Twitter - All Users"
        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/show.html"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["title"] = f"Twitter - @{self.get_object().username}"
        context["tweets"] = (
            self.get_object()
            .tweets.order_by("-created_at")
            .all()
            .with_likes()
            .with_author()
            .with_is_liked(self.request.user)[:10]
        )
        return context


class UserCreateView(CreateView):
    model = User
    template_name = "accounts/new.html"
    form_class = UserCreationForm

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context["title"] = "Twitter - Create Account"
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "accounts/edit.html"
    form_class = UserUpdateForm
