from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone

from screener.screeners import get_questions
from screener import forms
from screener.models import Screener

from agilecar import objectmapper

import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return HttpResponse('index')

def create_screener(request):
    """
    @request: HttpRequest
    """
    extra = get_questions(request)
    logger.debug('extra is {0}'.format(extra))
    form = forms.ScreenrForm(request.POST or None, extra=extra)
    if request.method == 'POST':
        if form.is_valid():
            #form.parseJson()
            screener = Screener()
            objectmapper.map(form, screener)
            return HttpResponse(str(extra))

    return render(request, 'screener/create.html', {'form': form})