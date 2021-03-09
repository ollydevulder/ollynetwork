from django.shortcuts import get_object_or_404, redirect, render

from . import models
from . import forms


def birthday(request, **kwargs):
    # birthday/<str:person>
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


def short_set(request, **kwargs):
    # /!
    context = {}
    if request.method == 'POST':
        form = forms.ShortForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            if not len(models.Short.objects.filter(long=url)):
                url = models.Short(long=url)
                url.save()
            else:
                url = models.Short.objects.get(long=url)
            context['success'] = url
            context['path'] = request.build_absolute_uri() + url.short
        else:
            context['form'] = form
            return render(request, 'tools/short_set.html', context)
                
    context['form'] = forms.ShortForm
    return render(request, 'tools/short_set.html', context)

def short(request, **kwargs):
    # /!<str:url>
    short = get_object_or_404(models.Short, short=kwargs['url'])
    return redirect(short.long)
