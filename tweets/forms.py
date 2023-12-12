from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    body = forms.CharField(
        label="Tweet", required=True, widget=forms.Textarea(attrs={"rows": 5})
    )

    class Meta:
        model = Tweet
        fields = ("body",)


class LikeForm(forms.Form):
    user_id = forms.IntegerField()
