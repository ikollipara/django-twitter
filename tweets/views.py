from typing import Any
from django.db import models
from django.shortcuts import render, resolve_url
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet, Like
from accounts.models import User
from .forms import TweetForm, LikeForm

# Create your views here.


class TweetListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = "tweets/index.html"
    extra_context = {"title": "Twitter - All Tweets"}

    def get_queryset(self):
        qs = (
            Tweet.objects.all()
            .with_author()
            .with_likes()
            .with_is_liked(self.request.user)
        )
        return (
            qs[: int(limit)]
            if (limit := self.kwargs.get("limit")) and limit.isdigit()
            else qs
        )


class TweetByUserListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = "tweets/index.html"
    extra_context = {"title": "Twitter - All Tweets"}

    def get_queryset(self):
        qs = (
            Tweet.objects.tweets_by(self.kwargs["pk"])
            .with_likes()
            .with_author()
            .with_is_liked(self.request.user)
        )
        return (
            qs[: int(limit)]
            if (limit := self.kwargs.get("limit")) and limit.isdigit()
            else qs
        )


class TweetDetailView(LoginRequiredMixin, DetailView):
    model = Tweet
    template_name = "tweets/show.html"

    def get_queryset(self):
        return (
            Tweet.objects.all()
            .with_likes()
            .with_author()
            .with_is_liked(self.request.user)
        )

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

    def form_valid(self, form: TweetForm) -> HttpResponse:
        tweet = form.save(commit=False)
        tweet.author = self.request.user
        tweet.save()
        return HttpResponseRedirect(resolve_url("tweets:detail", pk=tweet.pk))


class TweetUpdateView(LoginRequiredMixin, UpdateView):
    model = Tweet
    template_name = "tweets/edit.html"
    form_class = TweetForm
    extra_context = {"title": "Twitter - Edit Tweet"}


class LikesUpdateView(LoginRequiredMixin, FormView):
    form_class = LikeForm

    def form_valid(self, form: LikeForm) -> HttpResponse:
        tweet = Tweet.objects.get(pk=self.kwargs["pk"])
        user = User.objects.get(pk=form.cleaned_data["user_id"])
        if (like := tweet.likes.filter(user=user)).exists():
            like.delete()
        else:
            like = Like(tweet=tweet, user=user)
            like.save()
        response = render(
            self.request,
            "tweets/_tweet.html",
            {"tweet": tweet, "is_liked": tweet.liked_by(self.request.user)},
        )
        response.status_code = 201
        return response
