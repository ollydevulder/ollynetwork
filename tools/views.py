from django.shortcuts import get_object_or_404, redirect, render

from . import models
from . import forms


def birthday(request, **kwargs):
    # <str:person>
    birthday = get_object_or_404(models.Birthday, pk=kwargs['person'])
    context = {
        'birthday': birthday,
    }
    if request.method == 'POST':
        form = forms.BirthdayForm(request.POST)
        # Ignore the very high security
        if form.is_valid() and form.cleaned_data['password'] == birthday.password:
            # Give access to Birthday
            return render(request, 'tools/birthday.html', context)
    else:
        form = forms.BirthdayForm

    context['form'] = form
    return render(request, 'tools/birthday_form.html', context)
