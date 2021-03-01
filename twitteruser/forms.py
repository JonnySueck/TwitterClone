from django import forms
from .models import MyCustomUser
from django.forms.widgets import PasswordInput


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    
    class Meta:
        model = MyCustomUser
        fields = ('username', 'password')