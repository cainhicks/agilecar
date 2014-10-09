from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone

from screener.screeners import get_questions
from screener import forms
from screener.models import Screener, load_screener

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
            screener.name = form.cleaned_data['name']
            screener.save_screeners(form.questions_as_dict())
            return HttpResponse(str(screener.id))
    

    return render(request, 'screener/create.html', {'form': form})

def edit(request, screener_id):
    extra = get_questions(request)
    form = forms.ScreenrForm(request.POST or None, extra = extra)
    screener = load_screener(screener_id)
    if request.method == 'POST':
        if form.is_valid():
            screener.name = form.cleaned_data['name']
            screener.save_screeners(form.questions_as_dict())
            return HttpResponse(str(screener.id))
    else:
        pass
    return render(request, 'screener/edit.html', {'form': form})