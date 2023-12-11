from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Tweet(models.Model):
    '''Model definition for Tweet.'''

    body = models.CharField(_("Body"), max_length=255)
    author = models.ForeignKey("accounts.User", verbose_name=_("Author"), on_delete=models.CASCADE, related_name="tweets")

    class Meta:
        '''Meta definition for Tweet.'''

        verbose_name = _('Tweet')
        verbose_name_plural = _('Tweets')

    def __str__(self):
       return f"{self.author} - {self.body}"


class Like(models.Model):
    '''Model definition for Like.'''

    tweet = models.ForeignKey("tweets.Tweet", verbose_name=_("Tweet"), on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey("accounts.User", verbose_name=_("User"), on_delete=models.CASCADE, related_name="likes")

    class Meta:
        '''Meta definition for Like.'''

        verbose_name = _('Like')
        verbose_name_plural = _('Likes')

    def __str__(self):
        return f"{self.objects.count()} for {self.tweet}"
