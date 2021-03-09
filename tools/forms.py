from django import forms

from . import models


class BirthdayForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password'
        })
    )
