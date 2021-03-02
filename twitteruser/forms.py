from django import forms
from .models import TwitterUser
from django.forms.widgets import PasswordInput


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    
    class Meta:
        model = TwitterUser
        fields = ('username', 'password')