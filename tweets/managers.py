from django.db import models


class TweetQuerySet(models.QuerySet):
    def with_likes(self):
        return self.annotate(likes_count=models.Count("likes"))


class TweetManager(models.Manager):
    def get_queryset(self):
        return TweetQuerySet(self.model, using=self._db)

    def tweets_by(self, user):
        return self.filter(author=user).order_by("-created_at")
