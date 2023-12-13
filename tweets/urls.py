from django.urls import path

from . import views

app_name = "tweets"

urlpatterns = [
    path("tweets/", views.TweetListView.as_view(), name="index"),
    path("tweets/new/", views.TweetCreateView.as_view(), name="create"),
    path("tweets/<int:pk>/", views.TweetDetailView.as_view(), name="detail"),
    path("tweets/<int:pk>/edit/", views.TweetUpdateView.as_view(), name="update"),
    path("<int:pk>/tweets/", views.TweetByUserListView.as_view(), name="by_user"),
    path("tweets/<int:pk>/likes/", views.LikesUpdateView.as_view(), name="like"),
]
