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
        if (limit := self.kwargs.get("limit")) and limit.isdigit():
            return Tweet.objects.all().with_likes()[: int(limit)]
        return Tweet.objects.all().with_likes()


class TweetByUserListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = "tweets/index.html"
    extra_context = {"title": "Twitter - All Tweets"}

    def get_queryset(self):
        if (limit := self.kwargs.get("limit")) and limit.isdigit():
            return Tweet.objects.tweets_by(self.kwargs["pk"])[: int(limit)]
        return Tweet.objects.tweets_by(self.kwargs["pk"])


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
        response = HttpResponseRedirect(resolve_url("tweet_detail", pk=tweet.pk))
        response.status_code = 303
        return response
