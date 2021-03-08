from django.forms import fields
from .models import Tweet
from django import forms

class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('text',)