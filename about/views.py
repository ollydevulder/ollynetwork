from django.shortcuts import redirect, render

from .models import Link


def index(request):
    request.session['dark'] = 'hello world'
    context = {
            'links': Link.objects.all(),
    }
    return render(request, 'about/index.html', context)
