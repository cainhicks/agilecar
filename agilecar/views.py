from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone

import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'jobposting/index.html', None)