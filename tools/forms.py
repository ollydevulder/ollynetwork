from django import forms

from . import models


class BirthdayForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password'
        })
    )

class ShortForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={
        'placeholder': 'URL to shorten',
        'title': 'URL'
        })
    )
