from django.shortcuts import render
from django.http import HttpResponse
from .form import VotingForm
from .form import OPTIONS_VOTING
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# Create your views here.

def index(request, value):
    return render(request, 'index.html', {'request': request, 'value': value })

def voting(request):
    if request.method == 'POST':
        form = VotingForm(request.POST or None)
        if form.is_valid():
            for option in dict(OPTIONS_VOTING).keys():
                option_vote = dict(request.POST.lists()).get(option)
                if option_vote:
                    value = option_vote[0]
                    if cache.get(value):
                        cache.incr(value)
                    else:
                        cache.set(option_vote[0], 1, timeout=300)
                    print(f'{value}: votes: [{cache.get(value)}]')
            return render(request, 'voting.html', {'form': form, 'request': request })
    form = VotingForm()
    return render(request, 'voting.html', {'form': form})