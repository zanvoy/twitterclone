from django import forms
from tweet.models import Tweet

class TweetAddForm(forms.Form):
    body = forms.CharField(max_length=140, widget=forms.Textarea)
