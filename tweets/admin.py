from django.contrib import admin

from .models import Tweet, Like

# Register your models here.


class LikeInline(admin.TabularInline):
    model = Like
    extra = 0


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    """Admin View for Tweet"""

    inlines = [LikeInline]
