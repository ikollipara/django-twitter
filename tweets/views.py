from django.shortcuts import render, resolve_url
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from accounts.models import User
from .forms import TweetForm, LikeForm

# Create your views here.


class TweetListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = "tweets/index.html"
    extra_context = {"title": "Twitter - All Tweets"}


class TweetByUserListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = "tweets/index.html"
    extra_context = {"title": "Twitter - All Tweets"}

    def get_queryset(self):
        return Tweet.objects.filter(author=self.kwargs["pk"]).order_by("-created_at")[
            : self.kwargs.get("limit", 10)
        ]


class TweetDetailView(LoginRequiredMixin, DetailView):
    model = Tweet
    template_name = "tweets/show.html"

    def get_context_data(self, **kwargs):
        context = super(TweetDetailView, self).get_context_data(**kwargs)
        object = self.get_object()
        context["title"] = f"Twitter - @{object.author.username} Tweet {object.pk}"
        return context


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    template_name = "tweets/new.html"
    form_class = TweetForm
    extra_context = {"title": "Twitter - Create Tweet"}


class TweetUpdateView(LoginRequiredMixin, UpdateView):
    model = Tweet
    template_name = "tweets/edit.html"
    form_class = TweetForm
    extra_context = {"title": "Twitter - Edit Tweet"}


class Likes(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        form = LikeForm(request.POST)
        if form.is_valid():
            tweet = Tweet.objects.get(pk=kwargs.pk)
            user = User.objects.get(pk=form.cleaned_data["user_id"])
            if tweet.likes.filter(pk=user.pk).exists():
                tweet.likes.remove(user)
            else:
                tweet.likes.add(user)
                response = HttpResponseRedirect(resolve_url("tweet_detail", tweet.pk))
                response.status_code = 303
                response["HX-Refresh"] = True
                return response
