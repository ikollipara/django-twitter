from django.urls import path

from . import views

urlpatterns = [
    path("tweets/", views.TweetListView.as_view(), name="tweet_index"),
    path("tweets/new", views.TweetCreateView.as_view(), name="tweet_create"),
    path("tweets/<int:pk>/", views.TweetDetailView.as_view(), name="tweet_detail"),
    path("tweets/<int:pk>/edit", views.TweetUpdateView.as_view(), name="tweet_update"),
    path("<int:pk>/tweets/", views.TweetByUserListView.as_view(), name="tweet_by_user"),
    path("tweets/<int:pk>/likes", views.LikesUpdateView.as_view(), name="tweet_like"),
]
