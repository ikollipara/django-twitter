from django.http import QueryDict
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django_htmx.http import HttpResponseClientRedirect
from .models import User
from .forms import UserCreateForm, UserEditForm

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
        user: User = self.model.objects.get(pk=self.kwargs["pk"])
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["title"] = f"Twitter - @{user.username}"
        return context

class UserCreateView(CreateView):
    model = User
    template_name = 'accounts/new.html'
    form_class = UserCreateForm

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context["title"] = "Twitter - Create Account"
        return context

class UserEditDetailView(DetailView):
    model = User
    template_name = 'accounts/edit.html'

    def get_context_data(self, **kwargs):
        user: User = self.model.objects.get(pk=self.kwargs["pk"])
        context = super(UserEditDetailView, self).get_context_data(**kwargs)
        context["title"] = f"Twitter - Edit @{user.username}"
        context["form"] = UserEditForm(instance=user)
        return context

    def put(self, request, *args, **kwargs):
        user: User = self.model.objects.get(pk=self.kwargs["pk"])
        form = UserEditForm(QueryDict(request.body), request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseClientRedirect(f"/accounts/{user.pk}")
        return render(request, self.template_name, {"form": form, 'object': user})
