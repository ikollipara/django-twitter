from django.db import models
from django.apps import apps


class TweetQuerySet(models.QuerySet):
    def with_likes(self):
        return self.annotate(likes_count=models.Count("likes"))

    def with_author(self):
        return self.select_related("author")

    def with_is_liked(self, user):
        return self.annotate(
            is_liked=models.Exists(
                apps.get_model("tweets", "Like").objects.filter(
                    tweet=models.OuterRef("pk"), user=user
                )
            )
        )


class TweetManager(models.Manager):
    def get_queryset(self):
        return TweetQuerySet(self.model, using=self._db)

    def tweets_by(self, user):
        return self.filter(author=user).order_by("-created_at")
