from django import forms

from . import models


class BirthdayForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['placeholder'] = 'password'
        
    class Meta:
        model = models.Birthday
        fields = ['password']
