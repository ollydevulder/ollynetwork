from django.shortcuts import get_object_or_404, redirect, render

from . import models


def birthday(request, **kwargs):
    # <str:person>
    birthday = get_object_or_404(models.Birthday, pk=kwargs['person'])
    context = { 'birthday': birthday }
    return render(request, 'tools/birthday.html', context)
